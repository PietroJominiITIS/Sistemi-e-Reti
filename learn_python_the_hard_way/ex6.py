# formatting a string with an integer
types_of_people = 10
x = f'There are {types_of_people} types of people'

# Formatting a string with two other strings
binary = 'binary'
do_not = 'don\'t'
y = f'Those who know {binary} and those who {do_not}'

# Printing formatted strings to console
print(x)
print(y)

# Formatting two strings with previous strings and printing them to console
print(f'I said: {x}')
print(f'I also said: {y}')

# Formatting a string with a boolean
hilarious = False
joke_evaluation = 'Isn\'t that joke so funny?! {}'

# and printing it to console
print(joke_evaluation.format(hilarious))

# Creating two strings
w = 'This is the left side of ...'
e = ' a string eith a right side.'

# And printing theyrs concatenation to console
print(w + e)

# :-----------------------------------------------------------------:
# There are actually 4 places where we place a string into another string:
#   - line 8 (2x)
#   - line 15
#   - line 16
# In fact, it depends on when we consider the type of the variable which
# we are 'putting in' the 'mother' string.
# To format a complete string, pythone translate every variables in a strin,
# so technically we put a string into another string every time we do a format,
# so, in this test case, 6 times
#
# :-----------------------------------------------------------------:
# string + string = string,
# 'cause string concatenation work this way ¯\_(ツ)_/¯