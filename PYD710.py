#TODO

    #Key: (後方有一空白格)
    # key = input("Key: ")
    
    #Value: (後方有一空白格)
    # value = input("Value: ")

d = {}
while True:
    key = input("Key: ")
    if key == 'end':
        break
    value = input("Value: ")
    d[key] = value

search = input('Search key: ')
print(search in d)