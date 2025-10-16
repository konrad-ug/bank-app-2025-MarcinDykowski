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