class ArithSeq : 
    def __init__ (self, start,step,end): 
        self.start = start
        self.step = step 
        self.end = end 
        self.position = start 
    def __iter__(self): 
        self.position = self.start 
        return self
    def __next__(self): 
        if self.position <= self.end: 
            value = self.position 
            self.position = self.step + self.position
            return value 
        else: 
            raise StopIteration