import pytest
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')
        self.a2 = Account('Jane')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a2.get_name() == 'Jane'
        assert self.a1.get_balance() == 0
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(20) is True
        assert self.a1.deposit(0) is False
        assert self.a1.deposit(20.5) is True
        assert self.a1.deposit(-8) is False

        assert self.a2.deposit(20) is True
        assert self.a2.deposit(0) is False
        assert self.a2.deposit(20.5) is True
        assert self.a2.deposit(-8) is False

    def test_withdraw(self):
        self.a1.deposit(20)
        assert self.a1.withdraw(2) is True
        assert self.a1.withdraw(0) is False
        assert self.a1.withdraw(1.5) is True
        assert self.a1.withdraw(100) is False
        assert self.a1.withdraw(-8) is False

        self.a2.deposit(20)
        assert self.a2.withdraw(2) is True
        assert self.a2.withdraw(0) is False
        assert self.a2.withdraw(1.5) is True
        assert self.a2.withdraw(100) is False
        assert self.a2.withdraw(-8) is False
