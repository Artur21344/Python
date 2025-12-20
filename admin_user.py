class User:
    def __init__(self,name):
        self.name = name

class Admin(User):
    def main(self):
        return f"Admin: {self.name}"

def block_user(user):
    return f"User {user.name} has been blocked."

admin1 = Admin("Artur")
print(admin1.main())

User1 = User("Bob")
print(User1.name)
print(f"User: {User1.name} hello")

print(Admin("Artur").main())
print(f"Hello {admin1.name}")