import time


input_string = 'Hello World!'
letters = 'abcdefghijklmnopqrstuvwxyz'
output_string = ''

for char in input_string:
    if letters.find(char) != -1:
        iterator = iter(letters[:letters.find(char)])
        output_string = output_string + char
        for letter in iterator:
            print(output_string + letter)
            time.sleep(0.04)
    else:
        output_string = output_string + char
        print(output_string)
