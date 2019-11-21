from assignmnent5 import Type, Token,Scanner
import pytest

'''
Question  3.1 
This test to see if the Types are in the ENUM class. 
'''
def test_enum():
    '''check that defined enum type matches assignment'''
    assert sorted([ member.name for member in Type ]) == ["BALANCE", "CURRENCY", 
                                                        "IDENT", "OPEN", "TRANSFER"]

'''
This test checks to make sure the types are case sensitive 
'''
def test_enum2():
    '''check that defined enum type matches assignment'''
    assert sorted([ member.name for member in Type ]) != ["balance", "cURRENCY", 
                                                        "ident", "OPeN", "transfer"]
''' 
Question 3.2
this test cases test to make sure the token objects are being created correctly
'''
def test_token():
    token=Token(Type.IDENT,"hello")
    assert token.type==Type.IDENT
    assert token.value=="hello"

def test_token_BALANCE():
    token=Token(Type.BALANCE,"cash")
    assert token.type==Type.BALANCE
    assert token.value=="cash"

def test_token_TRANSFER():
    token=Token(Type.TRANSFER,"savings")
    assert token.type==Type.TRANSFER
    assert token.value=="savings"

'''
Tests for question 3.2 
Make sures the Token will return the correct string 
'''
def test_str():
    id=Token(Type.IDENT,"hello")
    assert str(id) == '[IDENT: hello]'
    money=Token(Type.CURRENCY,10042)
    assert str(money) == '[CURRENCY: 100.42]'

def test_str_2():
    id=Token(Type.BALANCE,"poor")
    assert str(id) == '[BALANCE: poor]'
    money=Token(Type.CURRENCY,-10000)
    assert str(money) == '[CURRENCY: -100.0]'

'''
Tests for question 3.2.1
These test make sure that the equals method will return the proper answer
Test Type IDENT to see if the values are the same (case sensitive)
Test Type CURRENCY to compare the values 
Compare the other Types based on the keywords and the values but the values are not case sensitive 
'''
def test_equal_ident():
    assert Token(Type.IDENT,"Bob") == Token(Type.IDENT,"Bob")
    assert Token(Type.IDENT,"Bob") != Token(Type.IDENT,"bOb")

def test_equal_currency():
    assert Token(Type.CURRENCY,1000) == Token(Type.CURRENCY,1000)
    assert Token(Type.CURRENCY,1000) != Token(Type.CURRENCY,1001)

def test_equal_currency_2():
    assert Token(Type.CURRENCY,1000) != Token(Type.IDENT,10.0)
    assert Token(Type.IDENT,10.01) != Token(Type.CURRENCY,1001)

def test_equal_keywords():
    assert Token(Type.TRANSFER,"transfer") != Token(Type.OPEN,"open")
    assert Token(Type.OPEN,"OPEN") == Token(Type.OPEN,"open")
    assert Token(Type.BALANCE,"BALANCE") == Token(Type.BALANCE,"balance") 

def test_equal_keywords_2():
    assert Token(Type.TRANSFER,"transfer") != Token(Type.OPEN,"open")
    assert Token(Type.OPEN,"OPEN") != Token(Type.BALANCE,"open")
    assert Token(Type.OPEN,"BALANCE") != Token(Type.BALANCE,"balance") 

'''
Tests for 3.3
Test that the scanner will read the input then return the current token items 
Test to make sure that the scanner does not change the object 
Test to see if what is passed in is a memeber of Type. If it is then return a token of that type 
If the input is not a member of type or number then returns a token of type IDENT and the input as the value
'''
def test_scan_keywords():
    scanner=Scanner('''TrAnsFer transfer 
                       OPEN BALANCE balance''')
    toks = [Token(Type.TRANSFER,"TrAnsFer"), Token(Type.TRANSFER,"transfer"),
            Token(Type.OPEN,"OPEN"),
            Token(Type.BALANCE,"BALANCE"),  Token(Type.BALANCE,"balance")]

    assert [tok for tok in scanner] == toks
    # iterate a second time
    assert [tok for tok in scanner] == toks

def test_scan_identifiers():
    scanner=Scanner("equity cash end_of_the_world_fund")
    assert list(scanner) == [Token(Type.IDENT,"equity"),
                                        Token(Type.IDENT,"cash"),
                                        Token(Type.IDENT,"end_of_the_world_fund")]

def test_scan_identifiers_2():
    scanner=Scanner("cash savings expenses rent bills")
    assert list(scanner) == [Token(Type.IDENT,"cash"),
                                        Token(Type.IDENT,"savings"),
                                        Token(Type.IDENT,"expenses"),
                                        Token(Type.IDENT,"rent"),
                                        Token(Type.IDENT,"bills")]

'''
Tests for 3.3.1
Test that the scanner will read the input then return the current token items 
Test to see if the input is a number then it creates a token with the type of currency 
'''
def test_scan_currency():
    scanner=Scanner("100 100.00 100.42 -123.45")
    assert list(scanner) == [Token(Type.CURRENCY,10000),
                             Token(Type.CURRENCY,10000),
                             Token(Type.CURRENCY,10042),
                             Token(Type.CURRENCY,-12345)]

def test_scan_currency_2():
    scanner=Scanner("1000 -1.0 0.5 -123.45")
    assert list(scanner) == [Token(Type.CURRENCY,100000),
                             Token(Type.CURRENCY,-100),
                             Token(Type.CURRENCY,50),
                             Token(Type.CURRENCY,-12345)]
'''
Tests for 3.3.2
Test to see if the scanner will through an ValueError if unmatched text is entered
'''
def test_scan_bad():
    scanner=Scanner("&crash")
    with pytest.raises(ValueError, match="&crash"):
        next(scanner)
        
def test_scan_bad_2():
    scanner=Scanner("&FAIL")
    with pytest.raises(ValueError, match="&FAIL"):
        next(scanner)

