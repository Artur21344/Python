class User:
    def __init__(self,name):
        self.name = name

class Admin(User):
    def main(self):
        return f"Admin: {self.name}"
def password_do(admin):
    return f"Admin {admin.name} changed password."
def block_user(user):
    return f"User {user.name} has been blocked."

def hello_user(user):
    return f"Hello i am {user.__class__.__name__} my name is {user.name}"

admin1 = Admin("Artur")
print(admin1.main())

User1 = User("Bob")
print(hello_user(User1))

print(Admin("Artur").main())
print(hello_user(admin1))