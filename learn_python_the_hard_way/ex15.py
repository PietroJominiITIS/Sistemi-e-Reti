# The line under this comment is actually another line of comment.
# Really, keeping column-index small and still comment every line
# just in the line above isn't really easy... Well, let's try it out:
# "Importing argv from sys"
# hum, it wasn't a good one, i can do better... Let's see:
# "Telling to python interpreter to load some data from a module"
# hum... better, but really too much generic...
# "Including in our script command line arguments, from sys module"
# Looks better... Oh s**t, it isn't over the line which it comments, let's fix it:
# "Including in our script command line arguments, from sys module"
from sys import argv        # Ahh, perfection

# Now, let's be shorter...
# Unpacking some "notthatmuchusefulatthemoment" stuff and the filename we need from console arguments
_, filename = argv          # Here i went past 100 column...Whatever, none saw anything

# Tellling python that we need to accede the data located at a certain position in the disk,
txt = open(filename)        # but since we are in the hight level stuff, we just tell him
# the filename, and our beloved snake will do the dirty work and query the file system for 
# a memory adress, or some other low-level stuff like so. Important thing, we now have a file object
# from which we can read data (\0w0/)

# Standard output, with a formatted string
print(f'Here\'s your file {filename}:')
print(txt.read())   # And here we tell to python to go to the memory, at the adress
# previously found by the `open` function, and start reading data from there.

# Some console interaction
print('Type the filename again:')
file_again = input('> ')
# to input a new filename, in a nice console like formating

# Same stuff as above, 
txt_again = open(file_again)    # Strem init
print(txt_again.read())         # FS Q&A for the data
                                # and, of course, a nice console output

# Closing ours file objects
txt.close()
txt_again.cloes()