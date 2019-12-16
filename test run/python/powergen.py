def powergen(n):
    count = 0
    while True: 
        result = n**count 
        count = count +1
        yield result 




