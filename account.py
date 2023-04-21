class Account:
    def __init__(self, name: str) -> None:
        '''
        Function to set up object
        :param name: Account name
        '''
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Function to deposit an amount to account balance
        :param amount: amount wanted to deposit
        :return: boolean value on rather or not the account balance was changed
        '''
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        '''
        Function to withdraw an amount from the account balance
        :param amount: amount wanted to withdraw
        :return: boolean value on rather or not the account balance was changed
        '''
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        '''
        Function to access the account balance
        :return: The balance of the account
        '''
        return self.account_balance

    def get_name(self) -> str:
        '''
        Function to access the account name
        :return: The name of the account
        '''
        return self.account_name
