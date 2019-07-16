#!/usr/bin/env python


#%%
import requests
from bs4 import BeautifulSoup
import re


#%%
posts_rawlist = requests.get('https://www.splcenter.org/bitcoin-and-alt-right')
soup = BeautifulSoup((posts_rawlist.text), "html5lib")
wallet_addresses = soup.find(class_='field field-name-field-content-items field-type-field-collection field-label-hidden')


#%%
wallet_names = wallet_addresses.find_all('p')

names = []
for i in wallet_names:
    name = str(i).strip('p<>/')
    names.append(name)


#%%
wallet_text = wallet_addresses.text
wallets = wallet_text.split(' 0\n')
url_list = []
for item in wallets:
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', item)
    url_list.append(urls)
del url_list[0]


#%%
hashes = []
for link_list in url_list:
    hash_list = []
    for link in link_list:
        if link.startswith('https://blockchain.info/address/') is True:
            hash_list.append(link.lstrip('https://blockchain.info/address/'))
    hashes.append(hash_list)


#%%
list_zipped = zip(names, hashes)
alt_right_nodes = dict(list_zipped)
with open('data/alt_right_nodes.txt', 'w') as f:
    f.write(str(alt_right_nodes))
