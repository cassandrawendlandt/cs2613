class FizzBuzz:
    def __init__(self, max=100):
        self.n=1; self.max=max

    def __next__(self):
        if self.n <=self.max:
            value = self.n 
            self.n = self.n +1
            if (value % 3 ==0 and value%5 == 0): 
                value = "FizzBuzz"
            elif (value%3==0): 
                value = "Fizz"
            elif(value%5 ==0): 
                value ="Buzz"
            return value
        else: 
            raise StopIteration

    def __iter__(self):
        self.n =1 
        return self


