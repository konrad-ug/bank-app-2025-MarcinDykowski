from src.account import Account

class CompanyAccount(Account):
    def __init__ (self, company_name, nip):
        self.company_name = company_name
        self.nip = nip

        if (len(company_name) != 10):
            self.company_name = "Invalid"
