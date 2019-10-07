# NOT

# input A
# output Y

def Not(A):
    TT = {0:1, 1:0}
    Y = TT[A]
    return Y

# test
print(Not(0))
print(Not(1))
