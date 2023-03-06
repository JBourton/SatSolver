def branching_sat_solve(partial_assignment, clause_set):
    # If clause set contains empty clauses, UNSAT
    if [] in clause_set:
        return False
    # If clause_set contains no clauses, SAT;
    if not clause_set:
        return partial_assignment

    # Select a variable to eliminate
    chosen_literal = abs(clause_set[0][0])
    partial_assignment.append(chosen_literal)

    # TODO: issue here is the we initialise a for i = 1 to n but then alter the value of n
    for clause in clause_set:
        # print(clause)
        # Remove clauses containing True instance of this variable
        if chosen_literal in clause:
            clause_set.remove(clause)
        # Remove negation of this variable from all disjunctions
        elif -chosen_literal in clause:
            clause.remove(-chosen_literal)

    print(clause_set)

    # TODO: call function twice with chosen variable, and it's negation
    return False


# Inputs
clauses = [[1, -2], [-1, 3]]
# clauses = [[], [4, 5]]
partial_assign = []
print(branching_sat_solve(partial_assign, clauses))
