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


#%%
class Bitnodes:

    def bitnodes(url='https://bitnodes.earn.com/api/v1/snapshots/latest/'):
        """
        This function will pull the data from bitnodes api for Bitcoin miners.
        """
        headers = {'Accept': 'application/json; indent=4', }
        bitnodes_data = requests.get(url,
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

    def btc_com_nodes(url, access_key, puid):
        """
        This will pull the node list from btc.com pool
        Requires an account with access_key and puid
        url example 'https://pool.api.btc.com/v1/pool/node-list?access_key=${access_key}&puid=${puid}'
        """
        btc_com_data = requests.get(url)
        return btc_com_data

    def btc_com_pool_stats(url, access_key, puid):
        """
        This will pull the overall mining stats for btc.com pools
        Requires an account with access_key and puid
        url example 'https://pool.api.btc.com/v1/blocks?access_key=${access_key}&puid=${puid}'
        """
        btc_com_data = requests.get(url)
        return btc_com_data

    def btc_com_blocks(url):
        """
        This will scrape the Bitcoin block publication history from btc.com
        """
        btc_com_data = requests.get(url)
        return btc_com_data


class F2Pool:

    def f2pool_stats(url):
        """
        This will pull the stats from f2pool
        Requires an account with an API key
        url example 'http://api.f2pool.com/bitcoin/user'
        """
        f2pool_data = requests.get(url)
        return f2pool_data


class Bitminter:

    bitminter_stats_url = 'https://bitminter.com/api/pool/stats'

    def bitminter_stats(bitminter_stats_url):
        """
        This will pull the stats from bitminter
        pool stats are available through the public api
        """
        url = bitminter_stats_url
        bitminter_data = requests.get(url)
        return bitminter_data


class Slushpool:

    slushpool_stats_url = 'https://slushpool.com/stats/json/btc/'

    def slushpool_stats(slushpool_stats_url, api_key):
        """
        This will pull the stats from slushpool
        pool stats require an API key in the header
        header = {'SlushPool-Auth-Token': '<api key>'}
        """
        url = slushpool_stats_url
        headers = {'SlushPool-Auth-Token': str(api_key)}
        slushpool_data = requests.get(url, headers=headers)
        return slushpool_data


class BitcoinCom:

    bitcoincom_stats_url = ''

    def bitcoin_stats(bitcoincom_stats_url):
        """
        This will pull the stats data from bitcoin.com pool
        """
        url = bitcoincom_stats_url
        bitcoincom_data = requests.get(url)
        return bitcoincom_data


class GrinMint:

    grinmint_stats_url = 'https://api.grinmint.com/v1/poolStats'

    def grinmint_stats(grinmint_stats_url):
        """
        This will pull the stats data from GrinMint pool
        """
        url = grinmint_stats_url
        grinmint_data = requests.get(url)
        return grinmint_data


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


#  Bixin, BitFury, Poolin, btc.top


#%%
'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
