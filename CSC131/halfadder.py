def halfAdd(a, b):
    s = 0
    c = 0
    if (a == 1 and b == 1):
        s = 0
        c = 1
    elif (a == 1 or b == 1 and a != b):
        s = 1
        c = 0
    return c, s

print halfAdd(1, 1)
print halfAdd(1, 0)
print halfAdd(0,1)
print halfAdd(0,0)
