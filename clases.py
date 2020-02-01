class Car:
    color = "White"
    class_c = "sport"
    engine =  "Automatic"
    type_c = "SUV"
    model = 1990
    electric = False
    gasoline = True
    _break= True

    def breaking_car(self):
        print("This car its able to break the car")

    def gasoline(self):
        print("This car works with gasoline")

    def electric(self):
        if self.validator_electric() == True:
            print("this car works with electric")
        else:
            print("Better, choose a car that works with gasoline")

    def validator_electric(self):
        return self.electric


ford = Car()
ford.electric()
