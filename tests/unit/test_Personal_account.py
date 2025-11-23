from src.personal_acount import PersonalAccount
from src.Comany_Account import CompanyAccount
from src.personal_acount import AccountRegistry
import pytest

class TestAccount:

    # Test tworzenia konta — bez parametryzacji
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe", "12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        assert account.pesel == "12345678901"

    # Sparametryzowane testy błędnych PESELi
    @pytest.mark.parametrize(
        "pesel",
        [
            "12345",                        # za krótki
            "123454323244234224242",        # za długi
            None,                           # nie-cyfry
        ],
        ids=[
            "pesel_too_short",
            "pesel_too_long",
            "pesel_non_digit",
        ]
    )
    def test_wrong_pesel(self, pesel):
        account = PersonalAccount("Jane", "Doe", pesel)
        assert account.pesel == "Invalid"

    # Sparametryzowane testy kodów promocyjnych
    @pytest.mark.parametrize(
        "pesel, promo, expected_balance",
        [
            ("1234566778901", "PROM_YTS", 50),     # poprawny kod
            ("1234566778901", "PIESEK_PIESEK", 0), # dziwny kod
            ("1234566778901", "PROM_WYZS", 0),     # za długi kod
            ("1234566778901", "PROM_wz", 0),       # za krótki kod
            ("5809566778901", "PROM_XYZ", 0),      # stara osoba
            ("05210700056",   "PROM_XYZ", 50),     # młoda osoba
        ],
        ids=[
            "correct_promo_code",
            "weird_promo_code",
            "promo_too_long",
            "promo_too_short",
            "old_person_no_bonus",
            "young_person_bonus",
        ]
    )
    def test_promo_codes(self, pesel, promo, expected_balance):
        account = PersonalAccount("Jane", "Doe", pesel, promo)
        assert account.balance == expected_balance

class Test_AccountRegistry:
    @pytest.fixture(autouse=True)
    def setup_account(self):
        self.All_accounts = AccountRegistry()
        self.peapole = [PersonalAccount("Marcin", "Dykowski","05210700056"), PersonalAccount("Marcin", "Kowal", "06210700056"), PersonalAccount("Jan", "Nowak", "55210700056")]
        for i in self.peapole:
            self.All_accounts.add_account(i) 

    def test_adding_accounts(self):
        assert self.All_accounts.every_account() == [["Marcin", "Dykowski", "05210700056"], ["Marcin", "Kowal", "06210700056"], ["Jan", "Nowak", "55210700056"]]
    
    def test_count_accounts(self):
        assert self.All_accounts.number_of_accounts() == 3

    def test_search_pesel_correct(self):
        assert self.All_accounts.search_pesel("05210700056") == ["Marcin", "Dykowski", "05210700056"]
    
    def test_search_pesel_incorrect(self):
        assert self.All_accounts.search_pesel("05200700056") == False
