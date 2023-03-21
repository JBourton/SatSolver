from collections import Counter


# Given a clause set in CNF, return a satisfying partial assignment, or False is none exists
def branching_sat_solve(partial_assignment, clause_set):
    # If clause set is empty, SAT
    if not clause_set:
        return partial_assignment

    # Select most common literal to branch on
    flattened_clause_set = [lit for clause in clause_set for lit in clause]
    literal_occurrences = Counter(flattened_clause_set)

    branch_literal = None
    for lit, index in literal_occurrences.most_common():
        if lit not in partial_assignment and -lit not in partial_assignment:
            branch_literal = lit
            break

    # If there are no more literals to branch on, SAT
    if branch_literal is None:
        return False

    # Branch on the 2 truth assignments of chosen literal
    assignments = [-branch_literal, branch_literal]
    for selected_literal in assignments:
        reduced_clause_set = []
        new_partial_assignment = partial_assignment + [selected_literal]

        # Remove all instances of selected literal from the clause set
        for line in clause_set:
            if -selected_literal not in line and selected_literal not in line:
                reduced_clause_set.append(line)

        # Backtrack until solution found
        result = branching_sat_solve(new_partial_assignment, reduced_clause_set)

        if result is not False:
            return result

    return False


clauses = [[1], [1, 4, 5], [-1, -2], [-1, 3], [-3, 2, 6], [6, 2, -7, -4, 5], [-6, 2, -7, -8, 9], [-1, -2, 4, -5],
           [1, 2, 4, -8]]
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
partial_assign = []

print("Original clause set: " + str(clauses))
print()
solution = branching_sat_solve(partial_assign, four_queens)
if solution is not False:
    print("Satisfying assignment found: " + str(solution))
else:
    print("UNSAT")
