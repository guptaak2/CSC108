from reading import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *No main function. No user input. No print.

# helper function for outputting tables
# call this from squeal_main.py, not here!

def print_csv(table):
    '''(table) -> NoneType
    Print a representation of table.
    '''
    columns = list(table.keys())
    print(','.join(columns))
    for i in range(len(table[columns[0]])):
        cur_column = []
        for column in columns:
            cur_column.append(table[column][i])
        print(','.join(cur_column))

def cartesian_product(dict_one, dict_two):
    '''(table, table) -> table
    Return the cartesian product of dict_one and dict_two.
    '''
    # initialize variable(s)
    new_table = {}
    new_dict = {}
    table_title = []

    # get list of keys and values
    values_one = list(dict_one.values())
    values_two = list(dict_two.values())
    keys_one = list(dict_one.keys())
    keys_two = list(dict_two.keys())

    # create the header of the table
    table_title.append(keys_one + keys_two)
    for element in table_title:
        table_title = element

    # performs the cartesian product of dict_two
    for m in range(len(dict_two)):
        lst = []
        lst.append(values_two[m] * len(dict_two))
        combined = [item for sublist in lst for item in sublist]
        new_dict[keys_two[m]] = combined

    # performs the cartesian product of dict_one
    for k in range (len(dict_one)):
        lst = []
        for l in range (len(values_one[0])):
            lst.append([values_one[k][l]] * len(dict_one))
            combined = [item for sublist in lst for item in sublist]
        new_table[keys_one[k]] = combined
    new_table.update(new_dict)  #puts the products together
    
    return new_table

def split_message(message):
    '''(str) -> list of str
    Return the list of each word in message.
    >>> split_message('select * from movies')
    ['select', '*', 'from', 'movies']
    '''
    # initialize variable(s)
    new_message = []

    # split the inputed message
    new_message = message.split()
    lst_message = []

    # strip the commas from new_message
    for element in new_message:
        element = element.strip(',')
        lst_message.append(element)

    return lst_message

def cartesian_products(lst):
    ''' (lst of str) -> dict
    Return the cartesian product of two or more tables.
    '''
    # initalize variable(s)
    table = []

    # appends .csv to every element
    for element in lst:
        element += '.csv'
        table.append(read_table(element))

    # performs the cartesian product
    base_table = table[0]
    for i in range (1, len(table)):
       base_table = cartesian_product(base_table, table[i])

    return base_table

def select_message(message):
    '''(str) -> table
    Return the cartesian product of the inputed files.
    >>> select_message('select m.title from movies')
    {'m.title': ['Titanic', 'The Lord of the Rings: The Return of the King', \
    'Toy Story 3']}
    '''
    # initialize variable(s)
    lst_select = []
    new_table = {}

    # split the inputed message
    lst_message = split_message(message)

    # get the indices of 'select' and 'from'
    index_select = lst_message.index('select')
    index_from = lst_message.index('from')
    lst_select = lst_message[index_select+1:index_from]

    # gets the list of files from the inputed message
    lst_files = files(message)

    # if everything is to be selected
    if lst_select == ['*']:
        return cartesian_products(lst_files)

    # perfoms the cartesian product and chooses the columns required
    table = cartesian_products(lst_files)
    keys = list(table.keys())
    for k in range(len(keys)):
        for l in range(len(lst_select)):
            if keys[k] == lst_select[l]:
                new_table[keys[k]] = table[keys[k]]
    return new_table

def files(message):
    '''(str) -> lst
    Return the files needed to compute the cartesian product(s)
    >>> files('select o.title from oscars')
    ['oscars']
    '''
    # initialize variable(s)
    lst_files = []

    # split the inputed message
    lst_message = split_message(message)

    # get the indice of 'from' 
    index_from = lst_message.index('from')

    # checks if 'where' is in message
    if "where" in lst_message:
        index_where = lst_message.index('where')
        lst_files = lst_message[index_from+1:index_where]
    else:
        lst_files =  lst_message[index_from+1:]

    return lst_files
    
