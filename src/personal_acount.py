from src.account import Account
        
class PersonalAccount(Account):
    def __init__(self, first_name, last_name, pesel, promo_code = None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 50 if self.is_promo_code(promo_code, pesel) else 0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        self.history = []

    def is_pesel_valid(self, pesel):
        if isinstance(pesel, str) and len(pesel) == 11:
            return True
        else:
            return False
    
    def is_promo_code(self, promo_code, pesel):
        if (promo_code != None and promo_code[0:5] == "PROM_" and len(promo_code[5:]) == 3) and ((int(pesel[0:2]) > 60 and int(pesel[2:4] < 20)) or (int(pesel[2:4]) > 20)):
            return True
        else:
            return False
    
    def helper_sumbit_for_loan_checks_if_three_last_trasactions_are_on_plus(self):
        if len(self.history) >= 3 and self.history[-1] > 0 and self.history[-2] > 0 and self.history[-3] > 0:
            return True
        else:
            return False
        
    def helper_submit_for_loan_checks_if_total_sum_of_last_five_transactions_are_bigger_than_ammount_of_loan(self, ammount):
        if len(self.history) >= 5 and (self.history[-1] + self.history[-2] + self.history[-3] + self.history[-4] + self.history[-5])>ammount:
            return True
        else:
            return False

    def submit_for_loan(self, ammount):
        if self.helper_sumbit_for_loan_checks_if_three_last_trasactions_are_on_plus() == True:
            self.balance += ammount
            return True
        elif self.helper_submit_for_loan_checks_if_total_sum_of_last_five_transactions_are_bigger_than_ammount_of_loan(ammount) == True:
            self.balance += ammount
            return True
        else:
            return False

class AccountRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: PersonalAccount):
        self.accounts.append(account)
    
    def search_pesel(self, pesel):
        for i in self.accounts:
            if i.pesel == pesel:
                return [i.first_name, i.last_name, i.pesel]
        return False

    def every_account(self):
        return [[a.first_name, a.last_name, a.pesel] for a in self.accounts]

    def number_of_accounts(self):
        return len(self.accounts)