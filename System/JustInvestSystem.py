# Need to write why i used this import
import os
import re   
from Users import *
from AccessControl import rbac
import secrets
import hashlib


class JustInvestSystem:
    def __init__(self):
        self.users = {}  # Store users with their usernames as keys
        self.rbac = rbac() 
        self.common_weak_passwords = None
        self.weak_password_file = 'weak_passd.txt'
        self.logged_in=False
    
    def logged_in_status(self):
        return self.logged_in

    def add_user(self, user):
        self.users[user.userName] = user

    def login(self, username, password):
        password_file=PasswordFile()
        records=password_file.get_record(username)
       
        rehashed_password=password_file.hash_password(password,records['salt'])
        if rehashed_password == records['hashed_password']: 
            return records['role']
        print("No password records found for the username.")
        return None

    def display_user_operations(self, user):
        if user:
            j=0
            for x in self.rbac.get_permissions(user):
                j=j+1
                print(f"{j}" +" "+ x)
        return "Access Denied"
    
    def load_weak_passwords(self):
            try:
                with open(self.weak_password_file, 'r') as file:
                    self.common_weak_passwords = set(file.read().splitlines())
            except FileNotFoundError:
                self.common_weak_passwords = set(["password"])

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
        # check for common passwords
        if password in self.common_weak_passwords:
            print("Password in common weak password")
            return False

        return True

    def register_user(self):
        print("Welcome to justinvest please choose from the following options")
        print("Register a new user")
        
        # Prompt for username
        username = input("Enter username: ")
        password_file=PasswordFile()
        salt = secrets.token_hex(16)
        self.load_weak_passwords()

        
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
        hashed_password = password_file.hash_password(password, salt)
        password_file.add_record(username, salt,
                            hashed_password, user.__class__.__name__)
        




class PasswordFile:
    def __init__(self, file_name='passwd.txt'):
        current_directory = os.getcwd()
        self.file_path = os.path.join(current_directory, file_name)

        # Check if the file already exists
        if os.path.exists(self.file_path):
            print(f"File '{self.file_path}' already exists.")
        else:
            print(f"File '{self.file_path}' does not exist.")

    def hash_password(self, password, salt):
        """
        Hashes the password using SHA-256 and a salt.
        """
        hash_object = hashlib.sha256()
        hash_object.update((password + salt).encode('utf-8'))
        hashed_password = hash_object.hexdigest()
        return hashed_password

    def add_record(self, user_id, salt, hashed_password, role):
        """
        Adds a new record to the password file.
        """
        with open(self.file_path, 'a') as file:
            file.write(f"{user_id}:{salt}:{hashed_password}:{role}\n")

    def get_record(self, username):
        """
        Retrieves a record from the password file based on user ID.
        """
        with open(self.file_path, 'r') as file:
            for line in file:
                fields = line.strip().split(':')
                if fields[0] == username:
                    return {
                        'username': fields[0],
                        'salt': fields[1],
                        'hashed_password': fields[2],
                        'role': fields[3]
                    }
        return None
