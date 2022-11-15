import time


input_string = 'Hello World!'
letters = 'abcdefghijklmnopqrstuvwxyz'
output_string = ''

for char in input_string:
    if letters.find(char) != -1:
        iterator = letters[:letters.find(char)+1]
        for letter in iterator:
            print(output_string + letter)
            time.sleep(0.04)
        output_string += char
    else:
        output_string += char
        print(output_string)