class Account:

    def getting_money(self, ammout):
        if (isinstance(ammout, int) == True or isinstance(ammout, float) == True):
            self.balance += ammout

    def outgoing_transer(self, ammout):
        if (ammout < self.balance and ammout > 0):
            self.balance -= ammout

    def fast_outgoing_transfer(self, ammout):
        if hasattr(self, "company_name") and self.balance - ammout -5 >= -5:
            self.balance -= ammout + 5
        elif hasattr(self, "first_name") and self.balance - ammout - 1 >= -1:
            self.balance -= ammout + 1