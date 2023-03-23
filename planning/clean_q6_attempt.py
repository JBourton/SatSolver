# Given a clause set in CNF, return a satisfying partial assignment, or False is none exists
def branching_sat_solve(partial_assignment, clause_set):
    # If clause set is empty, SAT
    if not clause_set:
        return partial_assignment

    # Select a literal to branch on
    flattened_clause_set = [lit for clause in clause_set for lit in clause]
    available_literals = list(
        {lit for lit in flattened_clause_set if -lit not in partial_assignment and lit not in partial_assignment})

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
                if selected_literal not in line:  # and -selected_literal not in line
                    reduced_clause_set.append(line)

            # Backtrack until solution found
            result = branching_sat_solve(new_partial_assignment, reduced_clause_set)

            # Return false if unsat

            if result is not False:
                return result

    return False


clauses = [[1, -2], [-1, -2], [-1, 2], [1, 3], [2, -3, 4], [2, -4, 5], [3, 4, -5], [3, -4, 6], [-4, -5, 6], [-4, 5, -6], [-6, 7], [-6, -8], [6, 9], [-6, 10], [-6, -11], [7, -8], [-7, 8], [-8, -9], [9, 10], [9, -11], [-10, 11], [-1, -7, 8], [2, 5, 9], [-3, 4, -8], [1, -5, -10], [-2, -6, -11]]
# clauses = [[-1, 2], [-1, -4], [-1, -5], [1, -3], [1, -7], [1, -8], [-2, -3, 4], [-2, 3, -4], [2, -4, 5], [2, 4, -5], [-3, 4, 6], [-3, -4, -6], [-4, -5, 6], [-4, -6, 7], [-5, -7, 8], [-5, 6, -8], [6, 8, -9], [-7, 8, -9], [1, 2, 3], [-2, 5, 7]]
# clauses = [[-1, 2, 3], [1, -2, 3], [1, 2, -3], [-1, -2, -3, 4], [1, 2, -4], [-1, -3, 4], [1, -3, -4], [-1, 2, -4], [2, 3, 5], [2, 4, 5], [-3, 4, 5], [1, -5, 6], [-1, 5, -6], [-4, -5, 7], [-5, 6, -7]]
# clauses = [[1], [1, 4, 5], [-1, -2], [-1, 3], [-3, 2, 6], [6, 2, -7, -4, 5], [-6, 2, -7, -8, 9], [-1, -2, 4, -5], [1, 2, 4, -8]]
four_queens = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [-1, -5], [-2, -6],
               [-3, -7], [-4, -8], [-1, -9], [-2, -10], [-3, -11], [-4, -12], [-1, -13], [-2, -14],
               [-3, -15], [-4, -16], [-1, -17], [-2, -18], [-3, -19], [-4, -20], [-5, -1], [-6, -2], [-7, -3], [-8, -4],
               [-5, -9], [-6, -10], [-7, -11], [-8, -12], [-5, -13], [-6, -14], [-7, -15], [-8, -16], [-5, -17],
               [-6, -18], [-7, -19], [-8, -20], [-9, -1], [-10, -2], [-11, -3], [-12, -4], [-9, -5], [-10, -6],
               [-11, -7], [-12, -8], [-9, -13], [-10, -14], [-11, -15], [-12, -16], [-9, -17], [-10, -18], [-11, -19],
               [-12, -20], [-13, -1], [-14, -2], [-15, -3], [-16, -4], [-13, -5], [-14, -6], [-15, -7], [-16, -8],
               [-13, -9], [-14, -10], [-15, -11], [-16, -12], [-13, -17], [-14, -18], [-15, -19], [-16, -20], [-17, -1],
               [-18, -2], [-19, -3], [-20, -4], [-17, -5], [-18, -6], [-19, -7], [-20, -8], [-17, -9], [-18, -10],
               [-19, -11], [-20, -12], [-17, -13], [-18, -14], [-19, -15], [-20, -16]]
php_5_4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [-1, -5], [-2, -6],
           [-3, -7], [-4, -8], [-1, -9], [-2, -10], [-3, -11], [-4, -12], [-1, -13], [-2, -14], [-3, -15], [-4, -16],
           [-1, -17], [-2, -18], [-3, -19], [-4, -20], [-5, -1], [-6, -2], [-7, -3], [-8, -4], [-5, -9], [-6, -10],
           [-7, -11], [-8, -12], [-5, -13], [-6, -14], [-7, -15], [-8, -16], [-5, -17], [-6, -18], [-7, -19], [-8, -20],
           [-9, -1], [-10, -2], [-11, -3], [-12, -4], [-9, -5], [-10, -6], [-11, -7], [-12, -8], [-9, -13], [-10, -14],
           [-11, -15], [-12, -16], [-9, -17], [-10, -18], [-11, -19], [-12, -20], [-13, -1], [-14, -2], [-15, -3],
           [-16, -4], [-13, -5], [-14, -6], [-15, -7], [-16, -8], [-13, -9], [-14, -10], [-15, -11], [-16, -12],
           [-13, -17], [-14, -18], [-15, -19], [-16, -20], [-17, -1], [-18, -2], [-19, -3], [-20, -4], [-17, -5],
           [-18, -6], [-19, -7], [-20, -8], [-17, -9], [-18, -10], [-19, -11], [-20, -12], [-17, -13], [-18, -14],
           [-19, -15], [-20, -16]]
