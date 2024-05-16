# print(23891471923807487.142352314353455 + 23891471923843245.142352314334563 >
# 23891471923807487.142352314356734 + 23891471923843245.142352314334553)

a = 5
b = 3 + 2
c = [5]
print(id(a), id(b), a == b, a == c[0], c[0] == b)
print(a.__eq__(b))
print(a is b)

age = input('your age: ')
print(age, type(age))
age = int(input('your age: '))
print(age, type(age))
