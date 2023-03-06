def branching_sat_solve(partial_assignment, clause_set):
    # If clause set contains empty clauses, UNSAT
    if [] in clause_set:
        return False
    # If clause_set contains no clauses, SAT;
    if not clause_set:
        return partial_assignment


# Inputs
clauses = [[1, -2], [-1, 3]]
# clauses = [[], [4, 5]]
partial_assign = [[]]
print(branching_sat_solve(clauses, partial_assign))
