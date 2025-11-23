from src.Comany_Account import CompanyAccount

class Test_company_acount():

    def test_firm_account_incorect_NIP(self):
        account = CompanyAccount("BANK_13", "1234567890000")
        assert account.nip == "Invalid"
    
    def test_Company_accout_Correct_NIP(self):
        account = CompanyAccount("BANK_13", "1234567890")
        assert account.nip == "1234567890"       