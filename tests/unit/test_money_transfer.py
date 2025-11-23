from src.personal_acount import PersonalAccount
from src.Comany_Account import CompanyAccount
import pytest


#   TESTY KONTA PERSONALNEGO

class TestPersonalTransfers:

    @pytest.fixture(autouse=True)
    def setup_account(self):
        self.account = PersonalAccount("Marcin", "Dykowski", "05210700056")

    @pytest.mark.parametrize(
        "transaction_type, amount, start_balance, expected_balance",
        [
            ("g", 100, 0, 100),
            ("o", 50, 100, 50),
            ("o", 500, 100, 100),
            ("o", -50, 100, 100),
        ],
        ids=[
            "test_getting_money",
            "test_outgoing_transfer",
            "test_outgoing_transfer_exceeding_amount",
            "test_outgoing_transfer_negative"
        ]
    )
    def test_transfers_parametrized(self, transaction_type, amount, start_balance, expected_balance):
        self.account.balance = start_balance
        if transaction_type == "g":
            self.account.getting_money(amount)
        else:
            self.account.outgoing_transer(amount)

        assert self.account.balance == expected_balance

    @pytest.mark.parametrize(
        "amount, start_balance, expected_balance",
        [
            (400, 500, 99),
            (444000, 500, 500),
            (500, 500, -1),
        ],
        ids=[
            "test_fast_outgoing",
            "test_fast_outgoing_too_much",
            "test_fast_outgoing_negative"
        ]
    )
    def test_fast_transfers_personal(self, amount, start_balance, expected_balance):
        self.account.balance = start_balance
        self.account.fast_outgoing_transfer(amount)
        assert self.account.balance == expected_balance

    def test_history_Personal(self):
        account = PersonalAccount("John", "Doe", "05210700056")
        account.balance = 100
        account.outgoing_transer(50)
        account.getting_money(800)
        account.fast_outgoing_transfer(300)
        assert account.history == [-50, 800, -300, -1]


#   TESTY KONTA FIRMOWEGO

class TestCompanyTransfers:

    @pytest.fixture(autouse=True)
    def setup_account(self):
        self.account = CompanyAccount("BANK_2137", "1234567890")

    @pytest.mark.parametrize(
        "transaction_type, amount, start_balance, expected_balance",
        [
            ("g", 5000, 10000, 15000),
            ("o", 5000, 10000, 5000),
            ("o", 50000, 10000, 10000),
        ],
        ids=[
            "test_company_money_transfer",
            "test_company_outgoing_money",
            "test_company_outgoing_exceeding"
        ]
    )
    def test_transfers_company(self, transaction_type, amount, start_balance, expected_balance):
        self.account.balance = start_balance
        if transaction_type == "g":
            self.account.getting_money(amount)
        else:
            self.account.outgoing_transer(amount)

        assert self.account.balance == expected_balance

    @pytest.mark.parametrize(
        "amount, start_balance, expected_balance",
        [
            (400, 500, 95),
            (444000, 500, 500),
            (500, 500, -5),
        ],
        ids=[
            "test_fast_outgoing_company",
            "test_fast_outgoing_company_too_much",
            "test_fast_outgoing_company_negative"
        ]
    )
    def test_fast_transfers_company(self, amount, start_balance, expected_balance):
        self.account.balance = start_balance
        self.account.fast_outgoing_transfer(amount)
        assert self.account.balance == expected_balance

    def test_history_Company(self):
        account = CompanyAccount("Bank_33", "1234567890")
        account.getting_money(50000)
        account.outgoing_transer(500)
        account.fast_outgoing_transfer(1000)
        assert account.history == [50000, -500, -1000, -5]