class User:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generate_password(password)
        self.email = email

    def __generate_password(self, password):
        return password.upper()

    def get_password(self):
        return self.__password

sergio = User("sergio", "cristal", "sergioq.7777@")
print(sergio.username)
#sergio.__password = "Change-pasword-injecction"# Here i can change the password without private class
#print(sergio.password)
print(sergio.get_password())
print(sergio.email)