def interview(lst, tot):
    if len(lst) < 8:
        return "unqualified"
    if lst[0] > 5 or lst [1] > 5:
        return "unqualified"
    if lst[2] > 10 or lst [3] > 10:
        return "unqualified"
    if lst[4] > 15 or lst [5] > 15:
        return "unqualified"
    if lst[6] > 20 or lst [7] > 20:
        return "unqualified"
    if tot > 120:
        return "unqualified"
    return "qualified"

print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))