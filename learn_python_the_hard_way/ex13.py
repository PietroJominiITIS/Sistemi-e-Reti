from sys import argv

# Python argv to be a list of length 4, so that it can be unpacked
# into four variables. Sp, if argv is a list of a different length than
# 4, it go haywire
script, first, second, third = argv

# So, if we wont to stick to sys.argv & to the precedent way of 'unpaking',
# while changing the number of arguments, we have to hardcode a different 
# 'unpack', like:
# file_name, first, second = argv                   # 2 arguments
# file_name, first, second, third, fourth = argv    # 4 arguments

print('The script is called: ', script)
print('Your first variable is: ', first)
print('Your second variable is: ', second)
print('Your third variable is: ', third)

# And finally, some users input, prêt à porter:
print('Votre apport est: ' + input('insert an input \'Français\': '))