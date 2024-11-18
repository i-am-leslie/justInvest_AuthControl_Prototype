# Need to write why i used this import
import re   
from Users import *
from AccessControl import rbac


class JustInvestSystem:
    def __init__(self):
        self.users = {}  # Store users with their usernames as keys
        self.rbac = rbac() 

    def add_user(self, user):
        self.users[user.userName] = user

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            print(user.display_info)
            return user
        return None

    def display_user_operations(self, user):
        if user:
            return self.rbac.get_permissions(user.getRole())
        return "Access Denied"

    def check_password(self, password, username):
        if len(password) < 8 or len(password) > 12:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'\d', password):
            return False
        if not re.search(r'[!@#$%*&]', password):
            return False
        if password == username:
            return False
        # Add check for common passwords here if necessary
        return True

    def register_user(self):
        print("Welcome to justinvest please choose from the following options")
        print("Register a new user")
        
        # Prompt for username
        username = input("Enter username: ")
        
        # Prompt for password with validation
        while True:
            password = input("Enter password: ")
            if not self.check_password(password, username):
                print("Password does not meet requirements.")
            else:
                break
        
        # Select role
        print("Select user role:")
        print("1. Client")
        print("2. Premium Client")
        print("3. Financial Advisor")
        print("4. Financial Planner")
        print("5. Teller")
        print("6. Employee")
        
        role_choice = input("Enter role number: ")
        
        # Create user instance based on role choice
        if role_choice == "1":
            user = Client(username, password)
        elif role_choice == "2":
            user = PremiumClient(username, password)
        elif role_choice == "3":
            user = FinancialAdvisor(username, password)
        elif role_choice == "4":
            user = FinancialPlanner(username, password)
        elif role_choice == "5":
            # Assume Tellers have business hours specified, for simplicity here we use a static range
            user = Teller(username, password, business_hours=(9, 17))
        elif role_choice == "6":
            user = Employee(username, password)
        else:
            print("Invalid role selection.")
            return
        
        # Add the new user to the system
        self.add_user(user)
        print(f"User '{username}' registered successfully as a {user.__class__.__name__}.")
        print(f"These are the actions you can perform on the system: {self.rbac.get_permissions(user.__class__.__name__)}")