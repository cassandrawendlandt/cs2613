import sys

stack = []

def process(line):
    if line in ("+", "-", "/", "*"):
        b = stack.pop()
        a = stack.pop()
    if line == "+":
        stack.append(a+b)
    elif line == "-":
        stack.append(a-b)
    elif line == "*":
        stack.append(a*b)
    elif  line == "/":
        stack.append(a//b)
    else :
        stack.append(int(line))


def  process_list (line):
    out = []
    for lines in line: 
        if lines == "quit":
            break 
        retv = process(line)
        if retv:
            out.append(retv)
    return retv
