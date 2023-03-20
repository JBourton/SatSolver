# Given a clause set in CNF, return a satisfying partial assignment, or False is none exists
def branching_sat_solve(partial_assignment, clause_set):
    # Apply propagation to clause set
    def reduce(original_clause_set, chosen_literal):
        print("chosen literal: " + str(chosen_literal))
        copy_set = [clause_line[:] for clause_line in original_clause_set]
        for clause_line in copy_set[:]:
            # Remove clauses containing True instance of this variable
            if chosen_literal in clause_line:
                copy_set.remove(clause_line)
        print("new_clause_set: " + str(copy_set))
        return copy_set

    def backtrack(updated_partial_assignment, original_clause_set):
        print()
        # If clause set contains no clauses, SAT;
        if not original_clause_set:
            print("clause set empty, expression is SAT")
            return updated_partial_assignment

        # Find most common element to branch on
        # Credit: GeeksForGeeks for basic implementation of selecting the literal with the highest frequency
        # appearance ~ https://www.geeksforgeeks.org/python-find-most-common-element-in-a-2d-list/
        flattened_set = [lit for clause in original_clause_set for lit in clause]
        available_literals = [lit for lit in flattened_set if -lit not in updated_partial_assignment and
                              lit not in updated_partial_assignment]
        if available_literals:
            literal = max(available_literals, key=flattened_set.count)
        else:
            # Satisfying assignment found
            return updated_partial_assignment

        # Try each literal and its negation at different levels
        both_assignments = [literal, -literal]
        if both_assignments[0] not in updated_partial_assignment and \
                both_assignments[1] not in updated_partial_assignment:
            # Try each literal and its negation at different levels
            for selected_literal in both_assignments:
                if -literal not in updated_partial_assignment:
                    new_partial_assignment = updated_partial_assignment + [selected_literal]
                    print("new_partial_assignment: " + str(new_partial_assignment))

                    # Simplify expression with selected literal
                    new_clause_set = reduce(original_clause_set, selected_literal)

                    # Backtrack to find satisfying assignment
                    result = backtrack(new_partial_assignment, new_clause_set)

                    if result:
                        return result

        return False

    return backtrack(partial_assignment, clause_set)


# clauses = [[2, 3], [-1, -3], [-1, -2, 3], [4, 1, -3], [-4, 1, 3]]
clauses = [[-1, 2, 3], [1, 3, 4], [1, 3, -4], [1, -3, 4], [1, -3, -4], [-2, -3, 4], [-1, 2, -3], [-1, -2, 3]]


print("Original clause set: " + str(clauses))
partial_assign = []
satisfiability = branching_sat_solve(partial_assign, clauses)
if not satisfiability:
    print("UNSAT")
else:
    print("Satisfiable by: " + str(satisfiability))
