import string
import time

output_string = ''

def print_wait(letter, char):
    global output_string
    print(output_string + letter)
    time.sleep(0.05)
    if letter == char:
        output_string += char

input_string = 'Hello World!'
list(map(lambda char:list(map(lambda i: print_wait(i, char), "".join(sorted(set(string.ascii_lowercase+char))).split(char)[0]+char)),input_string))