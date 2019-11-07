import csv

'''
Question 1: Read CSV File.

this will take in the name of a CSV file and add it to a list.
'''
def read_csv(filename):
    arr =[]
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader: 
            arr.append(row )

    return arr

'''
Question 2: Parsing Headers.

This will take in a row and turn it into a dictionary with the index number as the values and the key is the values in the row.
'''
def header_map  (headers):
    return { headers[i] : i for i in range(0, len(headers) ) }

'''
QUestion 3: Selecting Columns. 

This will select all the coulmns where the header matches the values passed in. 
'''
def select(file, lookups):
    print (type(lookups))
    headers = header_map(file[0])
    sendBack = []
    for x in file:
        arr = []
        for i in headers: 
            if i in lookups:
                arr.append(x[headers[i]])
        if arr: 
            sendBack.append(arr)
    return sendBack

'''
Question 4: Transforming rows into dictionaries. 

takes the output from header_map, and a row, and returns a dictionary representing that row. 
'''
def row2dict (headers, row):
    rowDic = {}
    for x in headers:
        rowDic [x] = row[headers[x]]
    return rowDic

''' 
This function is for questions 5 and 6.

Question 5: Matching rows.

takes a row in dictionary form, and checks if it matches a query tuple.

Question 6: Extending the query language. 

Extend check_row so that it supports operations AND and OR.
'''
def check_row (row, check):
    if (check[1] == "OR"):
        epr1 = check_row(row, check [0])
        epr2 = check_row(row, check[2])
        return epr1 or epr2
    elif (check[1] == "AND"):
        epr1 = check_row(row, check [0])
        epr2 = check_row(row, check[2])
        return epr1 and epr2
    else :
        for x in row:
            if x == check[0]:
                if check[1] == "==":
                    return  str(check[2]) ==  row[x]
                elif check[1] == ">=":
                    return int (check[2] )<= int(row[x])
                elif check[1] == "<=": 
                    return int (check[2]) >= int(row[x])
                    
'''
Question 7: Filtering tables.

selects certain rows of the table according to a query.
'''
def filter_table(table, check): 
    headers = header_map(table[0])
    newTable = []
    newTable.append(table[0])
    for x in table [1:]: 
        row = row2dict(headers,x)
        if check_row(row,check):
            newTable.append(x)
    if len(newTable) == 1: 
        return []
    return (newTable)
