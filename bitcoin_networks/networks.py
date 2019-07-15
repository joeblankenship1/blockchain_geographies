#!/usr/bin/env python3
"""
A library for generating Bitcoin graph data for a given address.
An API key may be required for access.
"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""

#%%
import pandas as pd
import networkx as nx
from blockchain import blockexplorer as bce


#%%
network_dict = {}


#%%
def main():
    pass


#%%
def bitcoin_data(address):
    """
    Gather and format the Bitcoin data for a given address
    """
    input_address = bce.get_address(address)
    transactions = input_address.transactions
    event_counter = 1
    for event in transactions:
        print('Transaction ' + str(event_counter))
        for i in event.inputs:
            print('from ' + i.address)
        for o in event.outputs:
            print('to ' + o.address)
        event_counter += 1

    # push to dataframe (datetime, from, to, block id, name)
    # dataframe to csv


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
