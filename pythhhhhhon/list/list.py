
def uno(lista = []):
    """ Scrivere un programma che reimpia una lista arbitraria chiedendo i valori degli elementi all'utente """
    try:
        inp = int(input("Inserisci un numero: [NaN per uscire] "))
        lista.append(inp)
        return uno(lista = lista)
    except ValueError:
        return lista

def due():
    """ Inserire una lista di stirnghe, poi un numero e stampare quelle più lunghe di quel numero  """
    lista = []
    for i in range(0, int(input("Inserire il rage: "))):
        lista.append(input("Inserire la string di indice {}: ".format(i)))
    maxl = int(input("Inserire la lunghezza minima: "))
    lista = [stringa for stringa in lista if len(stringa) >= maxl]
    return lista
    
def tre(a = [], b = []):
    """ Date due liste scelte dall'utente, calcolare l'intersezione """
    return [el for el in a if el in b]
    
def tref(a = [], b = []):
    """ Date due liste scelte dall'utente, calcolare l'intersezione """
    return list(filter(lambda x: x in b, a))
    
def main():
    # print(uno())
    # print(due())
    print(tref([3, 4], [2, 3]))

if __name__ == '__main__':
    main()
