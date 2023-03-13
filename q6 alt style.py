# Given a clause set in CNF, return a satisfying partial assignment, or False is none exists
def branching_sat_solve(partial_assignment, clause_set):
    # Apply propagation to clause set
    # TODO: probably something wrong with this function
    def reduce(original_clause_set, chosen_literal):
        print("chosen literal: " + str(chosen_literal))
        copy_set = original_clause_set[:]
        for clause_line in copy_set[:]:
            # Remove clauses containing True instance of this variable
            if chosen_literal in clause_line:
                copy_set.remove(clause_line)
            # Remove negation of this variable from all disjunctions
            #elif -chosen_literal in clause_line:
            #    clause_line.remove(-chosen_literal)
        print("new_clause_set: " + str(copy_set))
        return copy_set

    # Search for a satisfying partial assignment
    def backtrack(updated_partial_assignment, original_clause_set):
        print()
        # If clause_set contains no clauses, SAT;
        if not original_clause_set:
            print("clause set empty, expression is SAT")
            return updated_partial_assignment
        # If clause set contains empty clauses, UNSAT
        # elif [] in original_clause_set:
        #    print("[] in clause set")
        #    return False

        # Generate list of remaining unique literals
        unique_set = set()
        for clause in original_clause_set:
            for literal in clause:
                unique_set.add(abs(literal))
        unique_literals = list(unique_set)
        # print("Unique literals: " + str(unique_literals))

        # Try each literal and its negation at different levels
        for literal in unique_literals:
            if literal not in updated_partial_assignment and -literal not in updated_partial_assignment:
                # Branch on the 2 truth assignments for selected variable
                for selected_literal in [literal, -literal]:
                    new_partial_assignment = updated_partial_assignment + [selected_literal]
                    print("new_partial_assignment: " + str(new_partial_assignment))

                    # Simplify expression with selected literal
                    new_clause_set = reduce(original_clause_set, selected_literal)

                    result = backtrack(new_partial_assignment, new_clause_set)

                    if result is not False:
                        # Need some way to revert to original state of clause set - we already have this
                        print("Result is: " + str(result))
                        return result

        return False

    return backtrack(partial_assignment, clause_set)


clauses = [[2, 3], [-1, -3], [-1, -2, 3], [4, 1, -3], [-4, 1, 3]]

print("Original clause set: " + str(clauses))
partial_assign = []
satisfiability = branching_sat_solve(partial_assign, clauses)
if not satisfiability:
    print("UNSAT")
else:
    print("Satisfiable by: " + str(satisfiability))
