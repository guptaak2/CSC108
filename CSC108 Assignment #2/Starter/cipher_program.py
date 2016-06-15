"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'secret1.txt'
MODE = 'd'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    # gets the deck from cipher_functions.read_deck
    deck = cipher_functions.read_deck (DECK_FILENAME)
    # gets the messages from cipher_functions.read_messages
    messages = cipher_functions.read_messages (MSG_FILENAME)
    # prints the encrypted/decrypted message
    print (cipher_functions.process_messages (deck, messages, MODE))
    

