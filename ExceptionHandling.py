d = {1:2, 3:'pig', 'goat': 74.59999999999994, 'rabbit':'hostile'}
print(d)

try:
    d['ef']
except KeyError:
    print('Oops!')
finally:
    print('Hey!')
