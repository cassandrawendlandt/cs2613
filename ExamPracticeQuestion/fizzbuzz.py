class FizzBuzz:
    def __init__(self, max=100):
        self.n=1; self.max=max

    def __iter__(self): 
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max: 
            value = self.n
            if (self.n%3 ==0 and self.n%5 ==0): 
                value = "FizzBuzz"
            elif (self.n%3 == 0): 
                value = "Fizz"
            elif (self.n%5 == 0): 
                value = "Buzz"
            self.n = self.n +1
            return value 
        else :  
            raise StopIteration