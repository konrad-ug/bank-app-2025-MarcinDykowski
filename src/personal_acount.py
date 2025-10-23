from src.account import Account

class Personal_Account(Account):
    def __init__(self, first_name, last_name, pesel, promo_code = None):
        self.first_name = first_name
        self.last_name = last_name
        # print(pesel)
        # print(promo_code)
        self.balance = 50 if self.is_promo_code(promo_code, pesel) else 0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        

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
