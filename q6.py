def branching_sat_solve(partial_assignment, clause_set):
    # If clause set contains empty clauses, UNSAT
    if [] in clause_set:
        return False
    # If clause_set contains no clauses, SAT;
    elif not clause_set:
        return partial_assignment
    # Search for a valid interpretation via backtracking
    else:
        # Select a variable to eliminate
        chosen_literal = abs(clause_set[0][0])
        partial_assignment.append(chosen_literal)

        for clause in clause_set[:]:
            # Remove clauses containing True instance of this variable
            if chosen_literal in clause:
                clause_set.remove(clause)
            # Remove negation of this variable from all disjunctions
            elif -chosen_literal in clause:
                clause.remove(-chosen_literal)

        print(clause_set)
        return branching_sat_solve(partial_assignment, clause_set)

    return False


# Inputs
clauses = [[1, -2], [-1, 3]]
# clauses = [[], [4, 5]]
partial_assign = []
print(branching_sat_solve(partial_assign, clauses))
