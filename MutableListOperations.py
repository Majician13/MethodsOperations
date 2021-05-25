a = [2, 1, 7, 5, 3, 19]
a[2] = 13
print(a)

a[2:4] = [21, 27]
print(a)

del a[2:4]
print(a)

a = [2, 1, 7, 5, 3, 19]
a[1:6:2] = [21, 15, 4]
print(a)

a = [2, 1, 7, 5, 3, 19]
del a[1:6:2]
print(a)

a = [2, 1, 7, 5, 3, 19]
a.append(13)
print(a)

a = [2, 1, 7, 5, 3, 19]
a.extend([6, 9, 12])
print(a)

a = [2, 1, 7, 5, 3, 19]
print(a.count(7))

a = [2, 1, 7, 5, 3, 19]
print(a.index(7))

a = [2, 1, 7, 5, 3, 19]
a.insert(3, 12)
print(a)

a = [2, 1, 7, 5, 3, 19]
print(a.pop())
print(a)

a = [2, 1, 7, 5, 3, 19]
a.remove(5)
print(a)

a = [2, 1, 7, 5, 3, 19]
a.reverse()
print(a)

a = [2, 1, 7, 5, 3, 19]
a.sort()
print(a)

s = list([1, 5, 2, 3])
print(s)

list.reverse(s)
print(s)

s = 'big red dog sly brown fox'
print(s.split())

s = 'big red dog sly brown fox'
b = s.split()[2:5]
print(b)

b = s.split()[2:5].sort()
print(b)

s = 'big red dog sly brown fox'
b = sorted(s)
print(b)
print(type(b))


