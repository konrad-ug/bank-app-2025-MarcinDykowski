from src.personal_acount import PersonalAccount
import pytest

class Test_transfer_Personal:

    # Fixture tworząca konto i automatycznie przypisywana do self.account
    @pytest.fixture(autouse=True)
    def setup_account(self):
        self.account = PersonalAccount("Marcin", "Dykowski", "05210700056")

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
            ([500, 600, 100], 10000, True, 11200),
            ([500, -200, 100], 10000, False, 400),
            ([500, 100], 10000, False , 600),
            ([199, -30, -100, 200, 150], 200, True, 619),
            ([199, -30, 200, 150], 200, False, 519),
            ([199, -30, 200], 900, False, 369),
        ],
        ids=[
            "test_Personal_submit_for_loan_3_getting_money",
            "test_Personal_submit_for_loan_2_getting_money_1_outgoing",
            "test_Personal_submit_for_loan_2_getting_money",
            "test_Personal_submit_for_loan_getting_money_beaing_on_plus",
            "test_Personal_submit_for_loan_2_getting_money_beaing_on_minus",
            "test_liitle_transactions",
        ]
    )
    def test_submit_for_loan_parametrized(self, history, amount, expected_result, expected_balance):
        self.replay_history(history)
        result = self.account.submit_for_loan(amount)
        assert result == expected_result
        assert self.account.balance == expected_balance