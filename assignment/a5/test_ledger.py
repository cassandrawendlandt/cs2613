from ledger import ledger
import pytest
'''
Test question 4: 

The ledger method assumes user will enter right number of arguments for each call

test to see if ledger will return an empty list if nothing is inputed

Test if balance is called and account doesn't exist returns the account with 0 

Test that the ledger will return the proper values 
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
def test_transfer_2():
    assert list(ledger('''
                        open cash 100
                        open expenses 0
                        transfer cash expenses 50
                        balance cash
                        balance expenses
                        transfer expenses cash 50
                        balance cash
                        balance expenses
                        ''')) == [("cash",5000),("expenses",5000),("cash",10000),("expenses",0.0)]

'''
test to see if ledger will return a negative if transfered more than they have
'''
def test_transfer_3():
    assert list(ledger('''
                        open cash 100
                        open expenses 0
                        transfer cash expenses 200
                        balance cash
                        balance expenses
                        ''')) == [("cash",-10000),("expenses",20000)]
'''
This tests to see if the balance will print out other accounts 
'''
def test_transfer_4():
    assert list(ledger('''
                        open cash 100
                        open expenses 0
                        open rent 0
                        transfer cash rent 200
                        balance cash
                        balance expenses
                        balance rent
                        ''')) == [("cash",-10000),("expenses",0.0),("rent",20000)]

'''
Test if given an value that isnt expected it will raise a value error
'''
def test_ledger_ValueError():
    ledger2=ledger("&crash")
    with pytest.raises(ValueError, match="Unexpected Token"):
        next(ledger2)


def test_ledger_ValueError_2():
    ledger2=ledger("cash")
    with pytest.raises(ValueError, match="Unexpected Token"):
        next(ledger2)

