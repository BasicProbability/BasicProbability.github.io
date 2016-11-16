# stores a mapping from characters to code symbols
encoding_map = dict()
# stores a mapping from code words to characters
decoding_map = dict()
avg_code_length = 0

def construct_code(path):
    '''Construct a code from the empirical distribution found in a text file.

    :param path: The path to the text file
    '''

    # the keyword global allows you to manipulate variables that were defined outside this function
    global total
    global avg_code_length
    global avg_code_length

    pass

def encode(some_string):
    '''Encode a string according to a Huffman code.

    :param some_string: The string to encode
    :return: The encoding of the string
    '''

    pass

def decode(some_code):
    '''Decode a Huffman-encoded message.

    :param some_code: The code sequence
    :return: The decoded message
    '''

    pass

construct_code("war_and_peace.txt")
print("Average code word length is {}".format(avg_code_length))
print(encode("Hello World!"))
print(decode("1111011010001001101000010001101001000010111011000111010001000110010100010110110010011010110101010000"
             "10001010111000110100100000111110110000100100010010000111001111110010010000000111111001000110100110010"
             "1000010010010001001001100110011000001100111111110001"))
