class User:
    def __init__(self, name, password, email):
        self.name = name
        self.__password = self.__upper_setter(password)
        self.email = email

    def __upper_setter(self, password):
        return password.upper()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        self.__password = self.__upper_setter(valor)

new_user = User("sergio", "vane", "sergio1")
print(new_user.password)
new_user.password = "fuck"
print(new_user.password)
