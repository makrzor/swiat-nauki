#!/apps/public/bin/python

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
positions = {}

for A in DIGITS:
    if A == 0:
        continue
    positions["A"] = DIGITS.index(A)
    DIGITS.remove(A)
    for B in DIGITS:
        positions["B"] = DIGITS.index(B)
        DIGITS.remove(B)
        number_core = 100 * A + 10 * B
        for C in DIGITS:
            positions["C"] = DIGITS.index(C)
            DIGITS.remove(C)
            if (number_core + C) % 2 == 0:
                for D in DIGITS:
                    positions["D"] = DIGITS.index(D)
                    DIGITS.remove(D)
                    if (number_core + D) % 3 == 0:
                        for E in DIGITS:
                            positions["E"] = DIGITS.index(E)
                            DIGITS.remove(E)
                            if (number_core + E) % 4 == 0:
                                for F in DIGITS:
                                    positions["F"] = DIGITS.index(F)
                                    DIGITS.remove(F)
                                    if (number_core + F) % 5 == 0:
                                        for G in DIGITS:
                                            positions["G"] = DIGITS.index(G)
                                            DIGITS.remove(G)
                                            if (number_core + G) % 6 == 0:
                                                for H in DIGITS:
                                                    positions["H"] = DIGITS.index(H)
                                                    DIGITS.remove(H)
                                                    if (number_core + H) % 7 == 0:
                                                        for I in DIGITS:
                                                            positions["I"] = DIGITS.index(I)
                                                            DIGITS.remove(I)
                                                            if (number_core + I) % 8 == 0:
                                                                for J in DIGITS:
                                                                    positions["J"] = DIGITS.index(J)
                                                                    if (number_core + J) % 9 == 0:
                                                                        print("2| {}{}{}".format(A, B, C))
                                                                        print("3| {}{}{}".format(A, B, D))
                                                                        print("4| {}{}{}".format(A, B, E))
                                                                        print("5| {}{}{}".format(A, B, F))
                                                                        print("6| {}{}{}".format(A, B, G))
                                                                        print("7| {}{}{}".format(A, B, H))
                                                                        print("8| {}{}{}".format(A, B, I))
                                                                        print("9| {}{}{}\n".format(A, B, J))
                                                            DIGITS.insert(positions["I"], I)
                                                    DIGITS.insert(positions["H"], H)
                                            DIGITS.insert(positions["G"], G)
                                    DIGITS.insert(positions["F"], F)
                            DIGITS.insert(positions["E"], E)
                    DIGITS.insert(positions["D"], D)
            DIGITS.insert(positions["C"], C)
        DIGITS.insert(positions["B"], B)
    DIGITS.insert(positions["A"], A)
exit(0)
