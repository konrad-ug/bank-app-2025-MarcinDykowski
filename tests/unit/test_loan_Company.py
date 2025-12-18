from src.Comany_Account import CompanyAccount
from unittest.mock import patch, Mock
import pytest

class Test_transfer_Company:
    # paremetry
    @pytest.fixture(autouse=True)
    @patch('src.Comany_Account.CompanyAccount.is_Nip_correct', return_value=True)
    def setup_account(self, mock_is_Nip_correct):
        self.account = CompanyAccount("KORPORACJA_TEST", "1234567890")

    def replay_history(self, history):
        #Pomocnicza funkcja do odtwarzania historii transakcji
        for h in history:
            if h > 0:
                self.account.getting_money(h)
            else:
                self.account.outgoing_transer(-h)

    @pytest.mark.parametrize(
        "history, amount, expected_result, expected_balance",
        [
            ([20000,50000,-5000, -1775], 30000, True, 93225),
            ([20000,50000,-5000, -1775], 50000, False, 63225),
            ([20000,50000,-5000], 30000, False, 65000),
            ([20000,50000,-5000,], 50000, False, 65000)
        ],
        ids=[
            "test_loan_succesful_every_condition",
            "test_loan_unuccesful_too_big_loan",
            "test_loan_unuccesful_no_ZUS",
            "test_loan_unsuccelful_to_big_and_no_ZUS"
        ]
    )
    # tests
    def test_submit_for_loan_parametrized(self, history, amount, expected_result ,expected_balance):
        self.replay_history(history)
        result = self.account.submit_for_loan(amount)
        assert result == expected_result
        assert self.account.balance == expected_balance