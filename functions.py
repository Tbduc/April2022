import array


def userSum(a, b):
    sum = a + b
    return sum

print(userSum(10, 10))
print(4%16)
for i in range(5):
    for j in range(5):
        sum = userSum(i, j)
        print("%s + %s = %s" % (i, j, sum))