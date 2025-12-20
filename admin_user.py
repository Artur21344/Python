class User:
    def __init__(self,name):
        self.name = name
    def get_role(self):
        return "User"

class Admin(User):
    def get_role(self):
        return "Admin"

def hello(self):
    return f"Hello, I am {self.name} my role {self.get_role()}"

User.hello = hello
Admin.hello = hello

user1 = User("Bob")
admin1 = Admin("Artur") 

print(user1.hello())
print(admin1.hello())
