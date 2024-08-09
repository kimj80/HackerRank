def is_leap(year):
    leap = False

    # cond 1, 2, 3
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap