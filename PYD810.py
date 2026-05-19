# TODO

n = int(input())

for i in range(n):
    k = input()
    klist = [float(i) for i in k.split()]
    result = max(klist) - min(klist)
    print(f'{result:.2f}')