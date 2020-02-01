class Superuser:
    def __init__(self, name, password):
        self.name = name
        self.__password = self.__encrypt_passwd(password)

    def __encrypt_passwd(self, password):
        return password.upper()

    def get_passwd(self):
        return self.__password

sergio = Superuser("Vanessa", "sergiosergio")
print(sergio.get_passwd())
print(sergio.name)