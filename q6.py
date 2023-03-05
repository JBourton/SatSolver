def branching_sat_solve(clause_set, partial_assignment):
    # If clause_set contains no clauses it is SAT; if it contains empty clauses, UNSAT
    if clause_set == []:
        pass

