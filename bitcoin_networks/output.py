#!/usr/bin/env python3
"""
A library for delivery information in discrete formats.
"""


def to_csv(table, output_name):
    """
    This function saves data as a CSV file.
    """
    table.to_csv(str(output_name), index=False)


__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""


'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
