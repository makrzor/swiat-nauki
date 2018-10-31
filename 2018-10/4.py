#!/apps/public/bin/python

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
positions = {}

for A in DIGITS:
    if A == 0:
        continue
    for B in DIGITS:
        for C in DIGITS:
            for D in DIGITS:
                for E in DIGITS:
                    if (10000 * A + 1000 * B + 100 * C + 10 * D + E) == 45 * A * B * C * D * E:
                        print("{0}{1}{2}{3}{4} == 45 * {0} * {1} * {2} * {3} * {4}\n".format(A, B, C, D, E))
exit(0)
