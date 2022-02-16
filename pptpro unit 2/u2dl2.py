class parrot:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    def