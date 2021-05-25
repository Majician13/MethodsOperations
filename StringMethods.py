import string

s = 'a little string'
print(s)
s.capitalize()
print(s.capitalize())
print(s)
print(s.center(30))
print(s.count('t'))
print(s.endswith('ing'))

t = '\ta\tdog ate my Python'
print(t.expandtabs())
print(t.find('th'))
print(t.find('pg'))
    # prints -1 if not found
print(t.index('th'))
# print(t.index('pg'))  --- Will throw a Traceback error

t = 'abcd1234'
print(t.isalnum())
t = '=+?'
print(t.isalnum())

t = 'ab12'
print(t.isalpha())
t = 'abcd'
print(t.isalpha())

t = 'ab12'
print(t.isdigit())
t = '1234'
print(t.isdigit())

s = 'abc'
print(s.islower())
s = 'ABC'
print(s.islower())

s = '   '
print(s.isspace())
s = '  a  '
print(s.isspace())

s = 'big cat'
print(s.istitle())
s = 'Big Cat'
print(s.istitle())

s = 'abc'
print(s.isupper())
s = 'ABC'
print(s.isupper())

s = 'kitty'
print(s.ljust(10))

s = '     lots of space     '
print(s.lstrip())

s = 'a big cat'
print(s.replace('big', 'tiny'))

s = 'sat a cat'
print(s.rfind('at'))
print(s.rfind('ta'))

print(s.rindex('at'))
# print(s.rindex('ta'))  --- Will throw a Traceback error

s = 'kitty'
print(s.rjust(10))

s = '     lots of space     '
print(s.rstrip())

s = 'pepperoni'
print(s.startswith('pep'))

s = '     lots of space     '
print(s.strip())

t = 'A Big Cat'
print(t.swapcase())

s = 'a big cat'
print(s.title())

t = str.translate('ABCabc', 'CBAcba') # --- NO LONGER IN PYTHON 3.9
print(t)

s = 'a big cat'
print(s.translate(t))

t = 'abc'
print(t.upper())

t = '1234'
print(t.zfill(8))

s = str('cat')
print(s)

print(str.upper(s))

s = 'kitty'
t = s.replace('i', 'a')
print(t.capitalize())

print(s.replace('a', 'i').lower())