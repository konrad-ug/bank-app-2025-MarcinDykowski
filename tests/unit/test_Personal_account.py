from src.personal_acount import Personal_Account
from src.Comany_Account import CompanyAccount
import pytest


class TestAccount:

    # Test tworzenia konta — bez parametryzacji
    def test_account_creation(self):
        account = Personal_Account("John", "Doe", "12345678901")
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
        account = Personal_Account("Jane", "Doe", pesel)
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
        account = Personal_Account("Jane", "Doe", pesel, promo)
        assert account.balance == expected_balance