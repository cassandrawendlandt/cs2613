class ArithSeq: 
    
    def __init__(self,start,step,end): 
        self.start = start 
        self.position = start
        self.step = step 
        self.end = end 

    def __iter__(self): 
        return self

    def __next__(self):
        if self.position <= self.end : 
            value = self. position 
            self.position = self.position + self.step
            return value
        else :  
            raise StopIteration