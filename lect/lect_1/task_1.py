# name = 'Alex'
# a = 42 * 3.141592 / 2.71828
# b = 3
# print(a, b, sep='\n')
# res = int(input('enter something: '))
# print(1 + res)
# MAX_DATE = 13
# MAX_DATE += 1
# data = ["key", 3, 5, 29]
# while True:
#     key = input('input: ')
#     if key.isdigit():
#         key = int(key)
#     if key in data:
#         print("yes")
#     else:
#         data.append(key)
# num = int(input('enter: '))
# answer = True if num % 2 == 0 else False
# print(answer)

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for i in range (0, 12, 2):
#     print(i)

data = 0
while data < 100:
    data += 1
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
        break
else:
    data += 5
print(data)
