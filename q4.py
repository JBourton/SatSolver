import sys
import os

path = os.getcwd()
print(path)


def load_dimacs():
    clause_set = []
    # Take url as input and read associated DIMACS file
    url = None
    try:
        url = input("Enter url of DIMACS file (including .txt extension): ")
        if not url:
            raise ValueError('Invalid URL: Program terminated')
    except ValueError as e:
        sys.exit(e)

    url = path + url
    print(url)

    f = open(url, "r")
    data = f.read()
    sat_list = data.split("\n")
    f.close()

    # Parse each line of DIMACS file as CNF
    i = 0
    while i < len(sat_list) - 1:
        # Ignore non-comment lines
        if sat_list[i][0] == "c":
            i += 1
            continue
        # Ignore problem line
        if sat_list[i][0] == "p":
            i += 1
            continue

        # Split SAT line by space
        expression = sat_list[i].split()

        # If a 0 is at the end of a line the expression is not finished, so read the next line
        while expression[-1] != "0":
            i += 1
            expression += sat_list[i].split()
            if expression[-1] == "0":
                break

        # Remove end 0 and append to clause set
        expression.pop()
        clause_set.append(expression)

        i += 1

    return clause_set


clauses = load_dimacs()
print("Output clause set: " + str(clauses))