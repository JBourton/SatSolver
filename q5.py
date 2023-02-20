import itertools
from collections import Counter

# Below represents (v1 ∨ ¬v2) ∧ (¬v1 ∨ v3)
clauses = [[1, -2], [-1, 3]]


def simple_sat_solve(clause_set):
    pass

    # Determine number of variables
    print(unique_values(unique_values(clause_set)))

    n = len(unique_values())

    allorderings = list(itertools.product([False, True], repeat=n))
    return allorderings


# Determine number of unique values in the clause set
def unique_values(clause_set):
    # Generate list of clauses without negations
    less_negations = clause_set
    value = 0
    while value < len(less_negations):
        subvalue = 0
        while subvalue < len(less_negations[value]):
            if less_negations[value][subvalue] < 0:
                less_negations[value][subvalue] = abs(less_negations[value][subvalue])
            subvalue += 1
        value += 1

    # Generate list of unique values
    uniqueVals = list(set(itertools.chain(*less_negations)))
    return uniqueVals


result = simple_sat_solve(clauses)
print(result)
