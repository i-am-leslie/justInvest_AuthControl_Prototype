from .User import User

class FinancialAdvisor(User):


    def __init__(self, username, PhoneNumber,passWord):
        super().__init__(username,passWord)
        self.PhoneNumber = PhoneNumber
        # Private  Consumer instrument dont know 

    def get_permissions(self):
        """Abstract method to retrieve permissions for the user role."""
        pass