import secrets
import string
from System.JustInvestSystem import JustInvestSystem
from Users import *

def generate_random_password(length=10):
    """Generate a random password containing uppercase, lowercase, digits, and special characters."""
    characters = string.ascii_letters + string.digits + "!@#$%*&"
    return ''.join(secrets.choice(characters) for _ in range(length))

def test_add_users_to_system():
    # Create an instance of JustInvestSystem
    system = JustInvestSystem()

    # List of sample employees and clients
    sample_data = [
        {"name": "Sasha Kim", "role": "Client"},
        {"name": "Emery Blake", "role": "Client"},
        {"name": "Noor Abbasi", "role": "Premium Client"},
        {"name": "Zuri Adebayo", "role": "Premium Client"},
        {"name": "Mikael Chen", "role": "Financial Advisor"},
        {"name": "Jordan Riley", "role": "Financial Advisor"},
        {"name": "Ellis Nakamura", "role": "Financial Planner"},
        {"name": "Harper Diaz", "role": "Financial Planner"},
        {"name": "Alex Hayes", "role": "Teller"},
        {"name": "Adair Patel", "role": "Teller"},
    ]

    # Add each user to the system
    for person in sample_data:
        username = person["name"].replace(" ", "").lower()
        password = generate_random_password()

        # Create a user instance based on the role
        if person["role"] == "Client":
            user = Client(username, password)
        elif person["role"] == "Premium Client":
            user = PremiumClient(username, password)
        elif person["role"] == "Financial Advisor":
            user = FinancialAdvisor(username, password)
        elif person["role"] == "Financial Planner":
            user = FinancialPlanner(username, password)
        elif person["role"] == "Teller":
            user = Teller(username, password)
        else:
            print(f"Unknown role for {person['name']}.")
            continue

        # Add the user to the system
        system.add_user(user)

        # Display information
        print(f"Added {person['name']} with username '{username}' and role '{user.role}'.")
        print(f"Randomly generated password: {password}")

# Run the test case
test_add_users_to_system()
