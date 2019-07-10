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
def bitnodes():
    url = 'https://bitnodes.earn.com/api/v1/snapshots/latest/'
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
    bitnodes_nodes.to_csv('bitnodes.csv', encoding='utf-8')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
