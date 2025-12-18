import pytest
from src.Comany_Account import CompanyAccount
from unittest.mock import patch, Mock

class Test_company_acount():

    def test_firm_account_incorect_NIP(self):
        account = CompanyAccount("BANK_13", "12345678900090")
        assert account.nip == "Invalid"

    @patch('src.Comany_Account.CompanyAccount.is_Nip_correct', return_value=True)
    def test_Company_accout_Correct_NIP(self, mock_is_Nip_correct):
        account = CompanyAccount("BANK_13", "1234567890")
        assert account.nip == "1234567890"

    @patch('src.Comany_Account.requests.get')
    def test_correct_nip(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "result": {
                "subject": {
                    "statusVat": "Czynny",
                    "nip": "8461627563",
                    "name": "Firma Testowa"
                }
            }
        }

        account = CompanyAccount("BANK_13", "8461627563")
        
        assert account.is_Nip_correct("8461627563") == True

    @patch('src.Comany_Account.requests.get')
    def test_incorrect_nip(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "result": {
                "subject": {
                    "statusVat": "Zwolniony"
                }
            }
        }

        with pytest.raises(ValueError, match="Company not registered!!"):
                CompanyAccount("BANK_13", "8461627564")