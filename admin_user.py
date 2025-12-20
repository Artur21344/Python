class User:
    def __init__(self,name, class_name = "User"):
        self.name = name
        self.class_name = class_name

    def hello(self):
        return f"Hello, I am {self.name} i am {self.class_name}"


class Admin(User):
    def __init__(self, name):
        super().__init__(name, class_name="Admin")
        
    def get_role(self):
        return "Admin"



admin1 = Admin("Artur")
print(admin1.hello())
print(admin1.get_role())

User1 = User("Bob")
print(User1.hello())
print(User1.class_name)
