import time


input_string = 'Hello Word!'
letters = 'abcdefghijklmnopqrstuvwxyz'
output_string = ''
abc = 0

for char in input_string:
    if letters.find(char) != -1:
        for letter in letters:
            print(output_string + letter)
            if char == letter:
                output_string = output_string + letter
                break
            time.sleep(0.05)
    else:
        output_string = output_string + char
        print(output_string)
