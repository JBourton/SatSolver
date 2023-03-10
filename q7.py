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
        else:
            break

    # Append single literals
    clause_set += unit_clauses
    return clause_set


clauses = [[1, -2], [1, 2], [-1, -2], [-1, 2], [1]]
# Representing (x'1 + x'3) (x2 + x'5) (x3 + x4) (x3 + x'4) is clauses = [[-1, -3], [2, -5], [3, 4], [3, -4]]
# clauses = [[-3], [2, -5], [3, 4], [3, -4]]
print("Result: " + str(unit_propagate(clauses)))

# TODO: Test should be to bring about an empty clause if a contradiction occurs, and if we have an empty clause,
#  return it because unsat
