from readCsv import read_csv, check_row,filter_table,header_map,select,row2dict

'''
Question 1: reading the csv file in. 

this checks to see if the function will read in the file properly.
'''
def test_read_csv():
    assert read_csv('test1.csv') == [['name', 'age', 'eye colour'],
                                     ['Bob', '5', 'blue'],
                                     ['Mary', '27', 'brown'],
                                     ['Vij', '54', 'green']]

'''
Question 1: reading the csv file in.

this test is to make sure an empty file will return an empty list.
'''
def test_read_csv_empty():
    assert read_csv('hello.csv') == []

#creates a copy of the table that can be used throughout the tests
table = read_csv('test1.csv')
table2 = read_csv ('dataFile.csv')

'''
Question 2: Parsing the headers.

Test to see if the function creates dictionary with the row passed in the row becomes the keys and the index becomes the value.
'''
def test_header_map_1():
    hmap = header_map(table[0])
    assert hmap == { 'name': 0, 'age': 1, 'eye colour': 2 }

'''
Question 2: Parsing the headers.

test to see if the function will return a list of headers for a different set of data.
'''
def test_header_map_2():
    hmap = header_map(table2[0])
    assert hmap == { 'UNITID':0, 'OPEID':1, 'OPEID6':2, 'INSTNM':3, 'CITY':4, 'STABBR':5, 'ZIP':6 }

'''
Question 3: Selecting Column.

This test to see if the function will return the proper columns.
'''
def test_select_1():
    assert select(table,{'name','eye colour'}) == [['name', 'eye colour'],
                                                   ['Bob',  'blue'],
                                                   ['Mary', 'brown'],
                                                   ['Vij',  'green']]

'''
Question 3: Selecting Column.

this test to see if the function will return an empty list if the user enters an element that is not a header.
'''                                    
def test_select_2():
    assert select(table,{'height'}) == []

'''
Question 3: Selecting Column.

this test to see if the function will return a list containing only they values in the header when the user enters a field that is in the header and a field that is not in the header.
'''                                    
def test_select_3():
    assert select(table,{'height','name'}) == [['name'],
                                                   ['Bob'],
                                                   ['Mary'],
                                                   ['Vij']]

'''
Question 4: Transforming rows into dictionaries.

This test takes the header dictoriary and replace the values with the the values at that index from the row that is passed in.
'''
def test_row2dict():
    hmap = header_map(table[0])
    assert row2dict(hmap, table[1]) == {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}

'''
Question 4: Transforming rows into dictionaries.

This is to check if it will return the proper values when the row from the middle if the file is sent as a parameter.
'''
def test_row2dict_2():
    hmap = header_map(table2[0])
    assert row2dict(hmap,table2[8]) == { 'UNITID':'100812', 'OPEID':'100800', 
                                            'OPEID6':'1008', 'INSTNM':'Athens State University',
                                            'CITY':'Athens', 'STABBR':'AL', 'ZIP':'35611' }

'''
Question 5: Matching rows.

this checks if given a row and a conditional statement will return the correct boolean answer. 
'''
def test_check_row():
    row = {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}
    assert check_row(row, ('age', '==', 5))
    assert not check_row(row, ('eye colour', '==', 5))
    assert check_row(row, ('eye colour', '==', 'blue'))
    assert check_row(row, ('age', '>=', 4))
    assert check_row(row, ('age', '<=', 1000))

'''
Question 5: Matching rows.

this test to see if the function will return false while using > or < with a string comparison.
'''
def test_check_row2():
    row = {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}
    assert not check_row(row, ('eye colour', '>=' 'purle'))
    assert not check_row(row, ('age', '<=' 'yellow'))

'''
Question 6: Extending the query language.

This checks to see if the funtion will return true with an or given a true and a false an and return false when it is given a true and false expression.
'''
def test_check_row_logical():
    row = {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}
    assert check_row(row, (('age', '==', 5),'OR',('eye colour', '==', 5)))
    assert not check_row(row, (('age', '==', 5),'AND',('eye colour', '==', 5)))

'''
Question 6: Extending the query language.

This test case checks to see the function will return the correct values for different cases.

And cases: both false, both true. 

Or cases: both false, both true. 
'''
def test_check_row_logical_2():
    row = {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}
    assert not check_row(row, (('age', '==', 10),'OR',('eye colour', '==', 5)))
    assert check_row(row, (('age', '==', 5),'OR',('name', '==', 'Bob')))
    assert not check_row(row, (('age', '==', 50),'AND',('eye colour', '==', 5)))
    assert check_row(row, (('age', '==', 5),'AND',('eye colour', '==', 'blue')))

'''
Question 7: Filtering Tables. 

This test to see if given a table and a conditional statement if it return all the rows that fit the conditional as well as the headers.
'''
def test_filter_table1():
    assert filter_table(table,('age', '>=', 0)) == [['name', 'age', 'eye colour'],
                                                    ['Bob', '5', 'blue'],
                                                    ['Mary', '27', 'brown'],
                                                    ['Vij', '54', 'green']]

    assert filter_table(table,('age', '<=', 27)) == [['name', 'age', 'eye colour'],
                                                     ['Bob', '5', 'blue'],
                                                     ['Mary', '27', 'brown']]

    assert filter_table(table,('eye colour', '==', 'brown')) == [['name', 'age', 'eye colour'],
                                                                 ['Mary', '27', 'brown']]

    assert filter_table(table,('name', '==', 'Vij')) == [['name', 'age', 'eye colour'],
                                                         ['Vij', '54', 'green']]

'''
Question 7: Filtering Tables. 

This test to seee if the filtering tables function can handle and/or's statements. 
'''
def test_filter_table2():
    assert filter_table(table,(('age', '>=', 0),'AND',('age','>=','27'))) == [['name', 'age', 'eye colour'],
                                                                              ['Mary', '27', 'brown'],
                                                                              ['Vij', '54', 'green']]


    assert filter_table(table,(('age', '<=', 27),'AND',('age','>=','27'))) == [['name', 'age', 'eye colour'],
                                                                               ['Mary', '27', 'brown']]

    assert filter_table(table,(('eye colour', '==', 'brown'),
                               'OR',
                               ('name','==','Vij'))) == [['name', 'age', 'eye colour'],
                                                        ['Mary', '27', 'brown'],
                                                        ['Vij', '54', 'green']]

'''
Question 7: Filtering Tables 

This test to see if a query returns false then the function will return an empty list. 
'''
def test_filter_table_1_1():
    assert filter_table(table2,('age', '>=', 0)) == []
