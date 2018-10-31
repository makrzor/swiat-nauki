#!/apps/public/bin/python

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
positions = {}

for A in DIGITS:
    positions["A"] = DIGITS.index(A)
    if positions["A"] == 6:
        break
    DIGITS.remove(A)
    for B in DIGITS[positions["A"]:]:
        positions["B"] = DIGITS.index(B)
        if positions["B"] == 7:
            break
        DIGITS.remove(B)
        for C in DIGITS[positions["B"]:]:
            positions["C"] = DIGITS.index(C)
            if positions["C"] == 8:
                break
            DIGITS.remove(C)
            for D in DIGITS[positions["C"]:]:
                if (A + B + C + D) % 7 == 0:
                    numbers = [1000 * A + 100 * B + 10 * C + D, 1000 * A + 100 * B + 10 * D + C,
                                1000 * A + 100 * C + 10 * B + D, 1000 * A + 100 * C + 10 * D + B,
                                1000 * A + 100 * D + 10 * B + C, 1000 * A + 100 * D + 10 * C + B,
                                1000 * B + 100 * A + 10 * C + D, 1000 * B + 100 * A + 10 * D + C,
                                1000 * B + 100 * C + 10 * A + D, 1000 * B + 100 * C + 10 * D + A,
                                1000 * B + 100 * D + 10 * A + C, 1000 * B + 100 * D + 10 * C + A,
                                1000 * C + 100 * A + 10 * B + D, 1000 * C + 100 * A + 10 * D + B,
                                1000 * C + 100 * B + 10 * A + D, 1000 * C + 100 * B + 10 * D + A,
                                1000 * C + 100 * D + 10 * A + B, 1000 * C + 100 * D + 10 * B + A,
                                1000 * D + 100 * A + 10 * B + C, 1000 * D + 100 * A + 10 * C + B,
                                1000 * D + 100 * B + 10 * A + C, 1000 * D + 100 * B + 10 * C + A,
                                1000 * D + 100 * C + 10 * A + B, 1000 * D + 100 * C + 10 * B + A]
                    count = 0
                    for number in numbers:
                        if number % 7 != 0:
                            count += 1
                        else:
                            break
                    if count == 24:
                        print(A, B, C, D)
            DIGITS.insert(positions["C"], C)
        DIGITS.insert(positions["B"], B)
    DIGITS.insert(positions["A"], A)
exit(0)
