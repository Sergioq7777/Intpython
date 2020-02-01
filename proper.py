class users:
    def __init__(self, username, pasword, mail):
        self.username = username
        self.__pasword = self.__Upper_pass(pasword)
        self.mail = mail

    def __Upper_pass(self, pasword):
        return pasword.upper()
    @property
    def pasword(self):
        return self.__pasword

sergio = users("Sergio", "Vanessa", "sergioq.777")
print(sergio.pasword)
sergio.pasword = "NuevaNueva"
print(sergio.pasword)