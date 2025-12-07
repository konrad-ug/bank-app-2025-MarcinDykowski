import pytest
import requests

class TestAPI:
    url = "http://localhost:5000/api"
    
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        # setup - dodaj konto
        payload = {
            "first_name": "Anita",
            "last_name": "Fisher",
            "pesel": "05710700056"
        }
        response = requests.post(f"{self.url}/accounts", json=payload)
        assert response.status_code == 200

        yield

        # cleanup - usuń wszystkie konta
        all_accounts = requests.get(f"{self.url}/accounts").json()
        for account in all_accounts:
            response_delete = requests.delete(f"{self.url}/accounts/{account['pesel']}")

    def test_getting_money(self):
        url = f"{self.url}/accounts/05710700056/transfer"
        payload = {
            "amount": 500,
            "type": "incoming"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 200

    def test_getting_money_on_minus(self):
        url = f"{self.url}/accounts/05710700056/transfer"
        payload = {
            "amount": -500,
            "type": "incoming"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 400

    def test_getting_money_nonexisting_transfer_type(self):
        url = f"{self.url}/accounts/05710700056/transfer"
        payload = {
            "amount": 500,
            "type": "NOT_EXISTING"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 404

    def test_getting_money_outgoing_enough_cash(self):
        url = f"{self.url}/accounts/05710700056/transfer"
        payload = {
            "amount": 500,
            "type": "incoming"
        }
        response = requests.post(url, json=payload)

        payload2 = {
            "amount": 200,
            "type": "outgoing"
        }
        response2 = requests.post(url, json=payload2)
  
        assert response.status_code == 200 

    def test_getting_money_outgoing__not_enough_cash(self):
        url = f"{self.url}/accounts/05710700056/transfer"
        payload = {
            "amount": 500,
            "type": "incoming"
        }
        response = requests.post(url, json=payload)

        payload2 = {
            "amount": 700,
            "type": "outgoing"
        }
        response2 = requests.post(url, json=payload2)
  
        assert response2.status_code == 422  

    def test_outgoing_express_money_enough(self):
        url = f"{self.url}/accounts/05710700056/transfer"
        payload = {
            "amount": 500,
            "type": "incoming"
        }
        response = requests.post(url, json=payload)

        payload2 = {
            "amount": 500,
            "type": "express"
        }
        response2 = requests.post(url, json=payload2)
  
        assert response2.status_code == 200

    def test_outgoing_express_money_not_enough(self):
        url = f"{self.url}/accounts/05710700056/transfer"
        payload = {
            "amount": 500,
            "type": "incoming"
        }
        response = requests.post(url, json=payload)

        payload2 = {
            "amount": 900,
            "type": "express"
        }
        response2 = requests.post(url, json=payload2)
  
        assert response2.status_code == 422