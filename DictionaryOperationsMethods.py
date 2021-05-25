d = {1:2, 3:'pig', 'goat': 74.59999999999994, 'rabbit':'hostile'}
print(d)

# len(d) (length of dictionary operation)
print(d)
print(len(d))

# d[k] (get datum dictionary operation)
print('Get datum dictionary operation, print(d), print(d[1]), print(d[3]), print(d["goat"]), print(d["rabbit"]): ')
print(d)
print(d[1])
print(d[3])
print(d['goat'])
print(d['rabbit'])
# print(d[0]) will throw a Traceback error due to 0 not being a key value in the dictionary.

# d[k]=x (set datum dictionary operation)
print('Set datum dictionary operation, d["ox"]=128 and d["goat"]=32: ')
print(d)
d['ox']=128
d['goat']=32
print(d)

# del d[k] (delete datum dictionary operation)
print(d)
del d['goat']
print('del d["goat"]: ')
print(d)

# d.clear() (clear dictionary method)
d4 = {1:'box', 2:'sox'}
print(d4)
d4.clear()
print('d4.clear(): ')
print(d4)

# k in d (is a key of dictionary operation)
print(d)
print('Rabbit in d: ')
print('rabbit' in d)
print('Plabbit in d: ')
print('plabbit' in d)

# k not in d (is not a key of dictionary operation)
print('Rabbit not in d: ')
print('rabbit' not in d)
print('Plabbit not in d: ')
print('plabbit' not in d)

# d.items() (list key-datum pairs dictionary method)
print(d)
l = d.items()
print('Printing list l=d.items(): ')
print(l)

# d.keys() (list keys dictionary method)
print(d)
m = d.keys()
print('printing m=d.keys(): ')
print(m)

# For statements with Dictionaries
print(d)
print('printing for x in d: ')
for x in d:
    print(x)
# end for

print('printing both key, datum using for x in d print(x, d[x]): ')
for x in d:
    print(x, d[x])
# end for

# Various ways to print out dictionaries

print('print([k for k in d])')
print([k for k in d])

print('print([d[k] for k in d])')
print([d[k] for k in d])

print('print ([(k, d[k]) for k in d])')
print ([(k, d[k]) for k in d])