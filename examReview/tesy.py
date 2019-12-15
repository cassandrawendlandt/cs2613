import re 
#^ means start of the line  
# * means one or more repeats of the pervious thing 
#[^ ] . * ---wild card, looks for everthing s
regex = re.compile(r"^[\t \n]*([a-zA-Z][a-zA-Z0-9]*)")

for string in ["a123"," a123", "a"]: 
    match1 = regex.match(string)
    if match1 != None: 
        print (match1[0])