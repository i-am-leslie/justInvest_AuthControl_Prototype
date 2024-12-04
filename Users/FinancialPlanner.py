from .User import User

class FinancialPlanner(User):


    def __init__(self, username, PhoneNumber,passWord):
        super().__init__(username,passWord)
        self.PhoneNumber = 0
        # Money market instrument dont know 

    def get_permissions(self):
        """Abstract method to retrieve permissions for the user role."""
        pass