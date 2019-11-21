def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x = x + 1

def make_counter2(x):
    count = x
    def counter():
        nonlocal count,x
        if count ==x: 
            print ('Entering make_counter')
        x = x+1
        return x-1
    return counter