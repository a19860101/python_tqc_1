f_name = input()
str_old = input()
str_new = input()
#TODO
print("=== Before the replacement")

# data = open(f_name)
# result = data.read()

result = open(f_name).read()
print(result)
#TODO

print("=== After the replacement")
#TODO
print(result.replace(str_old, str_new))
