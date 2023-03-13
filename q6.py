# Given a clause set in CNF, return a satisfying partial assignment, or False is none exists
def branching_sat_solve(partial_assignment, clause_set):
    # Convert str clause set to int
    if type(clause_set[0][0]) is str:
        int_list = []
        for clause in clause_set:
            int_list.append([eval(lit) for lit in clause])
        clause_set = int_list

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

    # Search for a satisfying partial assignment
    def backtrack(updated_partial_assignment, original_clause_set):
        print()
        # If clause_set contains no clauses, SAT;
        if not original_clause_set:
            print("clause set empty, expression is SAT")
            return updated_partial_assignment

        # Generate list of remaining unique literals
        unique_set = set()
        for clause in original_clause_set:
            for literal in clause:
                unique_set.add(abs(literal))
        unique_literals = list(unique_set)

        # Try each literal and its negation at different levels
        for literal in unique_literals:
            both_assignments = [literal, -literal]
            if both_assignments[0] not in updated_partial_assignment and both_assignments[1] not in updated_partial_assignment:
                # Branch on the 2 truth assignments for selected variable
                for selected_literal in both_assignments:
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
input_set = [['1', '-2'], ['1', '2'], ['-1', '-2'], ['-1', '2'], ['1']]
# clauses = [[1, -2], [-1, 3]]
# clauses = [[], [4, 5]]
# clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2]]
# clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2], [1]]
# clauses = [[-1, 2, 3], [1, 3, 4], [1, 3, -4], [1, -3, 4], [1, -3, -4], [-2, -3, 4], [-1, 2, -3], [-1, -2, 3]]
# clauses = [[1, 2, 3], [-1, 2, 3], [1, -2, 3], [1, 2, -3]]
clauses = [[2, 3], [-1, -3], [-1, -2, 3], [4, 1, -3], [-4, 1, 3]]

print("Original clause set: " + str(input_set))
partial_assign = []
satisfiability = branching_sat_solve(partial_assign, input_set)
if not satisfiability:
    print("UNSAT")
else:
    print("Satisfiable by: " + str(satisfiability))
