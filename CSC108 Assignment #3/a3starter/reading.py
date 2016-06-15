# Functions for reading tables and databases

import glob

# a table is a dict of {str:list of str}.
# The keys are column names and the values are the values
# in the column, from top row to bottom row.

# A database is a dict of {str:table},
# where the keys are table names and values are the tables.

# use glob.glob('*.csv') to return a list of csv filenames

# Write the read_table and read_database functions below

def read_table (file):
    ''' (str) -> table {str: list of str}
    Return a table with contents from a text file.
    '''
    # initialize variable(s)
    d = {}

    # input the file contents
    input_file = open(file)
    lines = input_file.readlines()
    input_file.close()

    #strip the '/n' character & split the elements
    for i in range (len(lines)): 
        lines[i] = (lines[i].strip()).split(',')

   #table title is the first element of lines
    table_title = lines.pop(0) 

    #appends the list of elements to the key in d
    for k in range(len(lines[0])): 
        lst = []
        for l in range(len(lines)):
            lst.append(lines[l][k])
            d[table_title[k]] = lst
            
    return d

def read_database():
    '''()->database
    Return a database with all tables in the current directory.
    '''
    # initialize variable(s)
    database = {}

    # gets the list of .csv files in the directory
    lst_titles = glob.glob('*.csv')

    # appends the tables to a database
    i = 0
    while i < len(lst_titles): 
        table = read_table(lst_titles[i])
        table_title = lst_titles[i].strip('.csv')
        database[table_title] = table
        i += 1
    return database


    
        

            

        




   
        


  
   
   
   
