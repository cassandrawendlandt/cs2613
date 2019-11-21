from ledger import ledger
'''
Test question 4: 
test to see if ledger will return an empty list if nothing is inputted
'''
def test_empty():
    assert list(ledger("")) == []