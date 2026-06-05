class person:
    name="Ronit"
    occupation="AI Engineer"
    Age=29
    def info(self):
        print(f"{self.name} is an {self.occupation}")
a=person()
a.info()
a.name="xyz"
a.info()

