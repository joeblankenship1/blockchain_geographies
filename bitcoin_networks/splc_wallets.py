#!/usr/bin/env python3
"""
A library for generating node data for SPLC alt-right Bitcoin data.
"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""


import requests
from bs4 import BeautifulSoup
import re


def get_node_data():
    """
    This goes out to SPLC to grab alt-right Bitcoin addresses
    """
    # BeautifulSoup to grab SPLC website data
    posts_rawlist = requests.get('https://www.splcenter.org/bitcoin-and-alt-right')
    soup = BeautifulSoup((posts_rawlist.text), "html5lib")
    wallet_addresses = soup.find(class_='field field-name-field-content-items field-type-field-collection field-label-hidden')
    # extract all names attached to Bitcoin wallet list
    wallet_names = wallet_addresses.find_all('p')
    names = []
    for i in wallet_names:
        name = str(i).strip('p<>/')
        names.append(name)
    # I would do the same thing for 'a' elements, but the page wouldn't allow it. So...
    # extract page text, run a regex for urls, create a list of urls per entity on page
    wallet_text = wallet_addresses.text
    wallets = wallet_text.split(' 0\n')
    url_list = []
    for item in wallets:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', item)
        url_list.append(urls)
    del url_list[0]
    # extract hashes from urls
    hashes = []
    for link_list in url_list:
        hash_list = []
        for link in link_list:
            if link.startswith('https://blockchain.info/address/') is True:
                hash_list.append(link.lstrip('https://blockchain.info/address/'))
        hashes.append(hash_list)
    # create dictionary with names and hashes
    list_zipped = zip(names, hashes)
    alt_right_nodes = dict(list_zipped)
    # return dictionary
    return alt_right_nodes


def node_data_to_file():
    """
    Creates an external txt file for backup
    """
    with open('data/alt_right_nodes.txt', 'w') as f:
        f.write(str(get_node_data()))
