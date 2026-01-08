from src.personal_acount import PersonalAccount
import time
import requests

class TestPerfomanceOfCreatingAccounts:
    url = "http://127.0.0.1:5000/api"
    
    def test_delete_account_100_times(self):
        is_everytime_successful = True
        for _ in range(100):
            start = time.time()
            # creating account
            url = f"{self.url}/accounts"
            payload = {
                "first_name": "Jan",
                "last_name": "Dykowski",
                "pesel": "05210700056"
            }
            response = requests.post(url, json=payload)
            # deleting account
            url_del = f"{self.url}/accounts/05210700056"
            response_2 = requests.delete(url_del)
            end = time.time()
            duration = end - start
            if duration > 0.05:
                is_everytime_successful = False

        assert is_everytime_successful == True

    def test_100_times_getting_money(self):
        is_everytime_successful = True
        url = f"{self.url}/accounts"
        payload = {
                "first_name": "Jan",
                "last_name": "Dykowski",
                "pesel": "05210700057"
            }
        response = requests.post(url, json=payload)
        for _ in range(100):
            start = time.time()
            # getting money
            url = f"{self.url}/accounts/05210700057/transfer"
            payload = {
                "amount": 500,
                "type": "incoming"
            }
            response = requests.post(url, json=payload)
            end = time.time()
            duration = end - start
            if duration > 0.05:
                is_everytime_successful = False            
        #gettting account balance to check if money was added
        url_account = f"{self.url}/accounts/05210700057"
        response_account = requests.get(url_account)

        assert is_everytime_successful == True and response_account.json()["balance"] == 50000
