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
def main():
    pass


#%%
def bitcoin_data(address):
    """
    Gather and format the Bitcoin data for a given address
    """
    # get_address for an input hash
    # transaction from address object (output is list)
    # for i in transactions[i]:
    #     for i in .inputs: print i.address # returns input hashes for transaction
    #     for i in .outputs: print i.address # returns output hashes for transaction
    # push to dataframe (datetime, from, to, block id, name)
    # dataframe to csv
    pass


#%%
def bitcoin_network(data):
    """
    Generate the graph of bitcoin transactions
    """
    pass


#%%
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
