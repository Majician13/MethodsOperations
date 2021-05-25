p = [(7, 4), (3, 5), (2, 4)]
t = [x*y for x, y in p]
print(t)

m = [7, 3, 2]
n = [4, 5, 4]
print([x*y for x, y in zip(m, n)])
print([x*y/z for x,y,z in zip(m,n,range(2,5))])

def fn36(x,y):
    if None == x: return y
    if None == y: return x
    return y/(x+1.0)

print([fn36(x,y) for x,y in enumerate(n)])
print(list(map(fn36,range(3),n)))

# Per-Element Conditionals
def fnF1(x):
    if 3 == x: return False
    if x <= 5: return True
    if x <= 7: return False
    return True

print([x for x in range(10) if fnF1(x)])

v = (2, 7, 5)
print([x for x in range(10) if x not in v])

def fnF2(x,y):
    if 2 == x: return False
    if ((x>3) and (x <=6)): return False
    if 5 == y: return False
    if 7 == y: return False
    return True
print([x*y for x,y in enumerate(range(2,11)) if fnF2(x,y)])

# Nested List Comprehensions
print([x+1 for x in [y*y for y in range(6)] if x not in (9,16)])

# Convolution
t = (1, 5, 7)
u = (2, 3, 4)
print([(x,y) for x in t for y in u])

print([(x,y) for x in t for y in u if x*y < 20])

print([x+y for x in t for y in u if x*y < 20])

u = (2, 3, 4)
v = (6, 8)
print([(x,y) for x in t for y in v])

t = (1, 5, 7)
u = (2, 3, 4)
v = (6, 8)
print([(x,y,z) for x in t for y in u for z in v])

# a Word about Print
m = ['a', 'b', 'c']
for x in m:
    print(x)

for x in m:
    print(x, end = '')
    print(x, sep = ' y')