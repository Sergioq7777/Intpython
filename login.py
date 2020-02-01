""" class login_user:
    def __init__(self, username, pasword, mail):
        self.username = username
        self.__pasword = self.__encrypt_pass(pasword)
        self.mail = mail

    def __encrypt_pass(self, pasword):
        return pasword.upper()

    @property
    def password(self):
        return self.__pasword

sergio = login_user("Sergio", "vaneee", "sergioq777")
print(sergio.username)
print(sergio.password)
print(sergio.mail) """

class user:
    def __init__(self, name, sex, pasword, mail):
        self.name = name
        self.sex = sex
        self.__pasword = self.__upper_pass(pasword)
        self.mail = mail

    def __upper_pass(self, pasword):
        return pasword.upper()
    @property
    def get_pass(self):
        return self.__pasword


sergio = user("Sergio", "male", "vanessa", "sergio777")
print(sergio.password)