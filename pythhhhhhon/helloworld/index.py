
def hello(to = lambda: 'undefined one'):
    return '{} World'.format(to())
    
@hello
def helloworld():
    return 'World'

print(helloworld)