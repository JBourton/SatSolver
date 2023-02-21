import itertools
import copy
import numpy as np
from collections import Counter

# Below represents (v1 ∨ ¬v2) ∧ (¬v1 ∨ v3)
# clauses = [[1, -2], [-1, 3]]
clauses = [1, -2, 3]


def simple_sat_solve(clause_set):
    if len(clause_set) == 0:
        return True

    # Convert lines containing a single clause into a 2d list
    clause_set_format = copy.deepcopy(clause_set)
    check = 0
    while check < len(clause_set_format):
        if not isinstance(clause_set_format[check], list):
            clause_set_format = np.array(clause_set_format).reshape(len(clause_set_format), 1).tolist()
            break
        check += 1

    # Determine number of variables
    variables = unique_values(clause_set_format)
    n = len(variables)

    # Generate truth table orderings of combinations to test
    truth_table = list(itertools.product([False, True], repeat=n))

    # Iterate through all rows of the generated Truth table, replacing each unique variable with T or F
    i = 0
    while i < len(truth_table):
        expression = copy.deepcopy(clause_set_format)

        # Store dictionary of {unique variable : boolean value}
        variable_values = dict(zip(variables, truth_table[i]))
        # print(variable_values)

        # Replace integers with boolean values
        for clause in expression:
            # print(clause)
            k = 0
            while k < len(clause):
                variable = clause[k]
                if variable < 0:
                    variable = not (variable_values[abs(variable)])
                else:
                    variable = (variable_values[abs(variable)])

                clause[k] = variable
                k += 1

        # If the disjunctive doesn't contain at least one True value, the expression cannot be satisfied
        satisfiable = True
        elem = 0
        while elem < len(expression) and satisfiable:
            if expression[elem].count(True) < 1:
                satisfiable = False
            elem += 1

        if satisfiable:
            print("Expression " + str(clause_set) + " is satisfiable with the following boolean values: ")
            return truth_table[i]

        # print(expression)
        i += 1

    return "Expression " + str(clause_set) + " is unsatisfiable"


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
