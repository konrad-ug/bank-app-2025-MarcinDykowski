from requests import patch
from src.personal_acount import PersonalAccount
from unittest.mock import patch, Mock
from src.smtp.smtp import SMTPClient

class TestPersonalEmail:

    # correct email sending
    @patch('src.smtp.smtp.SMTPClient.send', return_value=True)
    def testing_sending_personal_account_email(self, mock_send):
        self.account = PersonalAccount("Marcin", "Dykowski", "05210700056")
        email = "alice@example.com"
        self.account.history = [100, 200, -50, 300, -100]

        result = self.account.send_history_via_email(email)

        assert result == True

        mock_send.assert_called_once()
        subject = mock_send.call_args[0][0]
        text = mock_send.call_args[0][1]

    # incorrect email sending
    @patch('src.smtp.smtp.SMTPClient.send', return_value=False)
    def testing_sending_personal_account_email_fail(self, mock_send):
        self.account = PersonalAccount("Marcin", "Dykowski", "05210700056")
        email = "alice@example.com"
        self.account.history = [100, 200, -50, 300, -100]

        result = self.account.send_history_via_email(email)

        assert result == False
        mock_send.assert_called_once()
        subject = mock_send.call_args[0][0]
        text = mock_send.call_args[0][1]      