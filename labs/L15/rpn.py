
import sys

stack = []

def process(line):
    if line == "+":
        num1 = stack.pop()
        stack[-1] = stack[-1]+num1

    elif line == "-":
        num1 = stack.pop()
        stack[-1] = stack[-1]-num1

    elif line == "*":
        num1 = stack.pop()
        stack[-1] = stack[-1]*num1

    elif  line == "/":
        num1 = stack.pop()
        stack[-1] = stack[-1]//num1

    elif line == "^": 
        stack[-1] = stack [-1] ** stack[-1]

    elif line == "clear":
        stack.clear()

    elif line == "dup": 
        stack.append(stack[-1])
        
    elif line == "pop":
        stack.pop()
    elif line == "swap":
        num1= stack.pop(-2)
        stack.append(num1)
    elif line == "print":
        return int(stack[-1])
    else :
        stack.append(int(line))


def  process_list (line):
    out = []
    for lines in line: 
        if lines == "quit":
            break 
        retv = process(lines)
        if retv:
            out.append(retv)
    return out

