

def FibonacciSum(x):
    Fn_2 = 0
    Fn_1 = 1
    sum = 0
    while True:
        Fn = Fn_1 + Fn_2
        if Fn >= x: return sum
        if Fn % 2 == 0: sum += Fn
        Fn_2, Fn_1 = Fn_1, Fn
    

final = FibonacciSum(4000000)
print(final)