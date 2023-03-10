# Repeatedly simplify clause set by applying rules for single literals
def unit_propagate(clause_set):
    print("clause set before unit propagation: " + str(clause_set))
    literal = None

    # Determine if any clauses contain a single literal
    literal_found = False
    for clause in clause_set:
        if len(clause) == 1:
            literal_found = True
            literal = clause[0]
            clause_set.remove(clause)
            break

    # TODO: Implement recursion part, then test this
    if not literal_found:
        print("hi")
        return clause_set

    print("Current literal is: " + str(literal))

    if literal:
        negative_literal = literal * -1
        # Scan clause set and simplify with new literal
        for clause in clause_set[:]:
            print(clause)
            if literal in clause:
                clause_set.remove(clause)
            elif negative_literal in clause:
                clause.remove(negative_literal)

        clause_set.append([literal])

        print("and clause set after unit propagation: " + str(clause_set))

        # unit_propagate(clause_set)
    else:
        return clause_set


clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2], [1]]
print("Result: " + str(unit_propagate(clauses)))
