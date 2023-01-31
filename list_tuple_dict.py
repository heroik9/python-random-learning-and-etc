# list = ["kazkodel"]
# list.append("kazkas")
# print(list[0], list)
# print(len(list))
# a = input("value: ")
# for i in list:
#     if i == a:
#         print("no no")
#
# a, b, c = (1, 2, 3)
# print(a)
#
# a = (1, 2, 3)
# print(a[0])
#
# for i in a:
#     print(i)
#
dict = {"M7": 6, "M8": 7}
dict.update({"M9": 6})
print(dict)
dict2 = {"h7": 8, "h8": 9}
dicts = {}
dicts.update(dict)
dicts.update(dict2)
print(dicts)
#
#
# a = int(input("Enter value: "))
#
# b = int(input("Enter value: "))
#
# for x, y in dicts.items():
#     if a == y:
#         for c, v in dicts.items():
#             if b == v:
#                 print("Bearing tolerance - {}, {}.".format(x, c))


list = [1, 2, 3, 4, 5]

print (list)
list.reverse()
print(list)

a = int(input("value: "))

for i in list:
    if a == i:
        list.pop(2)
        print(list)
        list.clear()
        print(list)
        list.append(8)
        print(list)

name = [1, 2, 3, 4, 5]


print(name[::-2])
print(name[::-3])
print(name[1:3])
print(name[::3])
print(name[1:4:2])
print(name[:3])
print(name[2:])







