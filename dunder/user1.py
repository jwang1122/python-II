"""
understand __name__
"""
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.cando = []

    def __repr__(self):
        return self.name
    
    # def isAllowd(self, thing):
    #     return thing in self.cando

    def do(self, something):
        # if self.isAllowd(something.__name__):
        #     something()
        if something.__name__ in self.cando:
            return something()
        else:
            print(f"{self.name}, you are not allowd to do {something.__name__}.")
    
    def setCanDo(self, cando):
        self.cando.append(cando)

def playPiano():
    print("playing piano...")

def writePython():
    print("coding python...")

if __name__ == '__main__':
    user1 = User("John", 1111)
    user1.setCanDo(playPiano.__name__)
    user1.do(playPiano)
    user1.do(writePython)
