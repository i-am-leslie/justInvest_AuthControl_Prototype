class rbac():
    def __init__(self):
        self.acl={"Client": ["ViewAccountBalance", "ViewInvestments", "ViewContactDetails"],
                  "PremiumClient": ["ModifyInvestmentPortfolio", "ViewFinancialPlannerDetails", "ViewInvestmentAnalystDetails"],
                  "Employee":["ViewClientAccountBalance", "ViewInvestments"],
                  "FinancialPlanner": ["ViewMoneyMarketInstruments", "ModifyInvestmentPortfolio"],
                  "Teller": [],
                  "FinancialAdvisor": ["ViewMoneyMarketInstruments", "ModifyInvestmentPortfolio"]
                  }
        
    
    def get_permissions(self, role):
        # Retrieve the list of permissions for a given role
        return self.acl.get(role, [])
    

def main():
   System= rbac()
   System.get_permissions("Client")


if __name__ == "__main__":
    main()
