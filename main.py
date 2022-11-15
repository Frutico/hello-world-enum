import string
import time


def print_wait(output_string, letter):
    print(output_string + letter)
    time.sleep(0.05)


input_string = 'Hello World!'
letters = string.ascii_lowercase
output_string = ''

for char in input_string:
#    iterator = [x for x in sorted(set(letters+char)) if x <= char]
#    iterator = "".join(sorted(set(letters+char))).split(char)[0]+char
    iterator = (letters.split(char)[0] if len(letters.split(char)) > 1 else "") + char
    list(map(lambda i: print_wait(output_string, i), iterator))
    output_string += char