def where_column_equals_column(message):
    '''(str) -> table
    Return a table with the required where conditions.
    >>> where_column_equals_column('select m.title, o.title from movies, \
    oscars where m.title=o.title')
    'm.gross': ['2186.8', '2186.8', '1119.9', '1063.2'], 'o.category': \
    ['Directing', 'Best Picture', 'Directing', 'Animated Feature Film'], \
    'm.year': ['1997', '1997', '2003', '2010'], 'm.studio': \
    ['Par.', 'Par.', 'NL', 'BV'], 'o.title': ['Titanic', 'Titanic', \
    'The Lord of the Rings: The Return of the King', 'Toy Story 3'], \
    'o.year': ['1997', '1997', '2003', '2010'], 'm.title': \
    ['Titanic', 'Titanic', 'The Lord of the Rings: The Return of the King', \
    'Toy Story 3']}
    '''
    # initialize variable(s)
    indices = []
    lst = []
    new_lst = []
    query_lst = []
    new_table = {}

    # get the index of 'where'
    index_where = message.find('where')

    # get the query from message and split the commas
    query = message[index_where+6:]
    query_lst = query.split(',')

    # get the files and perform cartesian product(s) on them
    lst_files = files(message)
    table = cartesian_products(lst_files)

    # checks if "=" is present and if column_name is given
    for i in range(len(query_lst)):
         if query.find('=') != -1:          
            lst = query.split('=')
            if lst[1].find("'") == -1:           
                column_name_1= table[lst[0]]
                column_name_2 = table[lst[1]]

            # gets the indices where the columns are equal
            for i in range(len(column_name_1)):
                 if column_name_1[i] == column_name_2[i]:
                       indices.append(i)

            # appends the columns at equal indices
            for keys in table:
                 column = []
                 for i in range(len(table[keys])):
                    if i in indices:
                        column.append(table[keys][i])
                    new_table[keys] = column

    return new_table

def where_column_equals_value(message):
    '''(str) -> table
    Return a table with the required where conditions.
    >>> where_column_greater_value ("select m.title, o.title from movies, \
    oscars where m.title>'Titanic'")
    {'m.studio': ['BV', 'BV', 'BV', 'BV'], 'm.title': ['Toy Story 3',\
    'Toy Story 3', 'Toy Story 3', 'Toy Story 3'], 'o.title':\
    ['Toy Story 3', 'The Lord of the Rings: The Return of the King',\
    'Titanic', 'Titanic'], 'o.year': ['2010', '2003', '1997', '1997'], \
    'm.year': ['2010', '2010', '2010', '2010'], 'o.category':\
    ['Animated Feature Film', 'Directing', 'Directing', 'Best Picture'], \
    'm.gross': ['1063.2', '1063.2', '1063.2', '1063.2']}
    '''
    # initialize variable(s)
    indices = []
    lst = []
    new_lst = []
    query_lst = []
    new_table = {}

    # get the index of 'where'
    index_where = message.find('where')

    # get the query from message and split the commas
    query = message[index_where+6:]
    query_lst = query.split(',')

    # get the files and perform cartesian product(s) on them
    lst_files = files(message)
    table = cartesian_products(lst_files)

    # checks if "=" is present and if value is given    
    for i in range(len(query_lst)):
         if query.find('=') != -1:              
            lst = query.split('=')
            if lst[1].find("'") != -1:             
                    column_name = table[lst[0]]
                    value = lst[1]
                    value = value.strip("'")

                    # gets the indices where the columns and values are equal
                    for i in range(len(column_name)):
                        if column_name[i] == value:
                               indices.append(i)
                            
                    # appends the columns and values at equal indices       
                    for keys in table:
                            column = []
                            for i in range(len(table[keys])):
                                   if i in indices:
                                       column.append(table[keys][i])
                            new_table[keys] = column

    return new_table

