import itertools
import copy
from collections import Counter

# Below represents (v1 ∨ ¬v2) ∧ (¬v1 ∨ v3)
clauses = [[1, -2], [-1, 3]]


def simple_sat_solve(clause_set):
    if len(clause_set) == 0:
        return True

    # Determine number of variables
    variables = unique_values(clause_set)
    n = len(variables)
    #print(variables)

    # Generate truth table orderings of combinations to test
    truth_table = list(itertools.product([False, True], repeat=n))
    #print(truth_table)

    # Iterate through all rows of the generated Truth table, replacing each unique variable with T or F
    i = 0
    while i < len(truth_table):
        expression = copy.deepcopy(clause_set)
        print(truth_table[i])
        # Inside this we want to make a list in `expression` that replaces the values with T and F

        # Store dictionary of {unique variable : boolean value}
        variable_values = dict(zip(variables, truth_table[i]))
        print(variable_values)

        for clause in expression:
            pass

            # Deal with -ve values here

            # Replace Values in a List using Lambda Function
            #clause = list(map(lambda x: True, clause))
            #print(clause)


            # replace 1, 2, 3 with corresponding truth value
            # Basically replicate this:
            # replace Pant with Ishan
            # l = list(map(lambda x: x.replace('Pant', 'Ishan'), l))
            # so probably a dictionary would be best here

        i += 1

    print(clause_set)

    return "End of function"


# Determine number of unique values in the clause set
def unique_values(clause_set):
    # Generate list of clauses without negations
    less_negations = copy.deepcopy(clause_set)
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
