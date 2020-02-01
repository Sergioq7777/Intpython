class User:
    def __init__(self, name, telephone, address, mail):
        self.__name = self.__encrypt_name(name)
        self.telephone = telephone
        self.address = address
        self.mail = mail

    def __encrypt_name(self, name):
        return name.upper()

    def get_name(self):
        return self.__name

sergio = User("vanessa", 31516168, "cr33336", "vannnerr")
#sergio.name = "Maleja"
#print(sergio.__name)
print(sergio.get_name())
print(sergio.telephone)
print(sergio.address)
print(sergio.mail)