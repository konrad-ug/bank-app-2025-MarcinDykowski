class Account:
    def __init__(self):
        pass

    def getting_money(self, ammout):
        if (isinstance(ammout, int) == True or isinstance(ammout, float) == True):
            self.balance += ammout

    def outgoing_transer(self, ammout):
        if (ammout < self.balance and ammout > 0):
            self.balance -= ammout