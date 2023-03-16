def dpll_sat_solve(partial_assignment, clause_set):
    # If str present in clause set convert set to int
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

    # Pure literal elimination
    def pure_literal_elimination(original_clause_set, partial_assignment):
        # Perform pure literal elimination
        unique_literals = generate_unique_vals(original_clause_set)
        pure_literals = []
        for literal in unique_literals:
            if -literal not in unique_literals:
                pure_literals.append(literal)

        print("-------------------------------------------------")
        print("Pure literals are: " + str(pure_literals))
        if pure_literals:
            for clause in clause_set[:]:
                for pure_literal in pure_literals:
                    if pure_literal in clause:
                        partial_assignment.append(pure_literal)
                        clause_set.remove(clause)
        print("Clause set after pure literal elimination: " + str(original_clause_set))
        print("-------------------------------------------------")

    # Repeatedly simplify clause set by applying rules for single literals
    def unit_propagate(clause_set, partial_assignment):
        while True:
            literal = None
            # print("clause set before unit propagation: " + str(clause_set))

            # Determine if any clauses contain a single literal
            for clause in clause_set:
                if len(clause) == 1:
                    literal = clause[0]
                    negative_literal = literal * -1

                    # Scan clause set to determine if contradiction is present
                    if [negative_literal] in clause_set:
                        clause_set.remove(clause)
                        clause_set.append([])
                        break

                    clause_set.remove(clause)
                    break

            if literal:
                # Add literal to partial assignment
                partial_assignment.append(literal)

                # print("Current literal is: " + str(literal))
                negative_literal = literal * -1
                # Scan clause set and simplify with new literal
                for clause in clause_set[:]:
                    # print(clause)
                    if literal in clause:
                        clause_set.remove(clause)
                    elif negative_literal in clause:
                        clause.remove(negative_literal)
                        if not clause:
                            clause_set.remove(clause)
                print("Unit propagation: " + str(clause_set))
                print()

                if not clause_set:
                    break
                elif [] in clause_set:
                    break
            else:
                break

    # Generate list of unique values in a clause set
    def generate_unique_vals(original_clause_set):
        # Generate list of remaining unique literals
        unique_set = set()
        for clause in original_clause_set:
            for literal in clause:
                unique_set.add(abs(literal))
        unique_literals = list(unique_set)
        return unique_literals

    # Recursively test for satisfiability on varying partial assignments
    def backtrack(updated_partial_assignment, original_clause_set):
        print()

        # Apply unit propagation
        unit_propagate(original_clause_set, updated_partial_assignment)

        # Apply pure literal elimination
        pure_literal_elimination(original_clause_set, updated_partial_assignment)

        # Generate remaining unique literals
        unique_literals = generate_unique_vals(original_clause_set)

        # If clause set contains no clauses, SAT;
        if not original_clause_set:
            return updated_partial_assignment
        # If empty clause present, UNSAT
        if [] in original_clause_set:
            return False

        # Try each literal and its negation at different levels
        for literal in unique_literals:
            both_assignments = [literal, -literal]
            if both_assignments[0] not in updated_partial_assignment and both_assignments[
                1] not in updated_partial_assignment:
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


# clauses = [[2, 3], [-1, -3], [-1, -2, 3], [4, 1, -3], [-4, 1, 3]]
clauses = [[1], [1, 4, 5], [-1, -2], [-1, 3], [-3, 2, 6], [6, 2, -7, -4, 5], [-6, 2, -7, -8, 9], [-1, -2, 4, -5],
           [1, 2, 4, -8]]
# (A OR B) AND (NOT A OR C) AND (D OR E OR NOT B)
# clauses = [[1, 2], [-1, 3], [4, 5, -2]]
print("Original clause set: " + str(clauses))
partial_assign = []
satisfiability = dpll_sat_solve(partial_assign, clauses)
if not satisfiability:
    print("UNSAT")
else:
    print("Satisfiable by: " + str(satisfiability))
