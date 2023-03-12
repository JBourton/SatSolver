# Given a clause set in CNF, return a satisfying partial assignment, or False is none exists
def branching_sat_solve(partial_assignment, clause_set):
    # Reduce clause set for selected variable
    if partial_assignment:
        chosen_literal = partial_assignment[-1]
        print("chosenlit: " + str(chosen_literal))
        for clause in clause_set[:]:
            # Remove clauses containing True instance of this variable
            if chosen_literal in clause:
                clause_set.remove(clause)
            # Remove negation of this variable from all disjunctions
            elif -chosen_literal in clause:
                clause.remove(-chosen_literal)
        partial_assignment.pop()

    # If clause_set contains no clauses, SAT;
    if not clause_set:
        return True
    # If clause set contains empty clauses, UNSAT
    if [] in clause_set:
        print("Going up recursion level with: " + str(partial_assignment) + " because of: " + str(clause_set))
        return False

    # Select new variable to eliminate
    chosen_literal = abs(clause_set[0][0])
    partial_assignment.append(chosen_literal)
    print("Clause Set: " + str(clause_set))
    print("Partial Assignment: " + str(partial_assignment))

    # Branch on the 2 truth assignments for selected variable
    partial_assignment.append(chosen_literal)
    if branching_sat_solve(partial_assignment, clause_set):
        return partial_assignment
    partial_assign.pop()
    partial_assign.append(-chosen_literal)
    if branching_sat_solve(partial_assignment, clause_set):
        return partial_assignment

    return False


# Inputs
# clauses = [[1, -2], [-1, 3]]
# clauses = [[], [4, 5]]
# clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2]]
# clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2], [1]]
# clauses = [[-1, 2, 3], [1, 3, 4], [1, 3, -4], [1, -3, 4], [1, -3, -4], [-2, -3, 4], [-1, 2, -3], [-1, -2, 3]]
# clauses = [[1, 2, 3], [-1, 2, 3], [1, -2, 3], [1, 2, -3]]
clauses = [[2, 3], [-1, -3], [-1, -2, 3], [4, 1, -3], [-4, 1, 3]]

partial_assign = []
satisfiability = branching_sat_solve(partial_assign, clauses)
if not satisfiability:
    print("UNSAT")
else:
    print("Satisfiable by: " + str(satisfiability))
