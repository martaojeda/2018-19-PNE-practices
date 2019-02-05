def count_bases(s):
    """Counting the number of As, Cs, Gs and Ts in the string"""

    result_a = 0
    result_c = 0
    result_g = 0
    result_t = 0
    for b in s:
        if b == "A":
            result_a += 1
        elif b == "C":
            result_c += 1
        elif b == "G":
            result_g += 1
        elif b == "T":
            result_t += 1
    return dict(As= result_a, Cs= result_c, Gs= result_g, Ts= result_t)

