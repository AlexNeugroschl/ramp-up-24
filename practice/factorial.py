def calculate_factorials(num:int):
    print(loop(num))
    print(recursive(num))

def loop(num:int):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    return factorial

def recursive(num:int):
    if num == 0:
        return 1
    return num * recursive(num - 1)

calculate_factorials(2)