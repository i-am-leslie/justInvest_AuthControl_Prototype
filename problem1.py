from AccessControl import rbac
import unittest


class testRBAC(unittest.TestCase):
    def setUp(self):
        # Setup a new instance of rbac for testing
        self.access_control = rbac()



        self.acl={"Client": ["ViewAccountBalance", "ViewInvestments", "ViewContactDetails"],
                  "PremiumClient": ["ModifyInvestmentPortfolio", "ViewFinancialPlannerDetails", "ViewInvestmentAnalystDetails"],
                  "Employee":["ViewAccountBalance", "ViewInvestments"],
                  "FinancialPlanner": ["ViewMoneyMarketInstruments", "ModifyInvestmentPortfolio"],
                  "Teller": [],
                  "FinancialAdvisor": ["ViewMoneyMarketInstruments", "ModifyInvestmentPortfolio"]
                  }

    # Test for client
    def test_client_permissions(self):
        permissions = self.access_control.get_permissions("Client")
        self.assertIn("ViewAccountBalance", permissions)
        self.assertIn("ViewInvestments", permissions)
        self.assertIn("ViewContactDetails", permissions)
        self.assertNotIn("ModifyInvestmentPortfolio", permissions)

    # Test for employee
    def test_employee_permissions(self):
        permissions = self.access_control.get_permissions("Employee")
        self.assertIn("ViewClientAccountBalance", permissions)
        self.assertIn("ViewInvestmentsPortfolio", permissions)
        self.assertNotIn("ModifyInvestmentPortfolio", permissions)

     # Test for premium client 
    def test_premium_client(self):
        permissions = self.access_control.get_permissions("PremiumClient")
        self.assertIn("ViewAccountBalance", permissions)
        self.assertIn("ViewInvestments", permissions)
        self.assertNotIn("ModifyInvestmentPortfolio", permissions)
    
    # Test for financial planner
    def test_financial_planner(self):
        permissions = self.access_control.get_permissions("FinancialPlanner")
        self.assertIn("ViewAccountBalance", permissions)
        self.assertIn("ViewInvestments", permissions)
        self.assertNotIn("ModifyInvestmentPortfolio", permissions)

     # Test for teller
    def test_teller(self):
        permissions = self.access_control.get_permissions("Teller")
        self.assertIn("ViewAccountBalance", permissions)
        self.assertIn("ViewInvestments", permissions)
        self.assertNotIn("ModifyInvestmentPortfolio", permissions)

     # Test for financial advisor
    def test_financial_advisor(self):
        permissions = self.access_control.get_permissions("FinancialAdvisor")
        self.assertIn("ViewAccountBalance", permissions)
        self.assertIn("ViewInvestments", permissions)
        self.assertNotIn("ModifyInvestmentPortfolio", permissions)

    # test for unknown role
    def test_no_permissions_for_unknown_role(self):
        permissions = self.access_control.get_permissions("UnknownRole")
        self.assertEqual(permissions, [])  # Expect an empty list

if __name__ == "__main__":
    unittest.main()