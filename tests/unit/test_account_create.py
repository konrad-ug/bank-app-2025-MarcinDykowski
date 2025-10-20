from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        assert account.pesel == "12345678901"
    
    def test_wrong_pesel_short(self):
        account = Account("Jane", "Doe", "12345")
        assert account.pesel == "Invalid"
    
    def test_wrong_pesel_long(self):
        account = Account("Jane", "Doe", "123454323244234224242")
        assert account.pesel == "Invalid"
    
    def test_wrong_pesel_non_digit(self):
        account = Account("Jane", "Doe", None)
        assert account.pesel == "Invalid"

    def test_Correct_Promo_Code(self):
        account = Account("Jane", "Doe", "1234566778901", "PROM_YTS")
        assert account.balance == 50

    def test_Wierd_Promo_Code(self):
        account = Account("Jane", "Doe", "1234566778901", "PIESEK_PIESEK")
        assert account.balance == 0
    
    def test_To_Long_Promo_Code(self):
        account = Account("Jane", "Doe", "1234566778901", "PROM_WYZS")
        assert account.balance == 0

    def test_To_Short_Promo_Code(self):
        account = Account("Jane", "Doe", "1234566778901", "PROM_wz")
        assert account.balance == 0

    def test_Old_Person(self):
        account = Account("Jane", "Doe", "5809566778901", "PROM_XYZ")
        assert account.balance == 0

    def test_Young_Person(self):
        account = Account("Marcin", "Dykowski", "05210700056", "PROM_XYZ")
        assert account.balance == 50