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
