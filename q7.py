# Iteratively reduce clause set by applying single literal rule
def unit_propagate(clause_set):
    while True:
        literal = None

        # Search for presence of single literal
        for clause in clause_set:
            if len(clause) == 1:
                literal = clause[0]
                negative_literal = literal * -1

                # Search clause set to determine if contradiction is present
                if negative_literal in clause_set:
                    clause_set.remove(clause)
                    break

                clause_set.remove(clause)
                break

        if literal:
            # Search clause set and simplify with new literal
            for clause in clause_set[:]:
                if literal in clause:
                    clause_set.remove(clause)
                elif negative_literal in clause:
                    clause.remove(negative_literal)
                    if not clause:
                        clause_set.remove(clause)

            if not clause_set:
                break
            elif [] in clause_set:
                break
        else:
            break
    return clause_set
