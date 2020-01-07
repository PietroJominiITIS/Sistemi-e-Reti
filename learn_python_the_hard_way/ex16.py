from sys import argv

script, filename = argv

print(f'We\'re going to erase {filename}.')
print('If you don\'t want that, hit CTRL_C (^C)')
print('If you do want that, hit RETURN')

input('?')

print('Opening the file...')
target = open(filename, 'w')

# useless
# print('Truncating the file. Goodbye!')
# target.truncate()

print('Now I\'m going to ask you for three lines.')
lines = [input('Line 1: '), input('Line 2: '), input('Line 3: ')]

print('I\'m going to write these to the file')

target.write('\n'.join(lines))

print('And finally, we close it.')
target.close()