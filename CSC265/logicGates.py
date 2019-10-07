def nand(a, b):
    TT = {
    (0,0):1,
    (0,1):1,
    (1,0):1,
    (1,1):0
    }
    Y = TT[(a,b)]
    return Y

print(nand(1,0))
print(nand(1,1))
