from sys import argv
from os.path import exists

# _, source, dest = argv

# in_file = open(source)
# indata = in_file.read()

# if exists(dest):
#     print('{dest} alreasy exists, delete it? [^C / ENTER]')
#     input()
    
# out_file = open(dest, 'w')
# out_file.write(indata)

# out_file.close
# in_file.close

# One line version : -->> (OwO)

open(argv[2]).write(open(argv[1]).read())