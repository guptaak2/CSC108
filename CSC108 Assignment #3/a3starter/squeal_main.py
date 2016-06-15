"""
Process queries from the keyboard and output the results.
"""

import reading
import squeal


def main():
    """ () -> NoneType

    Ask for queries from the keyboard; stop when an empty line is received.
    For each query, process it and use print_csv to print the results.
    
    """
    message = input('Please enter your query:\n')
    where = which_where(message)
    select = select_message(message)
    squeal.print_csv(select)
    
    while message != '':    
        message = input('Please enter your query:\n')
        if query != '':
            where = which_where(message)
            select = select_message(message)
            squeal.print_csv(select)
        else:
            pass

