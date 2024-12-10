from .User import User

class FinancialAdvisor(User):


    def __init__(self, username,passWord):
        super().__init__(username,passWord)
        self.PhoneNumber = 0
        # Private  Consumer instrument dont know 

    def get_permissions(self):
        """Abstract method to retrieve permissions for the user role."""
        pass