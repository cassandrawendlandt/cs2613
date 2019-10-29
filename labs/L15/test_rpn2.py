from rpn2 import process, stack,process_list



def test_push():
    process("1")
    process("2")
    assert stack == [1,2]

def test_plus():
    process("+")
    assert stack == [3]


def test_minus():
    process("1")
    process("-")
    assert stack == [2]

def test_mult():
    process("2")
    process("*")
    assert stack == [4]

def test_div():
    process("2")
    process("/")
    assert stack == [2]


def test_list_plus():
    ops ='clear 3 4 + print'.split()
    assert process_list(ops) == [7]

def test_list_mult():
    ops ='clear 3 4 * print'.split()
    assert process_list(ops) == [12]

def test_list_combo():
    ops ='clear 3 4 * print 2 + print'.split()
    assert process_list(ops) == [12,14]

