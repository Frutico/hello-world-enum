import time


def print_wait(output_string, letter):
    print(output_string + letter)
    time.sleep(0.05)


input_string = 'Hello World!'
letters = string.ascii_lowercase
output_string = ''

for char in input_string:
    if letters.find(char) != -1:
        iterator = letters[:letters.find(char)+1]
        list(map(lambda i: print_wait(output_string, i), iterator))
        output_string += char
    else:
        output_string += char
        print(output_string)