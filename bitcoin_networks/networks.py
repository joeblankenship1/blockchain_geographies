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
from splc_wallets import get_node_data


#%%
def timestamp_conv(time_stamp):
    time_formatted = datetime.utcfromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    return time_formatted


#%%
def bitcoin_data(address):
    """
    Gather and format the Bitcoin data for a given address
    Output schema as Tuple:
        input address,
        output address,
        {
        input value
        output value
        transaction hash
        transaction time
        transaction relay
        }
    """
    transaction_pairs = []
    input_address = bce.get_address(address)
    transactions = input_address.transactions
    for event in transactions:
        for i in event.inputs:
            for o in event.outputs:
                transaction_pairs.append(tuple([i.address,
                                                o.address,
                                                {
                                                 'input_value': i.value,
                                                 'output_value': o.value,
                                                 'hash': event.hash,
                                                 'time': timestamp_conv(event.time),
                                                 'relay': event.relayed_by
                                                 }
                                                ]))
    return transaction_pairs


#%%
def bitcoin_nodes_splc():
    """
    Gather and structure bitcoin address information
    for SPLC Alt-right wallets
    original url = 'https://www.splcenter.org/bitcoin-and-alt-right'
    """
    node_data = get_node_data()
    return node_data


#%%
def bitcoin_network(node_data):
    """
    Iterate over node addresses
    Download transactions for addresses
    generate edge list for network
    """
    network_data = []
    for i in node_data:
        network_data.append(bitcoin_data(i[0]))
    network_data_combine = []
    for i in network_data:
        for j in i:
            network_data_combine.append(j)
    return network_data_combine


#%%
def bitcoin_graph(node_data, edge_data):
    """
    Generate graph object of bitcoin transactions
    """
    graph_object = nx.DiGraph()
    graph_object.add_nodes_from(node_data)
    graph_object.add_edges_from(edge_data)
    return graph_object


#%%
def bitcoin_data_export(graph_data, type, filename):
    """
    export data in one of these formats:
        edgelist
        graphml
    """
    if type.lower() == 'edgelist':
        nx.write_edgelist(graph_data, f'data/{filename}.edgelist')
    elif type.lower() == 'graphml':
        nx.write_graphml(graph_data, f'data/{filename}.graphml')
    else:
        'Please enter one of the following options: edgelist; graphml.'


#%%
'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
