import pytest
import requests
from src.mongo_accounts_repository import MongoAccountsRepository

class TestAPIMongo:
    url = "http://127.0.0.1:5000"

    def test_create_account_then_save_it_and_then_delete_ervything_and_then_load_evrything(self):
        # clean in-memory registry and MongoDB to keep test deterministic
        requests.post(f"{self.url}/api/accounts/clear")
        MongoAccountsRepository().collection.delete_many({})

        url = f"{self.url}/api/accounts"
        payload = {
            "first_name": "Marcin",
            "last_name": "Dykowski",
            "pesel": "05210700056"
        }
        requests.post(url, json=payload)
        payload = {
            "first_name": "Jan",
            "last_name": "Kowalski",
            "pesel": "05210700099"
        }
        requests.post(url, json=payload)

        url2 = f"{self.url}/api/accounts/save"
        requests.post(url2, json=payload)
        url3 = f"{self.url}/api/accounts/clear"
        requests.post(url3)
        url4 = f"{self.url}/api/accounts/load"
        requests.post(url4)
        url5 = f"{self.url}/api/accounts"
        response = requests.get(url5)
        assert len(response.json()) == 2 and response.status_code == 200
        
    def test_the_same_like_the_above_but_without_saving(self):
        requests.post(f"{self.url}/api/accounts/clear")
        MongoAccountsRepository().collection.delete_many({})

        url = f"{self.url}/api/accounts"
        payload = {
            "first_name": "Marcin",
            "last_name": "Dykowski",
            "pesel": "05210700056"
        }
        requests.post(url, json=payload)
        payload = {
            "first_name": "Jan",
            "last_name": "Kowalski",
            "pesel": "05210700099"
        }
        requests.post(url, json=payload)

        url3 = f"{self.url}/api/accounts/clear"
        requests.post(url3)
        url4 = f"{self.url}/api/accounts/load"
        requests.post(url4)
        url5 = f"{self.url}/api/accounts"
        response = requests.get(url5)
        assert len(response.json()) == 0 and response.status_code == 200