eight_queens = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30, 31, 32], [33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48],
                [49, 50, 51, 52, 53, 54, 55, 56], [57, 58, 59, 60, 61, 62, 63, 64], [-1, -2], [-1, -3], [-1, -4],
                [-1, -5], [-1, -6], [-1, -7], [-1, -8], [-1, -9], [-1, -10], [-1, -17], [-1, -19], [-1, -25], [-1, -28],
                [-1, -33], [-1, -37], [-1, -41], [-1, -46], [-1, -49], [-1, -55], [-1, -57], [-1, -64], [-2, -1],
                [-2, -3], [-2, -4], [-2, -5], [-2, -6], [-2, -7], [-2, -8], [-2, -9], [-2, -10], [-2, -11], [-2, -18],
                [-2, -20], [-2, -26], [-2, -29], [-2, -34], [-2, -38], [-2, -42], [-2, -47], [-2, -50], [-2, -56],
                [-2, -58], [-3, -1], [-3, -2], [-3, -4], [-3, -5], [-3, -6], [-3, -7], [-3, -8], [-3, -10], [-3, -11],
                [-3, -12], [-3, -17], [-3, -19], [-3, -21], [-3, -27], [-3, -30], [-3, -35], [-3, -39], [-3, -43],
                [-3, -48], [-3, -51], [-3, -59], [-4, -1], [-4, -2], [-4, -3], [-4, -5], [-4, -6], [-4, -7], [-4, -8],
                [-4, -11], [-4, -12], [-4, -13], [-4, -18], [-4, -20], [-4, -22], [-4, -25], [-4, -28], [-4, -31],
                [-4, -36], [-4, -40], [-4, -44], [-4, -52], [-4, -60], [-5, -1], [-5, -2], [-5, -3], [-5, -4], [-5, -6],
                [-5, -7], [-5, -8], [-5, -12], [-5, -13], [-5, -14], [-5, -19], [-5, -21], [-5, -23], [-5, -26],
                [-5, -29], [-5, -32], [-5, -33], [-5, -37], [-5, -45], [-5, -53], [-5, -61], [-6, -1], [-6, -2],
                [-6, -3], [-6, -4], [-6, -5], [-6, -7], [-6, -8], [-6, -13], [-6, -14], [-6, -15], [-6, -20], [-6, -22],
                [-6, -24], [-6, -27], [-6, -30], [-6, -34], [-6, -38], [-6, -41], [-6, -46], [-6, -54], [-6, -62],
                [-7, -1], [-7, -2], [-7, -3], [-7, -4], [-7, -5], [-7, -6], [-7, -8], [-7, -14], [-7, -15], [-7, -16],
                [-7, -21], [-7, -23], [-7, -28], [-7, -31], [-7, -35], [-7, -39], [-7, -42], [-7, -47], [-7, -49],
                [-7, -55], [-7, -63], [-8, -1], [-8, -2], [-8, -3], [-8, -4], [-8, -5], [-8, -6], [-8, -7], [-8, -15],
                [-8, -16], [-8, -22], [-8, -24], [-8, -29], [-8, -32], [-8, -36], [-8, -40], [-8, -43], [-8, -48],
                [-8, -50], [-8, -56], [-8, -57], [-8, -64], [-9, -1], [-9, -2], [-9, -10], [-9, -11], [-9, -12],
                [-9, -13], [-9, -14], [-9, -15], [-9, -16], [-9, -17], [-9, -18], [-9, -25], [-9, -27], [-9, -33],
                [-9, -36], [-9, -41], [-9, -45], [-9, -49], [-9, -54], [-9, -57], [-9, -63], [-10, -1], [-10, -2],
                [-10, -3], [-10, -9], [-10, -11], [-10, -12], [-10, -13], [-10, -14], [-10, -15], [-10, -16],
                [-10, -17], [-10, -18], [-10, -19], [-10, -26], [-10, -28], [-10, -34], [-10, -37], [-10, -42],
                [-10, -46], [-10, -50], [-10, -55], [-10, -58], [-10, -64], [-11, -2], [-11, -3], [-11, -4], [-11, -9],
                [-11, -10], [-11, -12], [-11, -13], [-11, -14], [-11, -15], [-11, -16], [-11, -18], [-11, -19],
                [-11, -20], [-11, -25], [-11, -27], [-11, -29], [-11, -35], [-11, -38], [-11, -43], [-11, -47],
                [-11, -51], [-11, -56], [-11, -59], [-12, -3], [-12, -4], [-12, -5], [-12, -9], [-12, -10], [-12, -11],
                [-12, -13], [-12, -14], [-12, -15], [-12, -16], [-12, -19], [-12, -20], [-12, -21], [-12, -26],
                [-12, -28], [-12, -30], [-12, -33], [-12, -36], [-12, -39], [-12, -44], [-12, -48], [-12, -52],
                [-12, -60], [-13, -4], [-13, -5], [-13, -6], [-13, -9], [-13, -10], [-13, -11], [-13, -12], [-13, -14],
                [-13, -15], [-13, -16], [-13, -20], [-13, -21], [-13, -22], [-13, -27], [-13, -29], [-13, -31],
                [-13, -34], [-13, -37], [-13, -40], [-13, -41], [-13, -45], [-13, -53], [-13, -61], [-14, -5],
                [-14, -6], [-14, -7], [-14, -9], [-14, -10], [-14, -11], [-14, -12], [-14, -13], [-14, -15], [-14, -16],
                [-14, -21], [-14, -22], [-14, -23], [-14, -28], [-14, -30], [-14, -32], [-14, -35], [-14, -38],
                [-14, -42], [-14, -46], [-14, -49], [-14, -54], [-14, -62], [-15, -6], [-15, -7], [-15, -8], [-15, -9],
                [-15, -10], [-15, -11], [-15, -12], [-15, -13], [-15, -14], [-15, -16], [-15, -22], [-15, -23],
                [-15, -24], [-15, -29], [-15, -31], [-15, -36], [-15, -39], [-15, -43], [-15, -47], [-15, -50],
                [-15, -55], [-15, -57], [-15, -63], [-16, -7], [-16, -8], [-16, -9], [-16, -10], [-16, -11], [-16, -12],
                [-16, -13], [-16, -14], [-16, -15], [-16, -23], [-16, -24], [-16, -30], [-16, -32], [-16, -37],
                [-16, -40], [-16, -44], [-16, -48], [-16, -51], [-16, -56], [-16, -58], [-16, -64], [-17, -1],
                [-17, -3], [-17, -9], [-17, -10], [-17, -18], [-17, -19], [-17, -20], [-17, -21], [-17, -22],
                [-17, -23], [-17, -24], [-17, -25], [-17, -26], [-17, -33], [-17, -35], [-17, -41], [-17, -44],
                [-17, -49], [-17, -53], [-17, -57], [-17, -62], [-18, -2], [-18, -4], [-18, -9], [-18, -10], [-18, -11],
                [-18, -17], [-18, -19], [-18, -20], [-18, -21], [-18, -22], [-18, -23], [-18, -24], [-18, -25],
                [-18, -26], [-18, -27], [-18, -34], [-18, -36], [-18, -42], [-18, -45], [-18, -50], [-18, -54],
                [-18, -58], [-18, -63], [-19, -1], [-19, -3], [-19, -5], [-19, -10], [-19, -11], [-19, -12], [-19, -17],
                [-19, -18], [-19, -20], [-19, -21], [-19, -22], [-19, -23], [-19, -24], [-19, -26], [-19, -27],
                [-19, -28], [-19, -33], [-19, -35], [-19, -37], [-19, -43], [-19, -46], [-19, -51], [-19, -55],
                [-19, -59], [-19, -64], [-20, -2], [-20, -4], [-20, -6], [-20, -11], [-20, -12], [-20, -13], [-20, -17],
                [-20, -18], [-20, -19], [-20, -21], [-20, -22], [-20, -23], [-20, -24], [-20, -27], [-20, -28],
                [-20, -29], [-20, -34], [-20, -36], [-20, -38], [-20, -41], [-20, -44], [-20, -47], [-20, -52],
                [-20, -56], [-20, -60], [-21, -3], [-21, -5], [-21, -7], [-21, -12], [-21, -13], [-21, -14], [-21, -17],
                [-21, -18], [-21, -19], [-21, -20], [-21, -22], [-21, -23], [-21, -24], [-21, -28], [-21, -29],
                [-21, -30], [-21, -35], [-21, -37], [-21, -39], [-21, -42], [-21, -45], [-21, -48], [-21, -49],
                [-21, -53], [-21, -61], [-22, -4], [-22, -6], [-22, -8], [-22, -13], [-22, -14], [-22, -15], [-22, -17],
                [-22, -18], [-22, -19], [-22, -20], [-22, -21], [-22, -23], [-22, -24], [-22, -29], [-22, -30],
                [-22, -31], [-22, -36], [-22, -38], [-22, -40], [-22, -43], [-22, -46], [-22, -50], [-22, -54],
                [-22, -57], [-22, -62], [-23, -5], [-23, -7], [-23, -14], [-23, -15], [-23, -16], [-23, -17],
                [-23, -18], [-23, -19], [-23, -20], [-23, -21], [-23, -22], [-23, -24], [-23, -30], [-23, -31],
                [-23, -32], [-23, -37], [-23, -39], [-23, -44], [-23, -47], [-23, -51], [-23, -55], [-23, -58],
                [-23, -63], [-24, -6], [-24, -8], [-24, -15], [-24, -16], [-24, -17], [-24, -18], [-24, -19],
                [-24, -20], [-24, -21], [-24, -22], [-24, -23], [-24, -31], [-24, -32], [-24, -38], [-24, -40],
                [-24, -45], [-24, -48], [-24, -52], [-24, -56], [-24, -59], [-24, -64], [-25, -1], [-25, -4], [-25, -9],
                [-25, -11], [-25, -17], [-25, -18], [-25, -26], [-25, -27], [-25, -28], [-25, -29], [-25, -30],
                [-25, -31], [-25, -32], [-25, -33], [-25, -34], [-25, -41], [-25, -43], [-25, -49], [-25, -52],
                [-25, -57], [-25, -61], [-26, -2], [-26, -5], [-26, -10], [-26, -12], [-26, -17], [-26, -18],
                [-26, -19], [-26, -25], [-26, -27], [-26, -28], [-26, -29], [-26, -30], [-26, -31], [-26, -32],
                [-26, -33], [-26, -34], [-26, -35], [-26, -42], [-26, -44], [-26, -50], [-26, -53], [-26, -58],
                [-26, -62], [-27, -3], [-27, -6], [-27, -9], [-27, -11], [-27, -13], [-27, -18], [-27, -19], [-27, -20],
                [-27, -25], [-27, -26], [-27, -28], [-27, -29], [-27, -30], [-27, -31], [-27, -32], [-27, -34],
                [-27, -35], [-27, -36], [-27, -41], [-27, -43], [-27, -45], [-27, -51], [-27, -54], [-27, -59],
                [-27, -63], [-28, -1], [-28, -4], [-28, -7], [-28, -10], [-28, -12], [-28, -14], [-28, -19], [-28, -20],
                [-28, -21], [-28, -25], [-28, -26], [-28, -27], [-28, -29], [-28, -30], [-28, -31], [-28, -32],
                [-28, -35], [-28, -36], [-28, -37], [-28, -42], [-28, -44], [-28, -46], [-28, -49], [-28, -52],
                [-28, -55], [-28, -60], [-28, -64], [-29, -2], [-29, -5], [-29, -8], [-29, -11], [-29, -13], [-29, -15],
                [-29, -20], [-29, -21], [-29, -22], [-29, -25], [-29, -26], [-29, -27], [-29, -28], [-29, -30],
                [-29, -31], [-29, -32], [-29, -36], [-29, -37], [-29, -38], [-29, -43], [-29, -45], [-29, -47],
                [-29, -50], [-29, -53], [-29, -56], [-29, -57], [-29, -61], [-30, -3], [-30, -6], [-30, -12],
                [-30, -14], [-30, -16], [-30, -21], [-30, -22], [-30, -23], [-30, -25], [-30, -26], [-30, -27],
                [-30, -28], [-30, -29], [-30, -31], [-30, -32], [-30, -37], [-30, -38], [-30, -39], [-30, -44],
                [-30, -46], [-30, -48], [-30, -51], [-30, -54], [-30, -58], [-30, -62], [-31, -4], [-31, -7],
                [-31, -13], [-31, -15], [-31, -22], [-31, -23], [-31, -24], [-31, -25], [-31, -26], [-31, -27],
                [-31, -28], [-31, -29], [-31, -30], [-31, -32], [-31, -38], [-31, -39], [-31, -40], [-31, -45],
                [-31, -47], [-31, -52], [-31, -55], [-31, -59], [-31, -63], [-32, -5], [-32, -8], [-32, -14],
                [-32, -16], [-32, -23], [-32, -24], [-32, -25], [-32, -26], [-32, -27], [-32, -28], [-32, -29],
                [-32, -30], [-32, -31], [-32, -39], [-32, -40], [-32, -46], [-32, -48], [-32, -53], [-32, -56],
                [-32, -60], [-32, -64], [-33, -1], [-33, -5], [-33, -9], [-33, -12], [-33, -17], [-33, -19], [-33, -25],
                [-33, -26], [-33, -34], [-33, -35], [-33, -36], [-33, -37], [-33, -38], [-33, -39], [-33, -40],
                [-33, -41], [-33, -42], [-33, -49], [-33, -51], [-33, -57], [-33, -60], [-34, -2], [-34, -6],
                [-34, -10], [-34, -13], [-34, -18], [-34, -20], [-34, -25], [-34, -26], [-34, -27], [-34, -33],
                [-34, -35], [-34, -36], [-34, -37], [-34, -38], [-34, -39], [-34, -40], [-34, -41], [-34, -42],
                [-34, -43], [-34, -50], [-34, -52], [-34, -58], [-34, -61], [-35, -3], [-35, -7], [-35, -11],
                [-35, -14], [-35, -17], [-35, -19], [-35, -21], [-35, -26], [-35, -27], [-35, -28], [-35, -33],
                [-35, -34], [-35, -36], [-35, -37], [-35, -38], [-35, -39], [-35, -40], [-35, -42], [-35, -43],
                [-35, -44], [-35, -49], [-35, -51], [-35, -53], [-35, -59], [-35, -62], [-36, -4], [-36, -8], [-36, -9],
                [-36, -12], [-36, -15], [-36, -18], [-36, -20], [-36, -22], [-36, -27], [-36, -28], [-36, -29],
                [-36, -33], [-36, -34], [-36, -35], [-36, -37], [-36, -38], [-36, -39], [-36, -40], [-36, -43],
                [-36, -44], [-36, -45], [-36, -50], [-36, -52], [-36, -54], [-36, -57], [-36, -60], [-36, -63],
                [-37, -1], [-37, -5], [-37, -10], [-37, -13], [-37, -16], [-37, -19], [-37, -21], [-37, -23],
                [-37, -28], [-37, -29], [-37, -30], [-37, -33], [-37, -34], [-37, -35], [-37, -36], [-37, -38],
                [-37, -39], [-37, -40], [-37, -44], [-37, -45], [-37, -46], [-37, -51], [-37, -53], [-37, -55],
                [-37, -58], [-37, -61], [-37, -64], [-38, -2], [-38, -6], [-38, -11], [-38, -14], [-38, -20],
                [-38, -22], [-38, -24], [-38, -29], [-38, -30], [-38, -31], [-38, -33], [-38, -34], [-38, -35],
                [-38, -36], [-38, -37], [-38, -39], [-38, -40], [-38, -45], [-38, -46], [-38, -47], [-38, -52],
                [-38, -54], [-38, -56], [-38, -59], [-38, -62], [-39, -3], [-39, -7], [-39, -12], [-39, -15],
                [-39, -21], [-39, -23], [-39, -30], [-39, -31], [-39, -32], [-39, -33], [-39, -34], [-39, -35],
                [-39, -36], [-39, -37], [-39, -38], [-39, -40], [-39, -46], [-39, -47], [-39, -48], [-39, -53],
                [-39, -55], [-39, -60], [-39, -63], [-40, -4], [-40, -8], [-40, -13], [-40, -16], [-40, -22],
                [-40, -24], [-40, -31], [-40, -32], [-40, -33], [-40, -34], [-40, -35], [-40, -36], [-40, -37],
                [-40, -38], [-40, -39], [-40, -47], [-40, -48], [-40, -54], [-40, -56], [-40, -61], [-40, -64],
                [-41, -1], [-41, -6], [-41, -9], [-41, -13], [-41, -17], [-41, -20], [-41, -25], [-41, -27], [-41, -33],
                [-41, -34], [-41, -42], [-41, -43], [-41, -44], [-41, -45], [-41, -46], [-41, -47], [-41, -48],
                [-41, -49], [-41, -50], [-41, -57], [-41, -59], [-42, -2], [-42, -7], [-42, -10], [-42, -14],
                [-42, -18], [-42, -21], [-42, -26], [-42, -28], [-42, -33], [-42, -34], [-42, -35], [-42, -41],
                [-42, -43], [-42, -44], [-42, -45], [-42, -46], [-42, -47], [-42, -48], [-42, -49], [-42, -50],
                [-42, -51], [-42, -58], [-42, -60], [-43, -3], [-43, -8], [-43, -11], [-43, -15], [-43, -19],
                [-43, -22], [-43, -25], [-43, -27], [-43, -29], [-43, -34], [-43, -35], [-43, -36], [-43, -41],
                [-43, -42], [-43, -44], [-43, -45], [-43, -46], [-43, -47], [-43, -48], [-43, -50], [-43, -51],
                [-43, -52], [-43, -57], [-43, -59], [-43, -61], [-44, -4], [-44, -12], [-44, -16], [-44, -17],
                [-44, -20], [-44, -23], [-44, -26], [-44, -28], [-44, -30], [-44, -35], [-44, -36], [-44, -37],
                [-44, -41], [-44, -42], [-44, -43], [-44, -45], [-44, -46], [-44, -47], [-44, -48], [-44, -51],
                [-44, -52], [-44, -53], [-44, -58], [-44, -60], [-44, -62], [-45, -5], [-45, -9], [-45, -13],
                [-45, -18], [-45, -21], [-45, -24], [-45, -27], [-45, -29], [-45, -31], [-45, -36], [-45, -37],
                [-45, -38], [-45, -41], [-45, -42], [-45, -43], [-45, -44], [-45, -46], [-45, -47], [-45, -48],
                [-45, -52], [-45, -53], [-45, -54], [-45, -59], [-45, -61], [-45, -63], [-46, -1], [-46, -6],
                [-46, -10], [-46, -14], [-46, -19], [-46, -22], [-46, -28], [-46, -30], [-46, -32], [-46, -37],
                [-46, -38], [-46, -39], [-46, -41], [-46, -42], [-46, -43], [-46, -44], [-46, -45], [-46, -47],
                [-46, -48], [-46, -53], [-46, -54], [-46, -55], [-46, -60], [-46, -62], [-46, -64], [-47, -2],
                [-47, -7], [-47, -11], [-47, -15], [-47, -20], [-47, -23], [-47, -29], [-47, -31], [-47, -38],
                [-47, -39], [-47, -40], [-47, -41], [-47, -42], [-47, -43], [-47, -44], [-47, -45], [-47, -46],
                [-47, -48], [-47, -54], [-47, -55], [-47, -56], [-47, -61], [-47, -63], [-48, -3], [-48, -8],
                [-48, -12], [-48, -16], [-48, -21], [-48, -24], [-48, -30], [-48, -32], [-48, -39], [-48, -40],
                [-48, -41], [-48, -42], [-48, -43], [-48, -44], [-48, -45], [-48, -46], [-48, -47], [-48, -55],
                [-48, -56], [-48, -62], [-48, -64], [-49, -1], [-49, -7], [-49, -9], [-49, -14], [-49, -17], [-49, -21],
                [-49, -25], [-49, -28], [-49, -33], [-49, -35], [-49, -41], [-49, -42], [-49, -50], [-49, -51],
                [-49, -52], [-49, -53], [-49, -54], [-49, -55], [-49, -56], [-49, -57], [-49, -58], [-50, -2],
                [-50, -8], [-50, -10], [-50, -15], [-50, -18], [-50, -22], [-50, -26], [-50, -29], [-50, -34],
                [-50, -36], [-50, -41], [-50, -42], [-50, -43], [-50, -49], [-50, -51], [-50, -52], [-50, -53],
                [-50, -54], [-50, -55], [-50, -56], [-50, -57], [-50, -58], [-50, -59], [-51, -3], [-51, -11],
                [-51, -16], [-51, -19], [-51, -23], [-51, -27], [-51, -30], [-51, -33], [-51, -35], [-51, -37],
                [-51, -42], [-51, -43], [-51, -44], [-51, -49], [-51, -50], [-51, -52], [-51, -53], [-51, -54],
                [-51, -55], [-51, -56], [-51, -58], [-51, -59], [-51, -60], [-52, -4], [-52, -12], [-52, -20],
                [-52, -24], [-52, -25], [-52, -28], [-52, -31], [-52, -34], [-52, -36], [-52, -38], [-52, -43],
                [-52, -44], [-52, -45], [-52, -49], [-52, -50], [-52, -51], [-52, -53], [-52, -54], [-52, -55],
                [-52, -56], [-52, -59], [-52, -60], [-52, -61], [-53, -5], [-53, -13], [-53, -17], [-53, -21],
                [-53, -26], [-53, -29], [-53, -32], [-53, -35], [-53, -37], [-53, -39], [-53, -44], [-53, -45],
                [-53, -46], [-53, -49], [-53, -50], [-53, -51], [-53, -52], [-53, -54], [-53, -55], [-53, -56],
                [-53, -60], [-53, -61], [-53, -62], [-54, -6], [-54, -9], [-54, -14], [-54, -18], [-54, -22],
                [-54, -27], [-54, -30], [-54, -36], [-54, -38], [-54, -40], [-54, -45], [-54, -46], [-54, -47],
                [-54, -49], [-54, -50], [-54, -51], [-54, -52], [-54, -53], [-54, -55], [-54, -56], [-54, -61],
                [-54, -62], [-54, -63], [-55, -1], [-55, -7], [-55, -10], [-55, -15], [-55, -19], [-55, -23],
                [-55, -28], [-55, -31], [-55, -37], [-55, -39], [-55, -46], [-55, -47], [-55, -48], [-55, -49],
                [-55, -50], [-55, -51], [-55, -52], [-55, -53], [-55, -54], [-55, -56], [-55, -62], [-55, -63],
                [-55, -64], [-56, -2], [-56, -8], [-56, -11], [-56, -16], [-56, -20], [-56, -24], [-56, -29],
                [-56, -32], [-56, -38], [-56, -40], [-56, -47], [-56, -48], [-56, -49], [-56, -50], [-56, -51],
                [-56, -52], [-56, -53], [-56, -54], [-56, -55], [-56, -63], [-56, -64], [-57, -1], [-57, -8], [-57, -9],
                [-57, -15], [-57, -17], [-57, -22], [-57, -25], [-57, -29], [-57, -33], [-57, -36], [-57, -41],
                [-57, -43], [-57, -49], [-57, -50], [-57, -58], [-57, -59], [-57, -60], [-57, -61], [-57, -62],
                [-57, -63], [-57, -64], [-58, -2], [-58, -10], [-58, -16], [-58, -18], [-58, -23], [-58, -26],
                [-58, -30], [-58, -34], [-58, -37], [-58, -42], [-58, -44], [-58, -49], [-58, -50], [-58, -51],
                [-58, -57], [-58, -59], [-58, -60], [-58, -61], [-58, -62], [-58, -63], [-58, -64], [-59, -3],
                [-59, -11], [-59, -19], [-59, -24], [-59, -27], [-59, -31], [-59, -35], [-59, -38], [-59, -41],
                [-59, -43], [-59, -45], [-59, -50], [-59, -51], [-59, -52], [-59, -57], [-59, -58], [-59, -60],
                [-59, -61], [-59, -62], [-59, -63], [-59, -64], [-60, -4], [-60, -12], [-60, -20], [-60, -28],
                [-60, -32], [-60, -33], [-60, -36], [-60, -39], [-60, -42], [-60, -44], [-60, -46], [-60, -51],
                [-60, -52], [-60, -53], [-60, -57], [-60, -58], [-60, -59], [-60, -61], [-60, -62], [-60, -63],
                [-60, -64], [-61, -5], [-61, -13], [-61, -21], [-61, -25], [-61, -29], [-61, -34], [-61, -37],
                [-61, -40], [-61, -43], [-61, -45], [-61, -47], [-61, -52], [-61, -53], [-61, -54], [-61, -57],
                [-61, -58], [-61, -59], [-61, -60], [-61, -62], [-61, -63], [-61, -64], [-62, -6], [-62, -14],
                [-62, -17], [-62, -22], [-62, -26], [-62, -30], [-62, -35], [-62, -38], [-62, -44], [-62, -46],
                [-62, -48], [-62, -53], [-62, -54], [-62, -55], [-62, -57], [-62, -58], [-62, -59], [-62, -60],
                [-62, -61], [-62, -63], [-62, -64], [-63, -7], [-63, -9], [-63, -15], [-63, -18], [-63, -23],
                [-63, -27], [-63, -31], [-63, -36], [-63, -39], [-63, -45], [-63, -47], [-63, -54], [-63, -55],
                [-63, -56], [-63, -57], [-63, -58], [-63, -59], [-63, -60], [-63, -61], [-63, -62], [-63, -64],
                [-64, -1], [-64, -8], [-64, -10], [-64, -16], [-64, -19], [-64, -24], [-64, -28], [-64, -32],
                [-64, -37], [-64, -40], [-64, -46], [-64, -48], [-64, -55], [-64, -56], [-64, -57], [-64, -58],
                [-64, -59], [-64, -60], [-64, -61], [-64, -62], [-64, -63]]
