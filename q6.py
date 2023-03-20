# Given a clause set in CNF, return a satisfying partial assignment, or False is none exists
def branching_sat_solve(partial_assignment, clause_set):
    # Apply propagation to clause set
    def reduce(original_clause_set, chosen_literal):
        print("chosen literal: " + str(chosen_literal))
        copy_set = original_clause_set[:]
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
        elif [] in original_clause_set:
            print("clause set contains an empty clause, UNSAT")
            return False

        # Find most common element to branch on
        # Credit: GeeksForGeeks for basic implementation of selecting the literal with the highest frequency
        # appearance ~ https://www.geeksforgeeks.org/python-find-most-common-element-in-a-2d-list/
        flattened_set = [lit for clause in original_clause_set for lit in clause]
        available_literals = [lit for lit in flattened_set if -lit not in updated_partial_assignment and lit not in updated_partial_assignment]
        if available_literals:
            literal = max(available_literals, key=flattened_set.count)
        else:
            if len(original_clause_set) == 0:
                # Satisfying assignment found
                return updated_partial_assignment
            else:
                # UNSAT under current assignment, return up a level
                return False

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


# Inputs
# clauses = [['1', '-2'], ['1', '2'], ['-1', '-2'], ['-1', '2'], ['1']]
# clauses = [[1, -2], [-1, 3]]
clauses = [[], [4, 5]]
# clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2]]
# clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2], [1]]
# clauses = [[-1, 2, 3], [1, 3, 4], [1, 3, -4], [1, -3, 4], [1, -3, -4], [-2, -3, 4], [-1, 2, -3], [-1, -2, 3]]
# clauses = [[1, 2, 3], [-1, 2, 3], [1, -2, 3], [1, 2, -3]]
# clauses = [[2, 3], [-1, -3], [-1, -2, 3], [4, 1, -3], [-4, 1, 3]]
# clauses = [[1], [1, 4, 5], [-1, -2], [-1, 3], [-3, 2, 6], [6, 2, -7, -4, 5], [-6, 2, -7, -8, 9], [-1, -2, 4, -5], [1, 2, 4, -8]]
four_queens = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [-1, -5], [-2, -6],
               [-3, -7], [-4, -8], [-1, -9], [-2, -10], [-3, -11], [-4, -12], [-1, -13], [-2, -14],
               [-3, -15], [-4, -16], [-1, -17], [-2, -18], [-3, -19], [-4, -20], [-5, -1], [-6, -2], [-7, -3], [-8, -4],
               [-5, -9], [-6, -10], [-7, -11], [-8, -12], [-5, -13], [-6, -14], [-7, -15], [-8, -16], [-5, -17],
               [-6, -18], [-7, -19], [-8, -20], [-9, -1], [-10, -2], [-11, -3], [-12, -4], [-9, -5], [-10, -6],
               [-11, -7], [-12, -8], [-9, -13], [-10, -14], [-11, -15], [-12, -16], [-9, -17], [-10, -18], [-11, -19],
               [-12, -20], [-13, -1], [-14, -2], [-15, -3], [-16, -4], [-13, -5], [-14, -6], [-15, -7], [-16, -8],
               [-13, -9], [-14, -10], [-15, -11], [-16, -12], [-13, -17], [-14, -18], [-15, -19], [-16, -20], [-17, -1],
               [-18, -2], [-19, -3], [-20, -4], [-17, -5], [-18, -6], [-19, -7], [-20, -8], [-17, -9], [-18, -10],
               [-19, -11], [-20, -12], [-17, -13], [-18, -14], [-19, -15], [-20, -16]]
print("Original clause set: " + str(clauses))
partial_assign = []
satisfiability = branching_sat_solve(partial_assign, clauses)
if not satisfiability:
    print("UNSAT")
else:
    print("Satisfiable by: " + str(satisfiability))
