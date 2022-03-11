import pytest
from app.calculations import BankAccount, add

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1,num2,expected",[
    (2,3,5),
    (5,11,16),
    (15,15,30)
    ])
def test_add(num1,num2,expected):
    assert add(num1,num2)==expected

def test_intial_set_to_zero(zero_bank_account):
    assert zero_bank_account.balance==0

def test_intial_set_to_fifty(bank_account):
    assert bank_account.balance==50

def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.balance==100

def test_withdrew(bank_account):
    bank_account.withdraw(50)
    assert bank_account.balance==0

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance)==55

@pytest.mark.parametrize("deposit,withdrew,expected",[
    (50,10,40),
    (100,70,30),
    (5000,500,4500)
])
def test_transactions(zero_bank_account,deposit,withdrew,expected):
    zero_bank_account.deposit(deposit)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance==expected

def test_insufficient_funds(zero_bank_account):
    with pytest.raises(Exception):
        zero_bank_account.withdraw(50)

