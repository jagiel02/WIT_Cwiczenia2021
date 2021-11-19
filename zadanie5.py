class BankCard:
    def __init__(self, owner, number, provider):
            self.owner = owner
            self.number = number
            self.provider = provider

    def get_number(self):
        print('numer')

    def get_owner(self):
        print('owner')

    def get_provider(self):
        print('provider')


BankCard1 = BankCard('ja', '1234', 'bank')


class BankAccount:
    def __init__(self, owner, balance, bank, balance2):
        self.owner = owner
        self.balance = balance
        self.bank = bank
        self.balance2 = balance2

    def get_owner(self):
        print('owner')

    def get_balance(self):
        print('balance')

    def get_bank(self):
        print('bank')

    def set_balance(self):
        print('balance')

BankAccount1 = BankAccount('a', 'b', 'c', 'd')


class Bank:
    def __init__(self, balance, history):
        self.balance = balance
        self.payments_history = history

    def get_balance(self):
        print('get balance')

    def set_balance(self):
        print('set balance')

    def payments_history(self):
        print('payments history')


class CreditCard(BankCard):
    def __init__(self, owner, number, provider, balance, payments_history):
        super().__init__(owner, number, provider)
        self.balance = balance
        self.payments_history = payments_history


    def get_balance(self):
        print('get balance')
    def set_balance(self):
        print('set_balance')
    def get_payments_history(self):
        print('payments history')

#credit = CreditCard("1", "2", "3", "4", "5")



class PremiumBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, balance2, finacial_manager):
        super().__init__(owner, balance, bank, balance2)
        self.finacial_manager = finacial_manager

    def get_finacial_manager(self):
        print ('finacial manager')

    def set_finacial_manager(self):
        print('finacial manager2')


PremiumBankAccount1 = PremiumBankAccount('1', '2', '3', '4', '5')


class StudentBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, balance2, overdraft_balance, overdraft_limit):
        super().__init__(owner, balance, bank, balance2)
        self.overdraft_balance = overdraft_balance
        self.overdraft_limit = overdraft_limit

    def get_overdraft_balance():
        print('get_overdraft_balance')
    def set_overdraft_balance():
        print('set_overdraft_balance')
    def get_overdraft_limit():
        print('get_overdraft_limit')
    def set_overdraft_limit():
        print('set_overdraft_limit')

StudentBankAccount1 = StudentBankAccount("1", "2", "3", "4", "5", "6")



