import sys
import os
path = os.getcwd()
print(path)


# Take url as input and read associated DIMACS file
url = None
try:
    url = input("Enter url of DIMACS file: ")
    if not url:
        raise ValueError('Invalid URL: Program terminated')
except ValueError as e:
    sys.exit(e)

f = open(url, "r")
data = f.read()
data_list = data.split("\n")
f.close()







