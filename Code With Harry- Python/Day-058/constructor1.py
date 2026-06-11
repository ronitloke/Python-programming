class person:
    # name="Ronit"
    # occ="Dev"
    def __init__(self,n,o):       #Creating a constructor
        self.name=n
        self.occ=o
        print("Hey i am a person")

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("Ronit","Dev")
b=person("xyz", "HR")
# c=person(1,2,3) TypeError: person.__init__() takes 3 positional arguments but 4 were given
# c is considered as 'self' and is automatically passed thats why it says 4 args given
a.info()
b.info()