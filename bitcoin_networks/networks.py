#!/usr/bin/env python3
"""
A library for generating Bitcoin graph data for a given address.
An API key may be required for access.
All bitcoin values are in Satoshi (divide by 100000000 = BTC)
"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""

#%%
from datetime import datetime
import networkx as nx
from blockchain import blockexplorer as bce


#%%
# edges as set, list as metadata
network_dict = {}


#%%
def timestamp_conv(time_stamp):
    time_formatted = datetime.utcfromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    return time_formatted


#%%
def bitcoin_data(address):
    """
    Gather and format the Bitcoin data for a given address
    """
    input_address = bce.get_address(address)
    transactions = input_address.transactions
    for event in transactions:
        print('Transaction hash ' + str(event.hash))
        print('Time ' + str(timestamp_conv(event.time)))
        print('relayed by ' + str(event.relayed_by))
        for i in event.inputs:
            print('from ' + i.address)
            print('value ' + str(i.value))
        for o in event.outputs:
            print('to ' + o.address)
            print('value ' + str(o.value))
        print(' ')

    # metadata in dict > dict to list w/ to from > list to set > set to final edge list



#%%
def bitcoin_network(data):
    """
    Generate the graph of bitcoin transactions
    """
    # select data object(s) with node/edge information
    # create separate node/edge lists if needed
    # create graph of network
    # export options (csv, image, edge/node files)
    pass


#%%
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