def where_column_greater_column(message):
    '''(str) -> table
    Return a table with the required where conditions.
    >>> where_column_greater_column ('select m.title, o,title from movies,\
    oscars where m.title>o.title')
    {'m.studio': ['Par.', 'BV', 'BV', 'BV'], 'm.title': ['Titanic',\
    'Toy Story 3', 'Toy Story 3', 'Toy Story 3'], 'o.title': \
    ['The Lord of the Rings: The Return of the King', 'The Lord of the Rings:\
    The Return of the King', 'Titanic', 'Titanic'], 'o.year': \
    ['2003', '2003', '1997', '1997'], 'm.year': ['1997', '2010', '2010',\
    '2010'], 'o.category': ['Directing', 'Directing', 'Directing', \
    'Best Picture'], 'm.gross': ['2186.8', '1063.2', '1063.2', '1063.2']}
    '''
    # initialize variable(s)
    indices = []
    lst = []
    new_lst = []
    query_lst = []
    new_table = {}

    # get the index of 'where'
    index_where = message.find('where')

    # get the query from message and split the commas
    query = message[index_where+6:]
    query_lst = query.split(',')

    # get the files and perform cartesian product(s) on them 
    lst_files = files(message)
    table = cartesian_products(lst_files)

    # checks if "=" is present and if column_name is given
    for i in range(len(query_lst)):
         if query.find('>') != -1:                
            lst = query.split('>')
            if lst[1].find("'") == -1:              
                column_name_1 = table[lst[0]]
                column_name_2 = table[lst[1]]

            # gets the indices where the column_1 is greater than column_2
            for i in range(len(column_name_1)):
                 if column_name_1[i] > column_name_2[i]:
                       indices.append(i)
                       
            # appends the columns at greater indices 
            for keys in table:
                 column = []
                 for i in range(len(table[keys])):
                    if i in indices:
                        column.append(table[keys][i])
                 new_table[keys] = column

    return new_table

def where_column_greater_value(message):
    '''(str) -> table
    Return a table with the required where conditions.
    >>> where_column_greater_value ("select m.title, o.title from movies,\
    oscars where m.title>'Titanic'")
    {'m.studio': ['BV', 'BV', 'BV', 'BV'], 'm.title': ['Toy Story 3', \
    'Toy Story 3', 'Toy Story 3', 'Toy Story 3'], 'o.title': ['Toy Story 3',\
    'The Lord of the Rings: The Return of the King', 'Titanic', 'Titanic'],\
    'o.year': ['2010', '2003', '1997', '1997'], 'm.year': ['2010', '2010', \
    '2010', '2010'], 'o.category': ['Animated Feature Film', 'Directing',\
    'Directing', 'Best Picture'], 'm.gross': ['1063.2', '1063.2', \
    '1063.2', '1063.2']}
    '''
    # initialize variable(s)
    indices = []
    lst = []
    new_lst = []
    query_lst = []
    new_table = {}

    # get the index of 'where'
    index_where = message.find('where')

    # get the query from message and split the commas 
    query = message[index_where+6:]
    query_lst = query.split(',')

    # get the files and perform cartesian product(s) on them
    lst_files = files(message)
    table = cartesian_products(lst_files)

    # checks if "=" is present and if value is given
    for i in range(len(query_lst)):
        if query.find('>') != -1:                
           lst = query.split('>')
           if lst[1].find("'") != -1:              
               column_name = lst[0]
               value = lst[1]
               value = value.strip("'")
               new_lst = table[column_name]

                # gets the indices where the column is greater than value
               for i in range(len(new_lst)):
                    if new_lst[i] > value:
                            indices.append(i)

                # appends the columns where columns is greater than value
               for keys in table:
                        column = []
                        for i in range(len(table[keys])):
                            if i in indices:
                               column.append(table[keys][i])
                        new_table[keys] = column
    return new_table

def which_where(message):
    '''(str) -> table
    Return the output of which where clause to be used.
    '''
    # initialize variable(s)
    lst = []
    query_lst = []
    answer = {}

    # get the index of 'where'
    index_where = message.find('where')

    # get the query from message and split the commas 
    query = message[index_where+6:]
    query_lst = query.split(',')

    for i in range(len(query_lst)):
        if query.find('>') != -1:                
           lst = query.split('>')
           if lst[1].find("'") != -1:
               answer = where_column_greater_value(message)
               
        elif query.find('>') != -1:                
            lst = query.split('>')
            if lst[1].find("'") == -1:
                answer = where_column_greater_column(message)
                
        elif query.find('=') != -1:              
            lst = query.split('=')
            if lst[1].find("'") != -1:
                answer = where_column_equals_value(message)
                
        elif query.find('=') != -1:          
            lst = query.split('=')
            if lst[1].find("'") == -1:
                answer = where_column_equals_column(message)
        
    return answer








    
    

    

    
            
            


