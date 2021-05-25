# d.copy() (shallow copy dictionary method)
da = {'goat':12, 'shoat':4}
print(da)
db = da
print('db = da')
db['goat'] = 16
print('db["goat"] = 16')
print('print db: ')
print(db)
print('print da: ')
print(da)

print('dc = da.copy()')
dc = da.copy()
dc['goat'] = 21
print('dc["goat"]=21')
print('print da: ')
print(da)
print('print dc: ')
print(dc)

print("printing ID(da): ", id(da))
print("printing ID(db): ", id(db))
print("printing ID(dc): ", id(dc))

# d.update(d2) (update with iterable dictionary method)
d = {'pig':3, 'big':4, 'fig':27, 'wig':-7}
print('print d: ', d)
d2 = {'pig':7, 'gig':18}
print('print d2: ', d2)
d.update(d2)
print('print d.update(d2): ', d)

t3=(('wig', 3),)
print('Print t3: ', t3)
d.update(t3)
print('Print d.update(t3): ', d)

# d.fromkeys(seq[,value]) (create new dictionary class method)
print(d)
m = ['pop', 'stop', 'shop']
print('print m: ', m)
d3 = d.fromkeys(m)
print('print d3 = d.fromkeys(m): ', d3)
print('original dictionary is unchanged: ', d)
print('print m', m)
d4 = d.fromkeys(m, 0)
print('d4 = d.fromkeys(m, 0): ', d4)
print('print m: ', m)
d5 = dict.fromkeys(m, -3)
print('d5=dict.fromkeys(m, -3): ', d5)

print('print d: ', d)
d6 = dict.fromkeys(d, 0)
print('d6 = dict.fromkeys(d, 0): ', d6)
d7 = dict.fromkeys('box')
print('d7 = dict.fromkeys("box"): ', d7)
t2 = ('wig', 3)
print('print t2: ', t2)
d8 = dict.fromkeys(('wig', 'fig'))
print('d8 = dict.fromkeys(("wig", "fig")): ', d8)

# d.values() (list datum values dictionary method)
print("print d: ", d)
m2 = d.values()
print('m2 = d.values(): ', m2)

# d.get(k[,x]) (get datum with default dictionary method)
print('print d: ', d)
print("print d.get(gig): ", d.get('gig'))
print("print d.get(plig): ", d.get('plig'))
print("print d.get(whig, -1): ", d.get('whig', -1))

# d.setdefault(k[,x]) (set/get datum with default dictionary method)
d1 = {'a':2, 'c':4, 'b':3}
print('d1.setdefault("a", 7): ', d1.setdefault('a', 7))
print('print d1: ', d1)
print('d1.setdefault("a"): ', d1.setdefault('a'))

# d.pop(k[,x]) (pop datum with default dictionary method)
d1 = {'a':2, 'c':4, 'b':3, 'e':None, 'd':5}
print('print d1: ', d1)
d1.pop('e')
print('print d1 pop(e): ', d1)
d1.pop('d')
print('print d1.pop(d): ', d1)
# the following prevents an error by setting default for an object that isn't in the dictionary
print(d1.pop('f', -1))
print('print d1 pop(f, -1): ', d1)

# iter(d.items() (key-datum iterator dictionary method)
print('print d1: ', d1)
ikd = iter(d1.items())
print('print ikd: ', ikd)

# iter(d.items() (using for loop)
print('print ikd: ', ikd)
for t in ikd:
    print('print t for t in ikd: ', t)
# end for

# once used, this kind of iterator cannot be re-used, but instead behaves as if empty:
print('running for loop again: ')
for t in ikd:
    print('print t for t in ikd again: ', t)
# end for
# re-initialize ikd list
ikd = iter(d1.items())
print('print t for t in ikd: ', [t for t in ikd])

# iter(d.keys() (key iterator dictionary method)
print('print d1: ', d1)
ik = iter(d1.keys())
for k in ik:
    print('print for k in ik = iter(d1.keys()): ', k)
# end for

# iter(d.values() (datum iterator dictionary method)
print('print d1: ', d1)
id = iter(d1.values())
for v in id:
    print('print v for v in id = iter(d1.values()): ', v)
# end for
