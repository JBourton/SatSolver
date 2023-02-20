import itertools

# Below represents (v1 ∨ ¬v2) ∧ (¬v1 ∨ v3)
clauses = [[1, -2], [-1, 3]]


def simple_sat_solve(clause_set):
    pass
    # 'split and simplify' method - try each variable in order

    # Iterate through each clause in the clause set
    i = 0
    while i < len(clause_set):
        pass


result = simple_sat_solve(clauses)
print(result)
