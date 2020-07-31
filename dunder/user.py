class User:
    def __init__(self, name, id, cando):
        self.name = name
        self.id = id
        self.cando = cando

    # def __repr__(self):
    #     return self.name
    
    # def isAllowd(self, thing):
    #     return thing in self.cando

    def do(self, something):
        # if self.isAllowd(something.__name__):
        #     something()
        if something.__name__ in self.cando:
            return something()
        else:
            print(f"{self.name}, you are not allowd to do {something.__name__}.")
    
    # def setCanDo(self, cando):
    #     self.cando = cando