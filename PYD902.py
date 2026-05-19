f = open("read.txt")
# TODO

# 1
# result = [int(i) for i in f.read().split()]
# print(sum(result))

# 2
# print(sum([int(i) for i in f.read().split()]))

# 3
data = f.read()
data_list = data.split()
data_list_int = [int(i) for i in data_list]
print(sum(data_list_int))