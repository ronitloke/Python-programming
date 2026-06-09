class person:
    # name="Ronit"
    # occ="Dev"
    def __init__(self):       #Creating a constructor
        print("Hey i am a person")

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person()
b=person()
# a.info()