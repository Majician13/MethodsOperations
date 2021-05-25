a = [1, 2, 3, 4, 7]
print(a)

b = ['abc', 'def', 'ratty', 'catty']
print(b)

c = [1, 4, 7, True, 'abc', [1, 7, 'xyz']]
print(c)

print(type(a))
print(callable(a))

print(2 in a)
print([2, 3] in a)
print([1, 7, 'xyz'] in c)

print(4 not in a)
print(5 not in a)

print(a)
print(b)
print(a+b)

print(3*a)
print(b*2)

print(c)
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])

print(c[1:3])
print(c[1:2])
print(c[1:1])

print(a)
print(a[1:5:2])

print(len(a))
print(len(b))
print(len(c))

print(min(a))
print(min(b))
# print(min(c))  --- Throws Traceback error

print(max(a))
print(max(b))
# print(max(c))  --- Throws Traceback error

