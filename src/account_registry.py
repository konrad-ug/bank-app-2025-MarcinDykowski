from src.personal_acount import PersonalAccount

class AccountRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: PersonalAccount):
        self.accounts.append(account)
    
    def search_pesel(self, pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                return [account.first_name, account.last_name, account.pesel]
        return False

    def every_account(self):
        return self.accounts

    def number_of_accounts(self):
        return len(self.accounts)
    
    def update_account(self, pesel, new_first_name, new_last_name):
        for account in self.accounts:
            if account.pesel == pesel:
                account.first_name = new_first_name
                account.last_name = new_last_name
                return "Account Updated"
        return False

    def delete_account(self, pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                self.accounts.remove(account)
                return "Account deleted"
        return False
