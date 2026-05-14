# TODO

# 方法一
poker = []
for i in range(5):
    p = input()
    if p == 'J':
        poker.append(11)
    elif p == 'Q':
        poker.append(12)
    elif p == 'K':
        poker.append(13)
    elif p == 'A':
        poker.append(1)
    else:
        poker.append(int(p))

print(sum(poker))

# 方法二
# poker = 0
# for i in range(5):
#     p = input()
#     if p == 'J':
#         poker+=11
#     elif p == 'Q':
#         poker+=12
#     elif p == 'K':
#         poker+=13
#     elif p == 'A':
#         poker+=1
#     else:
#         poker+=int(p)
#
# print(poker)
