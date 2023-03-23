import collections


# Given a clause set in CNF, return a satisfying partial assignment, or False is none exists
def branching_sat_solve(partial_assignment, clause_set):
    # If clause set is empty, SAT
    if not clause_set:
        return partial_assignment

    # Select most common literal to branch on
    flattened_clause_set = [lit for clause in clause_set for lit in clause]
    counter = collections.Counter(flattened_clause_set)
    ordered_literals = [lit for lit, item in counter.most_common()]
    available_literals = list(
        {lit for lit in ordered_literals if -lit not in partial_assignment and lit not in partial_assignment})

    # If there are no more literals to branch on, SAT
    if not available_literals:
        return False

    # Try each of the available literals
    for branch_lit in available_literals:
        # Branch on the 2 truth assignments of chosen literal
        truth_assignments = [branch_lit, -branch_lit]

        for selected_literal in truth_assignments:
            reduced_clause_set = []
            new_partial_assignment = partial_assignment + [selected_literal]

            # Remove all instances of selected literal from the clause set
            for line in clause_set:
                if selected_literal not in line:
                    reduced_clause_set.append(line)

            # Backtrack until solution found
            result = branching_sat_solve(new_partial_assignment, reduced_clause_set)

            # Return false if unsat

            if result is not False:
                return result

    return False
