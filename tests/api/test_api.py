import pytest
import requests

class TestAPI:
    url = "http://127.0.0.1:5000/api"

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
            # assert response_delete.status_code == 200

    def test_create_account(self):
        url = f"{self.url}/accounts"
        payload = {
            "first_name": "Marcin",
            "last_name": "Dykowski",
            "pesel": "05210700056"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 200

    def test_create_account_2(self):
        url = f"{self.url}/accounts"
        payload = {
            "first_name": "Jan",
            "last_name": "Dykowski",
            "pesel": "05210700056"
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        print(response.json())

    def test_delete_account(self):
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
        assert response_2.status_code == 200

    def test_update_account(self):
        # creating account
        url = f"{self.url}/accounts"
        payload = {
            "first_name": "Rafał",
            "last_name": "Sobieraj",
            "pesel": "05210700056"
        }
        response = requests.post(url, json=payload)
        #update account
        payload_update = {
        "first_name": "Piotr",
        "last_name": "Wiejski"
        }
        url_update = f"{self.url}/accounts/05210700056"
        response_2 = requests.patch(url_update, json=payload)
        assert response_2.status_code == 200

    #finding pesel
    def test_search_account(self):
        # creating account
        url = f"{self.url}/accounts"
        payload = {
            "first_name": "Rafał",
            "last_name": "Sobieraj",
            "pesel": "05210700056"
        }
        response = requests.post(url, json=payload)
        # searching
        url_search = f"{self.url}/accounts/05210700056"
        response_2 = requests.get(url_search)
        assert response_2.status_code == 200

    def test_search_nonexisting_account(self):
        # creating account
        url = f"{self.url}/accounts"
        payload = {
            "first_name": "Rafał",
            "last_name": "Sobieraj",
            "pesel": "05210700056"
        }
        response = requests.post(url, json=payload)
        # searching
        url_search = f"{self.url}/accounts/55210700056"
        response_2 = requests.get(url_search)
        assert response_2.status_code == 404

    def test_adding_two_accounts_with_the_same_pesel(self):
        # creating account
        url = f"{self.url}/accounts"
        payload = {
            "first_name": "Rafał",
            "last_name": "Sobieraj",
            "pesel": "05210700056"
        }
        response_1 = requests.post(url, json=payload)

        # creating account 2(the same Pesel)
        url = f"{self.url}/accounts"
        payload = {
            "first_name": "Jan",
            "last_name": "Nowak",
            "pesel": "05210700056"
        }
        response_2 = requests.post(url, json=payload)
        assert response_2.status_code == 409