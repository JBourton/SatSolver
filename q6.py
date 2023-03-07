def branching_sat_solve(partial_assignment, clause_set):
    # Reduce clause set for selected variable
    if partial_assignment:
        print(partial_assignment)
        chosen_literal = partial_assignment[-1]
        for clause in clause_set[:]:
            # Remove clauses containing True instance of this variable
            if chosen_literal in clause:
                clause_set.remove(clause)
            # Remove negation of this variable from all disjunctions
            elif -chosen_literal in clause:
                clause.remove(-chosen_literal)
        print(clause_set)


    # If clause set contains empty clauses, UNSAT
    if [] in clause_set:
        return False
    # If clause_set contains no clauses, SAT;
    if not clause_set:
        return partial_assignment

    # Select new variable to eliminate
    chosen_literal = abs(clause_set[0][0])
    partial_assignment.append(chosen_literal)

    # Branch on the 2 truth assignments for selected variable
    partial_assignment.append(chosen_literal)
    branching_sat_solve(partial_assignment, clause_set)
    partial_assign.pop()
    partial_assign.append(-chosen_literal)
    branching_sat_solve(partial_assignment, clause_set)

    return False


# Inputs
clauses = [[1, -2], [-1, 3]]
# clauses = [[], [4, 5]]
partial_assign = []
print(branching_sat_solve(partial_assign, clauses))
