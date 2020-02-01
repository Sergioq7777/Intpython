class Felines:
    @property
    def claws(self):
        return True

    def mo_de(self):
        print("The feline it's haunting")

class Cat(Felines):
    pass
class Cheeta(Felines):
    def haunter_cat(self):
        self.mo_de()

class Tiger(Felines):
    pass

cat = Cat()
cheeta = Cheeta()   
tiger = Tiger()

print(cat.claws)
print(cheeta.haunter_cat())