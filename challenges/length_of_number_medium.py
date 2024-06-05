def number_length(num):
    string = str(num)
    digits = 0
    for i in string:
        digits += 1
    return digits
print(number_length(56))