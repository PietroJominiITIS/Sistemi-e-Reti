import random

class deck:
    def __init__(self):
        self.cards = []
        
    def loadSTD(self, rng = 52, n4s = 13):
        for i in range(0, rng):
            self.cards.append((i % n4s + 1, 'Cuori' if int(i / n4s) == 0 else 'Picche' if int(i / n4s) == 1 else 'Fiori' if int(i / n4s) == 2 else 'Quadri'))
        return self
        
    def cut(self, index = False):
        index = index if index else random.randint(0, len(self.cards))
        self.cards = self.cards[index:] +  self.cards[:index]
        return index
        
    def shuffle(self):
        cards = []
        for i in range(len(self.cards)):
            self.cut()
            cards.append(self.cards.pop())
        self.cards = cards[:]
        return self
        
    def print(self):
        print(self.cards)
        
if __name__ == "__main__":
    mazzo = deck().loadSTD().shuffle().print()