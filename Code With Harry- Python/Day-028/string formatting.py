x="hey my name is {0} and i m from {1}"
name="Ronit"
country="India"
print(x.format(name,country))

y=f"hey my name is {name} and i m from {country}"
print(y)
print(type(f"{2*30}"))


z=f"hey my name is {{name}} and i m from {{country}}" #double curly braces for printing as it is
print(z)
