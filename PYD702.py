# TODO
t1 = ()
t2 = ()

print("Create tuple1:")
# TODO
while True:
    n = int(input())
    if n == -9999:
        break
    t1 += (n,)
print("Create tuple2:")
# TODO
while True:
    n = int(input())
    if n == -9999:
        break
    t2 += (n,)


"""
Combined tuple before sorting: _
Combined list after sorting: _
"""
print(f'Combined tuple before sorting: {t1+t2}')
print(f'Combined list after sorting: {sorted(t1+t2)}')
