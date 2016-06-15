# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:

def clean_message (message):
    ''' (str) -> str
    Return a copy of the message that includes only its alphabetical characters
    where each of those characters have been converted to uppercase
    >>> clean_message ('hello, how are you?')
    'HELLOHOWAREYOU'
    '''
    # checks if every char in message is in the alphabet and returns the
    # message in uppercase
    new_message = ''
    for char in message:                            
        if char.isalpha():                    
            new_message = new_message + char  
    return new_message.upper()                

def encrypt_letter (letter, key):
    ''' (str, int) -> str
    Return the result of applying the keystream value to the character for
    encryption.
    >>> encrypt_letter ('k', 2)
    'm'
    '''
    # encrypts the letter by adding the key value
    letter = (ord(letter.upper()) - 65 + key) % 26  
    return chr (letter + 65)                               

def decrypt_letter (letter, key):
    ''' (str, int) -> str
    Return the result of applying the keystream value to the uppercase
    character for decryption.
    >>> decrypt_letter ('C', 2)
    'A'
    '''
    # decrypts the letter by subtracting the key value
    letter = (ord(letter.upper()) - 65 - key) % 26  
    return chr (letter + 65)                              

def swap_cards (deck, index):
    ''' (list of int, int) -> NoneType
    Swap the card at the index with the card that follows it.
    >>> deck = ([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,
    5,8,11,14,17,20,23,26])
    >>> swap_cards (deck, 1)
    >>> deck
    ([1,7,4,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,11,14,17,
    20,23,26])    
    '''
    # special case: treats the deck as circular if index = last card 
    if index == len(deck) - 1:   
        deck[:] = deck[index:] + deck[1:index] + deck[0:1]

    # swaps the card with the one that follows it
    else:                                                                                   
        deck[:] = deck[:index] + deck[index+1:index+2] + \
            deck[index:index+1] + deck[index+2:]  
    
def move_joker_1 (deck):
    ''' (list of int) -> NoneType
    Find JOKER1 and swap it with the card that follows it.
    >>> deck = ([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,
    11,14,17,20,23,26])
    >>> move_joker_1 (deck)
    >>> deck
    ([1,7,4,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,2, 2,5,8,11,14,
    17,20,23,26]) 
    '''
    # swaps joker 1 with the card that follows it
    JOKER1_index = deck.index(JOKER1)
    deck = swap_cards (deck, JOKER1_index)

def move_joker_2 (deck):
    ''' (list of int) -> NoneType
    Find JOKER2 and move it two cards down.
    >>> deck = ([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,
    5,8,11,14,17,20,23,26])
    >>> move_joker_2 (deck)
    >>> deck
    ([1,7,4,10,13,16,19,22,25,3,6,28,9,12,15,18,21,24,27,2,5,8,11,
    14,17,20,23,26]) 
    '''
    JOKER2_index = deck.index(JOKER2)

    # special case: if joker 2 is in the last position of the deck
    if deck[len(deck)-1] == JOKER2:
        deck[:] = deck[1:2] + deck[len(deck)-1:] + deck[2:JOKER2_index] + \
                      deck[0:1]
        
    # special case: if joker 2 is in the 2nd last position of the deck      
    if deck[len(deck)-2] == JOKER2:
        deck[:] = deck[JOKER2_index:JOKER2_index+1] + \
            deck[1:JOKER2_index] + deck[len(deck)-1:] + deck[0:1]
            
    # moves down joker 2 by 2 positions 
    else:
        deck[:] = (deck[:JOKER2_index] + deck[JOKER2_index+1:JOKER2_index+3] +
            deck[JOKER2_index:JOKER2_index+1] + deck[JOKER2_index+3:])

def triple_cut (deck):
    ''' (list of int) -> NoneType
    Find the two jokers and do a triple cut.
    >>> deck = ([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,11,14
    ,17,20,23,26])
    >>> triple_cut (deck)
    >>> deck
    [2,5,8,11,14,17,20,23,26,28,3,6,9,12,15,18,21,24,27,1,4,7,
    10, 13, 16, 19, 22, 25]
    '''
    JOKER1_index = deck.index(JOKER1)
    JOKER2_index = deck.index(JOKER2)

    # if joker 1 comes before joker 2 in the deck
    if JOKER1_index < JOKER2_index:
        deck[:] =  deck[JOKER2_index+1:] + \
            deck[JOKER1_index : JOKER2_index+1] + deck[:JOKER1_index]

    # if joker 2 comes before joker 1 in the deck
    elif JOKER2_index < JOKER1_index:
        deck[:] = deck[JOKER1_index+1:] + deck[JOKER2_index:JOKER1_index+1] +\
            deck[:JOKER2_index]
    
