from arithseq import ArithSeq

def test_evens():
    assert [ x for x in ArithSeq(0,2,10) ] == [0,2,4,6,8,10]

def test_odds():
    assert [ x for x in ArithSeq(1,2,10) ] == [1,3,5,7,9]



#I am testing to make sure the solution can go up by decmail numbers
#and not just integers. 

#these arent covered in the test povided because the number only go uo 
#by whole numbers 
def test_demials(): 
    assert [ x for x in ArithSeq(1,0.5,3) ] == [1,1.5,2,2.5,3]

