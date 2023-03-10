# Repeatedly simplify clause set by applying rules for single literals
def unit_propagate(clause_set):
    unit_clauses = []

    while True:
        literal = None
        print("clause set before unit propagation: " + str(clause_set))

        # Determine if any clauses contain a single literal
        for clause in clause_set:
            if len(clause) == 1:
                literal = clause[0]
                unit_clauses.append(clause)
                clause_set.remove(clause)
                break

        if literal:
            print("Current literal is: " + str(literal))
            negative_literal = literal * -1
            # Scan clause set and simplify with new literal
            for clause in clause_set[:]:
                print(clause)
                if literal in clause:
                    clause_set.remove(clause)
                elif negative_literal in clause:
                    clause.remove(negative_literal)
                    if not clause:
                        clause_set.remove(clause)

            if not clause_set:
                break
            print("and clause set after unit propagation: " + str(clause_set))

    # Append single literals
    clause_set += unit_clauses
    return clause_set


clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2], [1]]
print("Result: " + str(unit_propagate(clauses)))
