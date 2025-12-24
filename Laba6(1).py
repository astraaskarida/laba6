class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return password == self.__password


user = UserAccount("roman", "roman@mail.ru", "123456")

print(user.check_password("123456"))
print(user.check_password("000000"))

user.set_password("newpass")
print(user.check_password("newpass"))