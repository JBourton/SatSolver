from collections import Counter


# Given a clause set in CNF, return a satisfying partial assignment, or False is none exists
def branching_sat_solve(partial_assignment, clause_set):
    # Backtrack when argument under partial assignment found to be UNSAT
    def backtrack(updated_partial_assignment, original_clause_set):
        # If clause set is empty, SAT
        if not original_clause_set:
            return updated_partial_assignment

        # Select most common literal to branch on
        flattened_clause_set = [lit for clause in original_clause_set for lit in clause]
        literal_occurrences = Counter(flattened_clause_set)

        branch_literal = None
        for lit, index in literal_occurrences.most_common():
            if lit not in updated_partial_assignment and -lit not in updated_partial_assignment:
                branch_literal = lit
                break
        print("branch literal: " + str(branch_literal))

        # If there are no more literals to branch on, SAT
        if branch_literal is None:
            return False

        assignments = [-branch_literal, branch_literal]
        for selected_literal in assignments:
            new_partial_assignment = updated_partial_assignment + [selected_literal]

            # Remove all instances of selected literal from the clause set
            reduced_clause_set = [clause for clause in original_clause_set if selected_literal not in clause]

            result = backtrack(new_partial_assignment, reduced_clause_set)

            if result is not False:
                print("Partial assignment: " + str(new_partial_assignment))
                return result

        return False

    return backtrack(partial_assignment, clause_set)


clauses = [[1], [1, 4, 5], [-1, -2], [-1, 3], [-3, 2, 6], [6, 2, -7, -4, 5], [-6, 2, -7, -8, 9], [-1, -2, 4, -5],
           [1, 2, 4, -8]]
partial_assign = []

print("Original clause set: " + str(clauses))
print()
solution = branching_sat_solve(partial_assign, clauses)
if solution is not False:
    print("Satisfying assignment found: " + str(solution))
else:
    print("UNSAT")
