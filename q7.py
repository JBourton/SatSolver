# Repeatedly simplify clause set by applying rules for single literals
def unit_propagate(clause_set):
    literal = None

    # Determine if any clauses contain a single literal
    for clause in clause_set:
        if len(clause) == 1:
            literal = clause[0]
            # TODO: Clause set here is removed, but needs to be added back on later
            clause_set.remove(clause)

    print("Current literal is: " + str(literal))

    if literal:
        negative_literal = literal * -1
        # Scan clause set and simplify with new literal
        for clause in clause_set:
            if literal in clause:
                clause_set.remove(clause)
            elif negative_literal in clause:
                clause.remove(negative_literal)

        clause_set.append([literal])

        unit_propagate(clause_set)
    else:
        return clause_set


clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2], [1]]
unit_propagate(clauses)
