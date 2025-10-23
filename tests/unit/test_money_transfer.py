from src.personal_acount import Personal_Account
from src.Comany_Account import CompanyAccount

class Test_transfer:
    def test_getting_money(self):
        account = Personal_Account("John", "Doe", "05210700056")
        account.getting_money(100)
        assert account.balance == 100
    
    def test_getting_money_with_promo_code(self):
        account = Personal_Account("John", "Doe", "05210700056", "PROM_XYZ")
        account.getting_money(100)
        assert account.balance == 150

    def test_outgoing_trasnfer(self):
        account = Personal_Account("John", "Doe", "05210700056")
        account.balance = 100
        account.outgoing_transer(50)
        assert account.balance == 50

    def test_outgoing_trasnfer_exeding_ammout(self):
        account = Personal_Account("John", "Doe", "05210700056")
        account.balance = 100
        account.outgoing_transer(500)
        assert account.balance == 100

    def test_outgoing_trasnfe_negative(self):
        account = Personal_Account("John", "Doe", "05210700056")
        account.balance = 100
        account.outgoing_transer(-50)
        assert account.balance == 100

    # company transfers
    def test_Company_money_transfer(self):
        account = CompanyAccount("BANK_22", "1234567890")
        account.balance = 10000
        account.getting_money(5000)
        assert account.balance == 15000

    def test_Company_outgoing_money(self):
        account = CompanyAccount("Bank_33","1234567890")
        account.balance = 10000
        account.outgoing_transer(5000)
        assert account.balance == 5000  

    def test_Company_outgoing_money_to_much(self):
        account = CompanyAccount("Bank_33","1234567890")
        account.balance = 10000
        account.outgoing_transer(50000)
        assert account.balance == 10000  

    def test_Fast_money_outgoing_Company(self):
        account = CompanyAccount("Bank_33","1234567890")
        account.balance = 500
        account.fast_outgoing_transfer(400)
        assert account.balance == 95
 
    def test_Fast_money_outgoing_to_much_Company(self):
        account = CompanyAccount("Bank_33","1234567890")
        account.balance = 500
        account.fast_outgoing_transfer(44400)
        assert account.balance == 500

    def test_Fast_money_outgoing_going_on_minus_Company(self):
        account = CompanyAccount("Bank_33","1234567890")
        account.balance = 500
        account.fast_outgoing_transfer(500)
        assert account.balance == -5

    def test_Fast_money_outgoing_Personal(self):
        account = Personal_Account("John", "Doe", "05210700056")
        account.balance = 500
        account.fast_outgoing_transfer(400)
        assert account.balance == 99
 
    def test_Fast_money_outgoing_to_much_Personal(self):
        account = Personal_Account("John", "Doe", "05210700056")
        account.balance = 500
        account.fast_outgoing_transfer(44400)
        assert account.balance == 500

    def test_Fast_money_outgoing_going_on_minus_Personal(self):
        account = Personal_Account("John", "Doe", "05210700056")
        account.balance = 500
        account.fast_outgoing_transfer(500)
        assert account.balance == -1