class Animal:
    @property
    def terrestrial(self):
        return True
    @property
    def breathe_watter(self):
        return False

class Felines(Animal):
    @property
    def retractable_claws(self):
        return True

    @property
    def bark(self):
        return False

    @property
    def haunter(self):
        print("All felines have wedding instinct")
class pet_name:
    name = ''
    def cat_name(self):
        print(self.name)
class Cheeta(Felines):
    @property
    def color(self):
        print("Is spotted")

    @property
    def contexture(self):
        print("Athletic")

class Tiger(Felines):
    @property
    def color(self):
        print("Is striped")

    @property
    def contexture(self):
        print("Is brawny")

class Cat(Felines, pet_name):
    @property
    def color(self):
        print("Is peludo ")

    @property
    def behave(self):
        self.haunter #here inheriting attributes


    def cat_name(self):
        pet_name.cat_name(self):
        print("The name of my cat is : {}".format(self.name))

cat = Cat()
cat.name = "Rolo"
cat.cat_name()