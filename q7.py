# Repeatedly simplify clause set by applying rules for single literals
def unit_propagate(clause_set):
    # If str present in clause set convert set to int
    if type(clause_set[0][0]) is str:
        int_list = []
        for clause in clause_set:
            int_list.append([eval(lit) for lit in clause])
        clause_set = int_list

    while True:
        literal = None
        print("clause set before unit propagation: " + str(clause_set))

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
            print("Current literal is: " + str(literal))
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
            print("clause set after unit propagation: " + str(clause_set))
            print()

            if not clause_set:
                break
            elif [] in clause_set:
                break
        else:
            break
    return clause_set


# input_set = [[1, -2], [1, 2], [-1, -2], [-1, 2], [1]]
# input_set = [['1', '-2'], ['1', '2'], ['-1', '-2'], ['-1', '2'], ['1']]

# Representing (x'1 + x'3) (x2 + x'5) (x3 + x4) (x3 + x'4) is clauses = [[-1, -3], [2, -5], [3, 4], [3, -4]]
# clauses = [[-3], [2, -5], [3, 4], [3, -4]]
# input_set = [[1, 2, 3], [-1, 2, 3], [1, -2, 3], [1, 2, -3], [1]]
# (A OR B) AND (NOT A OR C) AND (D OR E OR NOT B)
# clauses = [[1, 2], [-1, 3], [4, 5], [-2]]
# clauses = [[-1, -4, 5], [-1, 6, -5], [-1, -6, 7], [-1, -7, -5], [1, 4, 6]]
# (P),(P ∨ Q ∨ ¬R),(¬P ∨ R ∨ U),(¬P ∨ ¬Q),(¬Q ∨ ¬P ∨ R),(R ∨ ¬U ∨ V),(¬P ∨ Q ∨ V)
# clauses = [[1], [1, 2, -3], [-1, 3, 4], [-1, -2], [-2, -1, 3], [3, -4, 5], [-1, 2, 5]]
# (P)(P, U, V)(P, Q)(P, R)(R, Q, S)(S, Q, T, U, V)(S, Q, T, W, X)(P, Q, U, V)(P, Q, U, W)
# P=1, Q=2, R=3, U=4, V=5, S=6, T=7, W=8, X=9
# clauses = [[1], [1, 4, 5], [1, 2], [1, 3], [3, 2, 6], [6, 2, 7, 4, 5], [6, 2, 7, 8, 9], [1, 2, 4, 5], [1, 2, 4, 8]]
clauses = [[1], [1, 4, 5], [-1, -2], [-1, 3], [-3, 2, 6], [6, 2, -7, -4, 5], [-6, 2, -7, -8, 9], [-1, -2, 4, -5], [1, 2, 4, -8]]

print("clause set before unit propagation: " + str(clauses))
print()
print("Result: " + str(unit_propagate(clauses)))
