import os,glob

strings_plus = []
for p in glob.glob("*.py"):
    size=os.stat(p).st_size
    strings_plus.append(p + "\t" + str(size))

print (strings_plus)

strings_format = ["{file}\t{size}".format(file = file, 
                    size = os.stat(file).st_size) for file in glob.glob("*py") ]