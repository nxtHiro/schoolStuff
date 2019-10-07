zero = 0
for i in range(1, 1000001):
    intVal = [int(j) for j in str(i)]
    for x in range(len(intVal)):
        if (intVal[x]==0):
            zero += 1
print zero
