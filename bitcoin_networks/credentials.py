#!/usr/bin/env python3
"""
A library for loading access key information into your virtual environment.
"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""

#%%
from dotenv import load_dotenv
from os import path, getenv
load_dotenv()


#%%
def generate_env_file():
    if path.exists('.env') is True:
        print("File already exists.")
        exit
    else:
        env_vars = [
            "LINKEDIN_NAME=\n",
            "LINKEDIN_SECRET=\n",
            "LINKEDIN_API=\n"
        ]
        with open('.env', 'a+') as env_file:
            env_file.writelines(env_vars)


#%%
def load_linkedin_keys():
    """
    Function loads Linkedin keys as environment variables from .env
    To load key values into .env, edit the file manually.
    """
    linkedin_name = getenv('LINKEDIN_NAME')
    linkedin_secret = getenv('LINKEDIN_SECRET')
    linkedin_api = getenv('LINKEDIN_API')
    return linkedin_name, linkedin_secret, linkedin_api


def load_github_keys():
    pass


def load_opencage_keys():
    pass


def load_bitcoinwhoswho_keys():
    pass


def load_btccom_keys():
    pass


'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
