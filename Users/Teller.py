from .User import User

class Teller(User):


    def __init__(self, username,passWord):
        super().__init__(username,passWord)

    
    def get_permissions(self):
        """Abstract method to retrieve permissions for the user role."""
        pass