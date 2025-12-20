class User:
    def __init__(self,name):
        self.name = name
    
    def hello(self):
        return f"Hello, {self.name}!"
    
    def get_role(self):
        return "User"

class Admin(User):
    def get_role(self):
        return "Admin"



admin1 = Admin("Artur")
print(admin1.hello())
print(admin1.get_role())

User1 = User("Bob")
print(User1.hello())
print(User1.get_role())
