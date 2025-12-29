from requests import patch
from src.Comany_Account import CompanyAccount
from unittest.mock import patch, Mock
from src.smtp.smtp import SMTPClient

class TestCompanyEmail:

    # correct email sending
    @patch('src.smtp.smtp.SMTPClient.send', return_value=True)
    @patch('src.Comany_Account.requests.get')
    def testing_sending_company_account_email(self, mock_get, mock_send):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': {'subject': {'statusVat': 'Czynny'}}}
        mock_get.return_value = mock_response
        
        self.account = CompanyAccount("Januszex", "1234563218")
        email = "alice@example.com"
        self.account.history = [100, 200, -50, 300, -100]

        result = self.account.send_history_via_email(email)

        assert result == True

        mock_send.assert_called_once()
        subject = mock_send.call_args[0][0]
        text = mock_send.call_args[0][1]

    # incorrect email sending
    @patch('src.smtp.smtp.SMTPClient.send', return_value=False)
    @patch('src.Comany_Account.requests.get')
    def testing_sending_company_account_email_fail(self, mock_get, mock_send):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': {'subject': {'statusVat': 'Czynny'}}}
        mock_get.return_value = mock_response
        
        self.account = CompanyAccount("Januszex", "1234563218")
        email = "alice@example.com"
        self.account.history = [100, 200, -50, 300, -100]

        result = self.account.send_history_via_email(email)

        assert result == False
        mock_send.assert_called_once()
        subject = mock_send.call_args[0][0]
        text = mock_send.call_args[0][1]      