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
    Output schema:
        input address, output address
        input value
        output value
        transaction hash
        transaction time
        transaction relay
    """
    transaction_pairs = []
    input_address = bce.get_address(address)
    transactions = input_address.transactions
    for event in transactions:
        for i in event.inputs:
            for o in event.outputs:
                transaction_pairs.append([i.address,
                                          o.address,
                                          i.value,
                                          o.value,
                                          event.hash,
                                          timestamp_conv(event.time),
                                          event.relayed_by])
    return transaction_pairs

# metadata in dict > dict to list w/ to from > list to set > set to final edge list
# single function for structuring edges from a single transaction event
# use this to populate edge list for a given address
# iterate over collection of addresses via node list


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

'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