def insert_top_to_bottom(deck):
    ''' (list of int) -> NoneType
    Move as many cards as the value of the bottom card from the top of deck 
    to bottom.
    >>> deck = ([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,
    11,14,17,20,23,26])
    >>> insert_top_to_bottom (deck)
    >>> deck
    [23, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 
    27, 2, 5, 8,
    11, 14, 17, 20, 26]
    '''
    bottom_card = deck[len(deck)-1]

    # special case: if the bottom card is joker 2
    if bottom_card == JOKER2:
        deck[:] = deck[bottom_card:len(deck)-1] + deck[:bottom_card]

    # if bottom card is less than or equal to the value of joker 1
    elif bottom_card <= JOKER1:
        deck[:] = deck[bottom_card:len(deck)-1] +deck[:bottom_card] + \
            deck[len(deck)-1:]

def get_card_at_top_index(deck):
    ''' (list of int) -> int
    Retun the card at the index of the value of the top card.
    >>> get_card_at_top_index([1,2,3,4,5,6])
    2
    ''' 
    top_card = deck[0]

    # special case: if the top card is joker 2
    if top_card == JOKER2:
        top_card = JOKER1

    # finds the card at the index of the value of the top card
    card =  deck[top_card]
    return card

def get_next_value(deck):
    ''' (list of int) -> int
    Return the next potential keystream value
    >>> get_next_value ([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,2
        4,27,2,5,8,11,14,17,20,23,26])
    11
    '''
    # does move joker 1, move joker 2, triple cut, insert top to bottom, and
    # get card at top index
    step_1 = move_joker_1(deck)
    step_2 = move_joker_2(deck)
    step_3 = triple_cut(deck)
    step_4 = insert_top_to_bottom(deck)
    step_5 = get_card_at_top_index(deck)
    return step_5

def get_next_keystream_value(deck):
    ''' (list of int) -> int
    Return the next keystream value in range 1-26.
    11
    '''
    # calls get_next_value to get the next keystream value
    value = get_next_value (deck)
    
    # if value is greater than 26, it calls get_next_value again
    while value > 26:
        value = get_next_value (deck)
    return value


def process_message (deck, message, mode):
    '''(list of int, str, str) -> str
    Return the encrypted or decrypted message
    >>> process_message([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,
        24,27,2,5,8,11,14,17,20,23,26],
    'Lake Hylia', 'e')
    'XIBDIMAVU'
    '''
    # cleans the inputed message
    new_message = ''
    message = clean_message(message)
    
    # if the message is to be encrypted:
    if (mode == 'e'):
        for char in message:
            keystream = get_next_keystream_value (deck)
            letter = encrypt_letter (char, keystream)
            new_message += letter

    # if the message is to be decrypted:
    if (mode == 'd'):
        for char in message:
            keystream = get_next_keystream_value (deck)
            letter = decrypt_letter (char, keystream)
            new_message += letter
            
    return new_message

def process_messages (deck, messages, mode):
    ''' (list of int, list of str, str) -> list of str
    Return the list of encrypted or decrypted messages
    >>> process_messages([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,
        24,27,2,5,8,11,14,17,20,23,26],
    ['Lake Hylia', 'Xibdimavu'], 'e')
    ['XIBDIMAVU', 'LAKEHYLIA']
    '''
    # calculates the length of the inputed message
    new_message = []
    len_messages = len(messages)
    i = 0
    
    # calls process_message to get the encrypted/decrypted message
    while i < len_messages:
        answer = process_message (deck, messages[i], mode)
        new_message.append(answer)
        i += 1
    return new_message

def read_messages (file):
    ''' (file open for reading) -> list of str
    Return the contents of the file as a list of messages
    '''
    # reads the inputed file
    infile = open(file)
    line = infile.readlines()
    lst_lines = []
    
    # strips the newline character from the line
    for i in range(len(line)):
        lst_lines.append (line[i].strip())
    return lst_lines

def read_deck (file):
    ''' (file open for reading) -> list of int
    Return the contents of the file as a list of int
    '''
    # reads the inputed file
    infile = open(file)
    line = infile.readlines()
    lst_lines = []
    deck = []
    
    # strips the newline character from the line
    for i in range(len(line)):
        lst_lines.append (line[i].strip())
        
    # splits the message into strings
    for j in range(len(lst_lines)):
        lst_lines[j] = lst_lines[j].split()

    # converts the strings to integers
    for k in range(len(lst_lines)):
        for l in range(len(lst_lines[k])):
            lst_lines[k][l] = int(lst_lines[k][l])

    # appends the converted integers to a new deck
    for m in range(len(lst_lines)):
        for n in range(len(lst_lines[m])):
            deck.append(lst_lines[m][n])

    infile.close()           
    return deck
    
# END OF PROGRAM




        
    




            
            



          


    

    
        

    
    
    
    
    

    

        
    
        
    



    

    

        
    


    
    
    
    


    










    


    
    














    






    








    
    



    
    
    

        




    
    
    
    
    
    
    






    


    
