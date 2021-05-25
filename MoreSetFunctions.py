# enumerate()
m = ['pig', 'cat', 'dog']
for t in m:
    print(t)

i = 0
for t in m:
    if 'dog' == t:
        m[i] = 'hog'
    i += 1
print(m)

e = enumerate(m)
print(e)
print(callable(e))
print(type(e))
for t in e:
    print(t)
v = [t for t in enumerate(m)]
print(v)
for i, t in enumerate(m):
    if 'pig' == t:
        m[i] = 'duck'
print(m)

s = 'Cat'
n = [t for t in enumerate(s)]
print(n)

# the following for statement throws a traceback error 'str' due to enumerate can only be used once.
#for i, c in enumerate(s):
    #if 'a' == c:
        #s[i] = 'o'

d = {'a':4, 'b':5}
e = enumerate(d)
print(e)
n = [t for t in enumerate(d)]
print(n)
d[0] = 'x'
print(d)

# the following for statement throws a traceback error dictionary changed size during iteration.
#d = {'a':4, 'b':5}
#for i, k in enumerate(d):
    #if 'a' == k:
        #d[i] = 7
# Filter Function
# in python 2 this worked, in Python 3, the equivalent is: list(filter(func,data))

print('filter function ------')
def fn(x):
    if 2 == x: return False
    return True
print(filter(fn, range(5)))
print(list(filter(fn, range(5))))

def fn2(x):
    if 2 == x: return False
    if ((x >= 9) and (x <= 15)): return False
    return True
m = list(filter(fn2, range(20)))
print(m)
n = list(filter(fn2, [x+0.1 for x in range(20)]))
print(n)

#join()
s1 = ' ' 
s2 = '   '
s3 = '\t'
s4 = '\n'
s5 = 'a'
t = ['rat', 'cat', 'sat', 'hat']
t1 = s1.join(t)
print(t1)
t2 = s2.join(t)
t3 = s3.join(t)
t4 = s4.join(t)
t5 = s5.join(t)
print(t2)
print(t3)
print(t4)
print(t5)

#map
def fnM1(a):
    if 3 == a: return 0
    return a*3
print(list(map(fnM1, range(6))))

p = list(map(fnM1, filter(fn2, range(20))))
print(p)

def fnM2(a, b, c):
    if None == a: return None
    if None == b: return None
    if None == c: return None
    if 0 == c: return 'Oops'
    return a*b/c
t1 = (7, 8, 2)
print(list(map(fnM2, t1, range(2, 6), range(0, 4))))

#zip
print(list(zip(t1, range(2, 6), range(0, 4))))
print(list(zip(range(3), t1)))
print([x for x in enumerate(t1)])