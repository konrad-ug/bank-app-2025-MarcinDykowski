from src.account import Account
import requests, os
from datetime import datetime
from src.smtp.smtp import SMTPClient
from datetime import datetime

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
            self.company_name = company_name
            self.balance = 0
            self.history = []
            
            if len(nip) != 10:
                self.nip = "Invalid"
            else:
                self.nip = nip
                if self.is_Nip_correct(nip):
                    self.nip = nip
                else:  
                    raise ValueError("Company not registered!!")
    def is_Nip_correct(self, NIP):
            bank_app_mf_url = os.environ.get("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl/")
            
            response = requests.get(f'{bank_app_mf_url}/#{NIP}?{datetime.now()}', timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                status = data.get('result', {}).get('subject', {}).get('statusVat')
                
                if status == "Czynny":
                    print("Company is active in the registry.")
                    return True
            print("Company is not active or not found in the registry.")
            return False
    def submit_for_loan(self, ammount):
        if self.balance > ammount*2 and -1775 in self.history:
            self.balance += ammount
            return True
        else:
            return False
    def send_history_via_email(self, email_address) -> bool:

        subject = f"Account Transfer History {datetime.now().strftime('%Y-%m-%d')}"
        text = f"Company account history: {self.history}"
        
        return SMTPClient.send(subject, text, email_address)