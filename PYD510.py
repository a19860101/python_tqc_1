# TODO
def compute(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return compute(n-1) + compute(n-2)

n = int(input())
for i in range(n):
    print(compute(i),end=' ')