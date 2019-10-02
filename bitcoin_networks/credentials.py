#!/usr/bin/env python3
"""
A library for loading access key information into your virtual environment.
"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""

#%%
from dotenv import load_dotenv, find_dotenv
from os import path, getenv
load_dotenv(find_dotenv('.credentials'))


#%%
def generate_env_file():
    """
    This function generates a .credentials file.
    """
    if path.exists('.credentials') is True:
        print("File already exists.")
        exit
    else:
        env_vars = [
            "LINKEDIN_USERNAME=\n",
            "LINKEDIN_PASSWORD=\n",
            "LINKEDIN_CLIID=\n",
            "LINKEDIN_CLISECRET=\n",
            "GITHUB_USERNAME=\n",
            "GITHUB_PASSWORD=\n",
            "GITHUB_KEY=\n",
            "TWITTER_USERNAME=\n",
            "TWITTER_PASSWORD=\n",
            "TWITTER_CONKEY=\n",
            "TWITTER_CONSECRET=\n",
            "TWITTER_ACCKEY=\n",
            "TWITTER_ACCSECRET=\n",
            "OPENCAGE_KEY=\n",
            "BLOCKCHAIN_KEY=\n",
            "BITCOINWHOSWHO_KEY=\n",
            "BTCCOM_ID=\n",
            "BTCCOM_KEY=\n",
            "F2POOL_PASSWORD=\n",
            "SLUSHPOOL_KEY=\n",
            "ANTPOOL_ID=\n",
            "ANTPOOL_KEY=\n",
            "ANTPOOL_SECRET=\n",
            "BITCOINCOM_KEY=\n"
        ]
        with open('.credentials', 'a+') as env_file:
            env_file.writelines(env_vars)


#%%
def load_linkedin_keys():
    """
    Function loads Linkedin keys as environment variables from .credentials
    """
    linkedin_name = getenv('LINKEDIN_USERNAME')
    linkedin_password = getenv('LINKEDIN_PASSWORD')
    linkedin_id = getenv('LINKEDIN_CLIID')
    linkedin_secret = getenv('LINKEDIN_CLISECRET')
    return linkedin_name, linkedin_password, linkedin_id, linkedin_secret


def load_github_keys():
    """
    Function loads GitHub keys as environment variables from .credentials
    """
    github_name = getenv('GITHUB_USERNAME')
    github_password = getenv('GITHUB_PASSWORD')
    github_key = getenv('GITHUB_KEY')
    return github_name, github_password, github_key


def load_twitter_keys():
    """
    Function loads Twitter keys as environment variables from .credentials
    """
    twitter_name = getenv('TWITTER_USERNAME')
    twitter_password = getenv('TWITTER_PASSWORD')
    twitter_conkey = getenv('TWITTER_CONKEY')
    twitter_consecret = getenv('TWITTER_CONSECRET')
    twitter_acckey = getenv('TWITTER_ACCKEY')
    twitter_accsecret = getenv('TWITTER_ACCSECRET')
    return twitter_name, twitter_password, twitter_conkey, twitter_consecret, twitter_acckey, twitter_accsecret


def load_opencage_keys():
    """
    Function loads OpenCage keys as environment variables from .credentials
    """
    opencage_key = getenv('OPENCAGE_KEY')
    return opencage_key


def load_blockchain_keys():
    """
    Function loads Blockchain.com keys as environment variables from .credentials
    """
    blockchain_key = getenv('BLOCKCHAIN_KEY')
    return blockchain_key


def load_bitcoinwhoswho_keys():
    """
    Function loads BitcoinWhosWho keys as environment variables from .credentials
    """
    bitcoinwhoswho_key = getenv('BITCOINWHOSWHO_KEY')
    return bitcoinwhoswho_key


def load_btccom_keys():
    """
    Function loads BTC.com keys as environment variables from .credentials
    """
    btccom_id = getenv('BTCCOM_ID')
    btccom_key = getenv('BTCCOM_KEY')
    return btccom_id, btccom_key


def load_f2pool_keys():
    """
    Function loads F2Pool keys as environment variables from .credentials
    """
    f2pool_password = getenv('F2POOL_PASSWORD')
    return f2pool_password


def load_slushpool_keys():
    """
    Function loads SlushPool keys as environment variables from .credentials
    """
    slushpool_key = getenv('SLUSHPOOL_KEY')
    return slushpool_key


def load_antpool_keys():
    """
    Function loads AntPool keys as environment variables from .credentials
    """
    antpool_id = getenv('ANTPOOL_ID')
    antpool_key = getenv('ANTPOOL_KEY')
    antpool_secret = getenv('ANTPOOL_SECRET')
    return antpool_id, antpool_key, antpool_secret


def load_bitcoincom_keys():
    """
    Function loads Bitcoin.com keys as environment variables from .credentials
    """
    bitcoincom_key = getenv('BITCOINCOM_KEY')
    bitcoincom_username = getenv('BITCOINCOM_USERNAME')
    bitcoincom_password = getenv('BITCOINCOM_PSW')
    return bitcoincom_key, bitcoincom_username, bitcoincom_password


#%%
'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
