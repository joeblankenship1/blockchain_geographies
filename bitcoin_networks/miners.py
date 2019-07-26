#!/usr/bin/env python3
"""
A library for extracting Bitcoin miner information from several APIs.
In many case, API keys will be required for access.
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
        bitnodes_nodes.to_csv('data/bitnodes.csv', encoding='utf-8')


#%%
class BtcCom:

    def btc_com_nodes(url):
        """
        This will pull the node list from btc.com pool
        Requires an account with access_key and puid
        url example 'https://pool.api.btc.com/v1/pool/node-list?access_key=${access_key}&puid=${puid}'
        """
        btc_com_data = requests.get(url)
        return btc_com_data

    def btc_com_pool_stats(url):
        """
        This will pull the overall mining stats for btc.com pools
        Requires an account with access_key and puid
        url example 'https://pool.api.btc.com/v1/blocks?access_key=${access_key}&puid=${puid}'
        """
        btc_com_data = requests.get(url)
        return btc_com_data


#%%
'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
