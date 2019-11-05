def split_csv(file): 
    newFile = []
    for row in file.splitlines(): 
        newFile.append(split_row_3(row))
    return newFile

def split_csv2(string): 
    return [strip_quotes(row).split(',') for row in string.splitlines()]

import re 

def strip_quotes(string):
    strip_regex = re.compile(r"[A-Za-zs'']")
    search = strip_regex.search(string)
    if search:
        return re.sub('"', '',string)
    else:
        return string

#Bremners result 
def strip_quotes2(string):
    strip_regex = re.compile(r'"?([^"]+)"?')
    search = strip_regex.search(string)
    if search: 
        return search.group(1)
    else: 
        return None


def split_row_3(string):
    split_regex=re.compile(
        r'''^   # start
        ("[^"]*"|[^,]+)     #first column 
        , 
        ("[^"]*"|[^,]+)    #Second column
        , 
        ("[^"]*"|[^,]+)     #third column 
        $''', re.VERBOSE)
    search = split_regex.search(string)
    if search:
        return [ strip_quotes(col) for col in search.groups() ]
    else:
        return None

