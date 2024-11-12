from System.JustInvestSystem import JustInvestSystem
def main():
    system = JustInvestSystem()
    
    while True:
        print("\n")
        print("Welcome to justinvest please choose from the following options")
        print("\n1. Register a new user")
        print("2. Log in as an existing user")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            system.register_user ()
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = system.login(username, password)
            if user:
                print(f"Welcome, {username}! Here are your available operations:")
                print(system.display_user_operations(user))
            else:
                print("Invalid username or password.")
        elif choice == "3":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

