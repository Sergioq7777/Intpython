class circle:
    pi = 3.141516
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio * self.radio * circle.pi #or .self

circle_uno = circle(4)
circle_dos = circle(7)



print(circle.pi)
print(circle_uno.area())
print(circle_dos.area())