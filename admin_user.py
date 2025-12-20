class User:
    def __init__(self,name):
        self.name = name
    def get_role(self):
        return "User"
    def hello(self):
        return f"Hello, I am {self.name} and my role is {self.get_role()}"

class Admin(User):
    def get_role(self):
        return "Admin"


user1 = User("Bob")
admin1 = Admin("Artur") 

print(user1.hello())
print(admin1.hello())
