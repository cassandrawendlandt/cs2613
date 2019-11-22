from assignmnent5 import Scanner,Type

'''
Question 4:Creating a ledger 

Takes in a string from the user and returns the final values of the accounts

Throws an ValueError if the begining token is not of type OPEN,TRANSFER, BALANCE

The methods assumes the user will enter the right number of arguments for each call
'''
def ledger(userInput): 
    
    if (userInput == ""): 
        return []
    else: 
        valueDic = {} 
        tokenList = [] 
        ScannerValues = Scanner(userInput)
        for tok in ScannerValues : 
            tokenList.append(tok)
        i = 0
        while (i < len(tokenList)):
            if (tokenList[i].type == Type.OPEN): 
                if (tokenList[i+1].type  == Type.IDENT ): 
                    if (tokenList[i+2].type == Type.CURRENCY): 
                        valueDic[tokenList[i+1].value] = tokenList[i+2].value
                        i = i +3
                    else: 
                        valueDic[tokenList[i+1].value] = 0
                        i = i+2

            elif (tokenList[i]. type == Type.TRANSFER):
                accFrom = tokenList[i+1].value
                accTo =tokenList[i+2].value
                value= (float)(tokenList[i+3].value)
                valueDic[accFrom] = valueDic[accFrom] - value
                valueDic[accTo] = valueDic[accTo] + value
                print (valueDic[accFrom] , accFrom)
                print (valueDic[accTo], accTo)
                i = i+4

            elif (tokenList[i].type == Type.BALANCE):
                if (tokenList[i+1].value not in valueDic.keys() ): 
                    yield (tokenList[i+1].value,0)
                else : 
                    yield (tokenList[i+1].value,valueDic[tokenList[i+1].value])
                i= i+2
            else :
                print (tokenList[i])
                raise ValueError("Unexpected Token")
            
                      
            
        