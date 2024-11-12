from .User import User

class Client(User):


    def __init__(self, username, passWord):
        super().__init__(username,passWord)
        # self.financialAdvisor = financialAdvisor
        # self.investmentPortfolio = investmentPortfolio


    def get_permissions(self):
        """Abstract method to retrieve permissions for the user role."""
        pass