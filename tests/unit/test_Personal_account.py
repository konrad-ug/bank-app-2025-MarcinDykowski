from src.personal_acount import Personal_Account
from src.Comany_Account import CompanyAccount

class TestAccount:
    def test_account_creation(self):
        account = Personal_Account("John", "Doe", "12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        assert account.pesel == "12345678901"
    
    def test_wrong_pesel_short(self):
        account = Personal_Account("Jane", "Doe", "12345")
        assert account.pesel == "Invalid"
    
    def test_wrong_pesel_long(self):
        account = Personal_Account("Jane", "Doe", "123454323244234224242")
        assert account.pesel == "Invalid"
    
    def test_wrong_pesel_non_digit(self):
        account = Personal_Account("Jane", "Doe", None)
        assert account.pesel == "Invalid"

    def test_Correct_Promo_Code(self):
        account = Personal_Account("Jane", "Doe", "1234566778901", "PROM_YTS")
        assert account.balance == 50

    def test_Wierd_Promo_Code(self):
        account = Personal_Account("Jane", "Doe", "1234566778901", "PIESEK_PIESEK")
        assert account.balance == 0
    
    def test_To_Long_Promo_Code(self):
        account = Personal_Account("Jane", "Doe", "1234566778901", "PROM_WYZS")
        assert account.balance == 0

    def test_To_Short_Promo_Code(self):
        account = Personal_Account("Jane", "Doe", "1234566778901", "PROM_wz")
        assert account.balance == 0

    def test_Old_Person(self):
        account = Personal_Account("Jane", "Doe", "5809566778901", "PROM_XYZ")
        assert account.balance == 0

    def test_Young_Person(self):
        account = Personal_Account("Marcin", "Dykowski", "05210700056", "PROM_XYZ")
        assert account.balance == 50


    class TestAccount_2:
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