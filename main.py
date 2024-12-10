from System.JustInvestSystem import JustInvestSystem
from Users import Teller
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
                print(f"Welcome, {username}!")
                if user== "Teller" and not Teller.is_business_hours():
                    print("You can only use the system at the allocated time")

                system.change_logged_in_status()
                while system.logged_in_status():
                    print(f"username:{username} \n")
                    system.display_user_operations(user)
                    print("Press 0 to exit the system\n")
                    choice = input("Enter action: \n")
                    if choice=="0":
                        system.change_logged_in_status()

            else:
                print("Invalid username or password.")
        elif choice == "3":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

