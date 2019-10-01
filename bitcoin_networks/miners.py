#!/usr/bin/env python3
"""
A library for extracting Bitcoin miner information from several APIs.
In many case, API keys will be required for access.

These are the mining pools that are currently accessible:

Bitnodes
BTC.com
F2Pool

"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""


#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup
import credentials


#%%
class Bitnodes:

    def bitnodes(url='https://bitnodes.earn.com/api/v1/snapshots/', date='latest/'):
        """
        This function will pull the data from bitnodes api for Bitcoin miners.
        Date if in unix time, latest for most recent
        Only the past 60 days is available
        """
        headers = {'Accept': 'application/json; indent=4', }
        bitnodes_data = requests.get((url + date),
                                     headers=headers
                                     )
        bitnodes = pd.read_json(bitnodes_data.text)
        node_fields = ['Protocol_version',
                       'User_agent',
                       'Connected_since',
                       'Services',
                       'Height',
                       'Hostname',
                       'City',
                       'Country_code',
                       'LAT',
                       'LON',
                       'Timezone',
                       'ASN',
                       'Organization_name'
                       ]
        bitnodes_nodes = pd.DataFrame(bitnodes.nodes.values.tolist(),
                                      columns=node_fields
                                      )
        bitnodes_nodes['Connected_since'] = pd.to_datetime(bitnodes_nodes['Connected_since'],
                                                           unit='s')
        return bitnodes_nodes


#%%
class BtcCom:

    id, key = credentials.load_btccom_keys()

    def btc_com_nodes(access_key=key, puid=id, url='https://pool.api.btc.com/v1/'):
        """
        This will pull the node list from btc.com pool
        Requires an account with access_key and puid
        url example 'https://pool.api.btc.com/v1/pool/node-list?access_key={access_key}&puid={puid}'
        """
        api_url = f'{url}pool/node-list?access_key={access_key}&puid={puid}'
        btc_com_data = requests.get(api_url)
        btc_com_df = pd.read_json(btc_com_data.text)
        btc_com_df_data = pd.DataFrame(btc_com_df.data.values.tolist())
        return btc_com_df_data

    def btc_com_pool_status(access_key=key, puid=id, url='https://pool.api.btc.com/v1/'):
        """
        This will pull the overall mining stats for btc.com pools
        Requires an account with access_key and puid
        url example 'https://pool.api.btc.com/v1/pool/status?access_key={access_key}&puid={puid}'
        """
        api_url = f'{url}pool/status?access_key={access_key}&puid={puid}'
        btc_com_data = requests.get(api_url)
        btc_com_df = pd.read_json(btc_com_data.text)
        df_drop = btc_com_df.drop(columns=['err_no'])
        df_transpose = df_drop.T
        df_transpose['dtg'] = pd.datetime.utcnow().isoformat()
        df_final = df_transpose.set_index('dtg')
        return df_final

    def btc_com_blocks_stats(access_key=key, puid=id, page='1', page_size='1', url='https://pool.api.btc.com/v1/'):
        """
        This will pull the Bitcoin block publication history from btc.com api
        Requires an account with access_key and puid
        url example 'https://pool.api.btc.com/v1/blocks?access_key={access_key}&puid={puid}&page={page_number}&page_size={max_1000}'
        """
        api_url = f'{url}blocks?access_key={access_key}&puid={puid}&page={page}&page_size={page_size}'
        btc_com_data = requests.get(api_url)
        btc_com_df = pd.read_json(btc_com_data.text)
        btc_com_df_final = btc_com_df.drop(columns=['err_no'])
        return btc_com_df_final.drop(['blocks'])

    def btc_com_blocks_api(access_key=key, puid=id, page_size='1000', url='https://pool.api.btc.com/v1/'):
        """
        This will pull the Bitcoin block publication history from btc.com api
        Requires an account with access_key and puid
        url example 'https://pool.api.btc.com/v1/blocks?access_key={access_key}&puid={puid}&page_size={max_1000}'
        """
        stats = BtcCom.btc_com_blocks_stats()
        page_count = ((int(stats.data[0]))//1000) + 1
        btc_com_blocks_all = pd.DataFrame()
        for i in range(page_count):
            btc_com_data = requests.get(f"{url}blocks?access_key={access_key}&puid={puid}&page={str(i + 1)}&page_size={page_size}")
            btc_com_df = pd.read_json(btc_com_data.text)
            btc_com_df_drop = btc_com_df.drop(columns='err_no')
            btc_com_df_blocks = btc_com_df_drop.loc['blocks']
            btc_com_df_final = pd.DataFrame(btc_com_df_blocks.loc['data'])
            btc_com_blocks_all = btc_com_blocks_all.append(btc_com_df_final)
        return btc_com_blocks_all

    def btc_com_blocks_scrape(url='https://pool.btc.com/pool-stats'):
        """
        This will scrape the Bitcoin block publication history from btc.com pool stats page
        """
        # TODO: Fix timeout issue for url redirect
        block_data_raw = requests.get(url)
        block_data_text = BeautifulSoup((block_data_raw.text), "html.parser")
        block_data_header = block_data_text.find('thead')
        block_data_heads = block_data_header.find_all('th')
        header = []
        for col in block_data_heads:
            cols = col.find_all('a')
            cols = [ele.text.strip() for ele in cols]
            header.append([ele for ele in cols if ele])
        header = [item for sublist in header for item in sublist]
        block_data_body = block_data_text.find('tbody')
        block_data_rows = block_data_body.find_all('tr')
        data = []
        for row in block_data_rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        block_data_final = pd.DataFrame(data, columns=header)
        return block_data_final


#%%
class F2Pool:

    psw = credentials.load_f2pool_keys()

    def f2pool_bitcoin_hashrate(url='http://api.f2pool.com/bitcoin/'):
        """
        This will pull the Bitcoin hashrate from f2pool
        url example 'http://api.f2pool.com/bitcoin/'
        """
        f2pool_data = requests.get(url)
        f2pool_df = pd.read_json(f2pool_data.text, orient='index')
        return f2pool_df

    def f2pool_bitcoin_userstats(user, url='http://api.f2pool.com/bitcoin/'):
        """
        This will pull the Bitcoin user info from f2pool
        url example 'http://api.f2pool.com/bitcoin/user'
        """
        f2pool_data = requests.get(f'{url}{user}')
        f2pool_df = pd.read_json(f2pool_data.text, orient='index')
        return f2pool_df


#%%
class Bitminter:

    bitminter_stats_url = 'https://bitminter.com/api/pool/stats'

    def bitminter_stats(url=bitminter_stats_url):
        """
        This will pull the stats from bitminter
        pool stats are available through the public api
        """
        bitminter_data = requests.get(url)
        bitminter_df = pd.read_json(bitminter_data.text, orient='index')
        bitminter_final = bitminter_df.transpose()
        return bitminter_final


#%%
class Slushpool:

    slushpool_stats_url = 'https://slushpool.com/stats/json/btc/'
    key = credentials.load_slushpool_keys()

    def slushpool_stats(slushpool_stats_url=slushpool_stats_url, api_key=key):
        """
        This will pull the stats from slushpool
        pool stats require an API key in the header
        header = {'SlushPool-Auth-Token': '<api key>'}
        """
        url = slushpool_stats_url
        headers = {'SlushPool-Auth-Token': str(api_key)}
        slushpool_data = requests.get(url, headers=headers)
        slushpool_df = pd.DataFrame(eval(slushpool_data.text))
        slushpool_trans = slushpool_df.transpose()
        slushpool_final = slushpool_trans.drop(columns=['blocks'])
        return slushpool_final


#%%
class BitcoinCom:

    bitcoincom_stats_url = ''

    def bitcoin_stats(bitcoincom_stats_url):
        """
        This will pull the stats data from bitcoin.com pool
        """
        url = bitcoincom_stats_url
        bitcoincom_data = requests.get(url)
        return bitcoincom_data


#%%
class GrinMint:

    grinmint_stats_url = 'https://api.grinmint.com/v1/poolStats'

    def grinmint_stats(grinmint_stats_url):
        """
        This will pull the stats data from GrinMint pool
        """
        url = grinmint_stats_url
        grinmint_data = requests.get(url)
        return grinmint_data


#%%
class ViaBtc:

    viaabtc_stats_url = 'https://pool.viabtc.com/'

    def viabtc_stats(viaabtc_stats_url):
        """
        This will pull the stats data from ViaBTC pool
        this is pulled from html on the page - not an API
        """
        url = viaabtc_stats_url
        viabtc_data = requests.get(url)
        return viabtc_data


#%%
class AntPool:

    antpool_stats_url = ''

    def antpool_stats(antpool_stats_url):
        """
        This will pull the stats data from AntPool
        Requires an API key to access
        """
        url = antpool_stats_url
        antpool_data = requests.get(url)
        return antpool_data


#%%
'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
