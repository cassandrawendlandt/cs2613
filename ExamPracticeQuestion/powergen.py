def powergen(x):
    n = 0 
    results =0
    while True:
        results = x**n
        n = n+1
        yield results

   
        