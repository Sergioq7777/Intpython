class user:
    def __init__(self, name, password, email):
        self.name = name
        self.password = self.encrypt(password)
        self.email = email

    def encrypt(self, password):
        return password.upper()

    def get_pss(self):
        return self.password

sergio = user("Sergio", "vanessa", "Sergioq.7777")
print(sergio.name)
print(sergio.get_pss())
print(sergio.email)