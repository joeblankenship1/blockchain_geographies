#!/usr/bin/env python3
"""
A library for extracting bitcoin and blockchain developer information.
In many case, API keys will be required for access.
"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""


from linkedin_v2 import linkedin

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY,
                                                          CONSUMER_SECRET, 
                                                          USER_TOKEN,
                                                          USER_SECRET, 
                                                          RETURN_URL,
                                                          linkedin.PERMISSIONS.enums.values()
                                                          )

application = linkedin.LinkedInApplication(authentication)


def user_data():
    """function for user data"""
    pass


def blockchain_people():
    """search function for finding blockchain-based people"""
    pass


def blockchain_orgs():
    """function for blockchain organizations"""
    pass


'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
