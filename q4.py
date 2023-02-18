import sys
import os

clause_set = []

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
sat_list = data.split("\n")
f.close()

print(sat_list)

# Parse each line of DIMACS file as CNF

i = 0
while i < len(sat_list):
    # Ignore non-comment lines
    if sat_list[i][0] == "c":
        i += 1
        continue
    # Ignore problem line
    if sat_list[i][0] == "p":
        i += 1
        continue

    # Split SAT line by space
    print("i: " + str(i))
    expression = sat_list[i].split()
    print(expression)

    # If a 0 is at the end of a line the expression is not finished, so read the next line
    while expression[-1] != "0":
        i += 1
        expression += sat_list[i].split()
        print(expression)
        if expression[-1] == "0":
            break

    # Remove end 0 and append to clause set
    expression.pop()
    clause_set.append(expression)

    i += 1

print("Output clause set: " + str(clause_set))
