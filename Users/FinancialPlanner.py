from .User import User

class FinancialPlanner(User):


    def __init__(self, username, PhoneNumber,passWord):
        super().__init__(username,passWord)
        self.PhoneNumber = PhoneNumber
        # Money market instrument dont know 

    def get_permissions(self):
        """Abstract method to retrieve permissions for the user role."""
        pass