from src.account import Account

class CompanyAccount(Account):
    def __init__ (self, company_name, nip):
        self.company_name = company_name
        self.nip = nip
        self.balance = 0
        self.history = []

        if (len(nip) != 10):
            self.nip = "Invalid"
    
    def submit_for_loan(self, ammount):
        if self.balance > ammount*2 and -1775 in self.history:
            self.balance += ammount
            return True
        else:
            return False