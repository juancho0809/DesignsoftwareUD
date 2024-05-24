from abc import ABC

class User(ABC):
    def __init__(self):
        self.users = {}  

    def register(self, username, password):
        if username not in self.users: 
            self.users[username] = password
            print(f"User '{username}' registered success")
        else:
            print(f"User '{username}' already exists.")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"User '{username}' logged in successfully!")
        else:
            print("Error: Invalid username or password.")

    def logout(self, username):
        print(f"User '{username}' logged out successfully!")


class Client(User):
    def __init__(self):
        super().__init__()
    

class Admin(User):
    def __init__(self):
        super().__init__()
