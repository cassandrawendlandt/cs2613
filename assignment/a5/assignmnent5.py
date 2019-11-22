import re
from enum import Enum 

'''
Question 3.1 Using Enum 

This class is used to classify the tokens
'''
class Type(Enum): 
    BALANCE =1 
    CURRENCY = 2
    IDENT  = 3 
    OPEN = 4 
    TRANSFER =5

'''
Question 3.2 Creating a token object with a type and value 

__str__ returns the token to be printed out

Question 3.2.1 creates a method to compare two token objects. 

If the type is currency it compares the number 

If the type is IDENT it will compare based on the value, this is case sensitive 

compare the type and the value, the values are not case sensitive 
'''
class Token: 
    def __init__ (self, type, value): 
        self.type = type
        self.value = value
        

    def __str__ (self):
        if (self.type == Type.CURRENCY): 
            return "[CURRENCY: %s]" %( ((float)(self.value)/100))
        else: 
            return "[%s: %s]" %(self.type.name, self.value)


    def __eq__ (self, other): 
        if (other == []): 
            return False      
        elif isinstance(other, list):
            if (self.type == Type.IDENT or self.type == Type.CURRENCY):
                return self.value == other[0].value
            else:
                return self.type == other[0].type and self.value.upper() == other[0].value.upper()
        elif isinstance(other, Token):
            if (self.type == Type.IDENT or self.type == Type.CURRENCY):
                return self.value == other.value
            else:
                return self.type == other.type and self.value.upper() == other.value.upper()
        
           
'''
Question 3.3 Creates the scanner as an interator class
'''
class Scanner:
    def __init__(self, seq):
        self.data= seq.split()
        self.pos= -1
        self.tokens = []

        for i in self.data:
            s = i.upper()
            if (re.match('^[-+]?[0-9]*?[.]?[0-9]+$',i)  == None):
                if (s in Type.__members__):
                    tok = Token(Type[s],i)
                    self.tokens.append(tok)
                else:
                    tok = Token(Type.IDENT,i)

                    self.tokens.append(tok)
            else:
                tok = Token(Type.CURRENCY,(float)(i)*100)
                self.tokens.append(tok)

    def __iter__(self):
        return iter(self.tokens)

    def __next__(self):
        self.pos =self.pos+1
        if self.pos < len(self.data):
            if (re.search('^([-+]?[0-9]?[a-z]?[A-Z])+$',self.data[self.pos]) == None): 
                raise ValueError (self.data[self.pos])
            else :
                return self.tokens[self.pos]
        else :
            raise StopIteration
        

