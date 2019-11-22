from ledger import ledger
import pytest
'''
Test question 4: 

test to see if ledger will return an empty list if nothing is inputed

Test that if balance is called and account does not exist it returns the account with 0 

Test that the ledger will return the proper values 

Test if given an value that isnt expected it will raise a value error
'''
def test_empty():
    assert list(ledger("")) == []

def test_balance():
    assert list(ledger('''
                    balance cash
                    balance stock
                    ''')) == [("cash",0),("stock",0)]

def test_open():
    assert list(ledger('''open cash 100
                        balance cash''')) == [("cash",10000)]


def test_transfer():
    assert list(ledger('''
                        open cash 100
                        open expenses 0
                        transfer cash expenses 50
                        balance cash
                        balance expenses
                        ''')) == [("cash",5000),("expenses",5000)]


def test_ledger_bad():
    ledger2=ledger("&crash")
    with pytest.raises(ValueError, match="Unexpected Token"):
        next(ledger2)


def test_ledger_bad2():
    ledger2=ledger("cash")
    with pytest.raises(ValueError, match="Unexpected Token"):
        next(ledger2)

