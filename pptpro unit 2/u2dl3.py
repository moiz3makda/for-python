class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("swim faster")

class Panguin(Bird):
    def __init__(self):
        super().__init__()
        print("Panguin is ready")

    def whoisthis(self):
        print("Panguin")

    def run(self):
        print("Run faster")

paggy = Panguin()
paggy.whoisthis()
paggy.run()
paggy.swim()