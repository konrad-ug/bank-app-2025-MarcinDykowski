from src.personal_acount import PersonalAccount

class AccountRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: PersonalAccount):
        if (len(self.accounts) == 0 or self.search_pesel(account.pesel) == False):
            self.accounts.append(account)
            return True
        else:
            return False

    def search_pesel(self, pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                return [account.first_name, account.last_name, account.pesel, account.balance]
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

    def registry_money(self, pesel, amount, tranfer_type):
        for account in self.accounts:
            if account.pesel == pesel:
                if tranfer_type == "incoming":
                    account.getting_money(amount)
                    return True
                elif tranfer_type == "outgoing" and int(account.balance) >= int(amount):
                    print("PIESEK")
                    account.outgoing_transer(amount)
                    return True
                elif tranfer_type == "express" and account.balance + 1 >= amount:
                    account.fast_outgoing_transfer(amount)
                    return True
                else:
                    return False
            else:
                return False
    
