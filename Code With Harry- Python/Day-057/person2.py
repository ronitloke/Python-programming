class person:
    name="Ronit"
    occupation="AI Engineer"
    Age=29
    def info(self):
        print(f"{self.name} is an {self.occupation}")
a=person()
b=person()
c=person()
a.name="xyz"
b.name="pqr"
a.info()
b.info()
c.info()

# Benifit of self is that we don't need to print name repeatedly'

