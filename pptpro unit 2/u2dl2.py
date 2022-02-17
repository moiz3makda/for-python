class parrot:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    def dance(self,style):
        return "{} is now dancing in {} style".format(self.name,style)

blu = parrot("blu",3)
print(blu.sing("'Happy'"))
print(blu.dance("hiphop"))