lnp_6 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],
         [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36], [-1], [-8], [-15], [-22], [-29], [-36], [-1, -1, 1],
         [-1, -2, 2], [-1, -3, 3], [-1, -4, 4], [-1, -5, 5], [-1, -6, 6], [-2, -7, 1], [-2, -8, 2], [-2, -9, 3],
         [-2, -10, 4], [-2, -11, 5], [-2, -12, 6], [-3, -13, 1], [-3, -14, 2], [-3, -15, 3], [-3, -16, 4], [-3, -17, 5],
         [-3, -18, 6], [-4, -19, 1], [-4, -20, 2], [-4, -21, 3], [-4, -22, 4], [-4, -23, 5], [-4, -24, 6], [-5, -25, 1],
         [-5, -26, 2], [-5, -27, 3], [-5, -28, 4], [-5, -29, 5], [-5, -30, 6], [-6, -31, 1], [-6, -32, 2], [-6, -33, 3],
         [-6, -34, 4], [-6, -35, 5], [-6, -36, 6], [-7, -1, 7], [-7, -2, 8], [-7, -3, 9], [-7, -4, 10], [-7, -5, 11],
         [-7, -6, 12], [-8, -7, 7], [-8, -8, 8], [-8, -9, 9], [-8, -10, 10], [-8, -11, 11], [-8, -12, 12], [-9, -13, 7],
         [-9, -14, 8], [-9, -15, 9], [-9, -16, 10], [-9, -17, 11], [-9, -18, 12], [-10, -19, 7], [-10, -20, 8],
         [-10, -21, 9], [-10, -22, 10], [-10, -23, 11], [-10, -24, 12], [-11, -25, 7], [-11, -26, 8], [-11, -27, 9],
         [-11, -28, 10], [-11, -29, 11], [-11, -30, 12], [-12, -31, 7], [-12, -32, 8], [-12, -33, 9], [-12, -34, 10],
         [-12, -35, 11], [-12, -36, 12], [-13, -1, 13], [-13, -2, 14], [-13, -3, 15], [-13, -4, 16], [-13, -5, 17],
         [-13, -6, 18], [-14, -7, 13], [-14, -8, 14], [-14, -9, 15], [-14, -10, 16], [-14, -11, 17], [-14, -12, 18],
         [-15, -13, 13], [-15, -14, 14], [-15, -15, 15], [-15, -16, 16], [-15, -17, 17], [-15, -18, 18], [-16, -19, 13],
         [-16, -20, 14], [-16, -21, 15], [-16, -22, 16], [-16, -23, 17], [-16, -24, 18], [-17, -25, 13], [-17, -26, 14],
         [-17, -27, 15], [-17, -28, 16], [-17, -29, 17], [-17, -30, 18], [-18, -31, 13], [-18, -32, 14], [-18, -33, 15],
         [-18, -34, 16], [-18, -35, 17], [-18, -36, 18], [-19, -1, 19], [-19, -2, 20], [-19, -3, 21], [-19, -4, 22],
         [-19, -5, 23], [-19, -6, 24], [-20, -7, 19], [-20, -8, 20], [-20, -9, 21], [-20, -10, 22], [-20, -11, 23],
         [-20, -12, 24], [-21, -13, 19], [-21, -14, 20], [-21, -15, 21], [-21, -16, 22], [-21, -17, 23], [-21, -18, 24],
         [-22, -19, 19], [-22, -20, 20], [-22, -21, 21], [-22, -22, 22], [-22, -23, 23], [-22, -24, 24], [-23, -25, 19],
         [-23, -26, 20], [-23, -27, 21], [-23, -28, 22], [-23, -29, 23], [-23, -30, 24], [-24, -31, 19], [-24, -32, 20],
         [-24, -33, 21], [-24, -34, 22], [-24, -35, 23], [-24, -36, 24], [-25, -1, 25], [-25, -2, 26], [-25, -3, 27],
         [-25, -4, 28], [-25, -5, 29], [-25, -6, 30], [-26, -7, 25], [-26, -8, 26], [-26, -9, 27], [-26, -10, 28],
         [-26, -11, 29], [-26, -12, 30], [-27, -13, 25], [-27, -14, 26], [-27, -15, 27], [-27, -16, 28], [-27, -17, 29],
         [-27, -18, 30], [-28, -19, 25], [-28, -20, 26], [-28, -21, 27], [-28, -22, 28], [-28, -23, 29], [-28, -24, 30],
         [-29, -25, 25], [-29, -26, 26], [-29, -27, 27], [-29, -28, 28], [-29, -29, 29], [-29, -30, 30], [-30, -31, 25],
         [-30, -32, 26], [-30, -33, 27], [-30, -34, 28], [-30, -35, 29], [-30, -36, 30], [-31, -1, 31], [-31, -2, 32],
         [-31, -3, 33], [-31, -4, 34], [-31, -5, 35], [-31, -6, 36], [-32, -7, 31], [-32, -8, 32], [-32, -9, 33],
         [-32, -10, 34], [-32, -11, 35], [-32, -12, 36], [-33, -13, 31], [-33, -14, 32], [-33, -15, 33], [-33, -16, 34],
         [-33, -17, 35], [-33, -18, 36], [-34, -19, 31], [-34, -20, 32], [-34, -21, 33], [-34, -22, 34], [-34, -23, 35],
         [-34, -24, 36], [-35, -25, 31], [-35, -26, 32], [-35, -27, 33], [-35, -28, 34], [-35, -29, 35], [-35, -30, 36],
         [-36, -31, 31], [-36, -32, 32], [-36, -33, 33], [-36, -34, 34], [-36, -35, 35], [-36, -36, 36]]
partial_assign = []

print("Original clause set: " + str(clauses))
print()
solution = branching_sat_solve(partial_assign, clauses)
if solution is not False:
    print("Satisfying assignment found: " + str(solution))
else:
    print("UNSAT")
