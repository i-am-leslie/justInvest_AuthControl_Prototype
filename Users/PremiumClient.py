from .User import User

class PremiumClient(User):


    def __init__(self, username,passWord):
        super().__init__(username,passWord)
        self.FinancialPlanners = "FinancialPlanners"
        self.investmentPortfolio = "investmentPortfolio"

    def get_permissions(self):
        """Abstract method to retrieve permissions for the user role."""
        pass