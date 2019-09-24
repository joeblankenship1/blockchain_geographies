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
            "LINKEDIN_CLIENTID=\n",
            "LINKEDIN_CLIENTSECRET=\n",
            "GITHUB_USERNAME=\n",
            "GITHUB_PASSWORD=\n",
            "GITHUB_KEY=\n",
            "TWITTER_USERNAME=\n",
            "TWITTER_PASSWORD=\n",
            "TWITTER_TOKEN=\n",
            "TWITTER_SECRET=\n",
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
    linkedin_id = getenv('LINKEDIN_CLIENTID')
    linkedin_secret = getenv('LINKEDIN_CLIENTSECRET')
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
    This function ...
    """
    pass


def load_opencage_keys():
    """
    This function ...
    """
    pass


def load_bitcoinwhoswho_keys():
    """
    This function ...
    """
    pass


def load_btccom_keys():
    """
    This function ...
    """
    pass


'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''


#%%
