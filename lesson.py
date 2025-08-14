a = "test"
b = a
c = b

print(c)

num = 1
name = '1'
is_ok = True

new_num = int(name)

print(num , type(num))
print(name, type(name))
print(is_ok, type(is_ok))

print(new_num, type(new_num))

print('Hi', 'Mike' , sep=',', end='\n')
print('Hi', 'Mike' , sep=',', end='\n')

import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

# print(help(math))

print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello.\nHow are you?')
print(r'C:\name\name')

print("###############")
print("""\
line 1
line 2
line 3\
""")
print("###############")

print('Hi' * 3 + 'Mike')

s = ('aaaaa'
     'bbbbb')

print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:])

word = 'j' + word[1:]
print(word)
n = len(word)
print(n)

s = 'My name is Mike. Hi Mike'
print(s)
is_start = s.startswith('My')
print (is_start)
is_start = s.startswith('X')
print (is_start)

print('############')

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

s = 'My name is {0} {1}. Watashi ha {1} {0}'.format('Azuki' , 'Melon>')
print(s)
s = 'My name is {name} {family}. Watashi ha {family} {name}'.format(name='Azuki' , family='Melon')
print(s)

name = 'Azuki'
family = 'Melon'
print(f'My name is {name} {family}. Watashi ha {family} {name}')

l = [1, 20, 4, 50, 6, 8]
print(l)
print(l[0])
print(l[3:])
n = [1, 2, 3, 4, 5, 6]
print(n[::2])
print(n[::-1])

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
s[0] = 'x'
print(s)
s[2:5] = ['x', 'y', 'z']
print(s)
print(s[:])

s.append('w')
print(s)
s.insert(0, 'A')
print(s)
print(s.pop())
print(s)
print(s.pop(0))
print(s)
del s[1]
print(s)
s.remove('x')
print(s)

a = [1, 2, 3]
b = [4, 5, 6]
x = a + b
print(x)
a += b
print(a)
a.extend(b)
print(a)

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

X = ' '.join(to_split)
print(X)

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('i =', i)
print('j =', j)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('x =', x)
print('y =', y)

count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')

#while True:
#    word = input('Enter:')
#    if word == 'ok':
#        break
#    print('next')

some_list = [1, 2, 3, 4, 5]

for i in some_list:
    print(i)
else:
    print('done')

for i in range(2, 12, 3):
    print(i)

for _ in range(2):
    print('hello')

for i, fruit in enumerate(['apple', 'orange', 'banana']):
    print(i, fruit)

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
fruits = ['apple', 'orange', 'banana']
drinks = ['milk', 'coffee']

for days, fruits, drinks in zip(days, fruits, drinks):
    print(days, fruits, drinks)


d = {'x' : 1, 'y' : 2, 'z' : 3}

for k, v in d.items():
    print(k, ':', v)

def say_hello():
    s = 'hello'
    return s

f = say_hello()
print(f)

def say_hello2(word):
    print(word)

say_hello2('hello World')

# 以下のように宣言はできるが、別にstr型も代入出来るので、あまり明示しない
def add_num(a: int, b: int) -> int:
    return a + b

def menu(entree='beef', drink='milk', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)

menu(drink='coffee')

# これはやらないように
def test_func(x, l=[]):
    l.append(x)
    return l
r = test_func(100)
print(r)
r = test_func(100)
print(r)

def say(word, *args):
    print('word = ', word)
    for arg in args:
        print(arg)

say('HI', 'Mike', 'Nance')

def menu (**kwargs):
    for key, value in kwargs.items():
        print(key, value)

d = {
    'entree' : 'beef',
    'drink' : 'milk',
    'dessert' : 'ice'
}
menu(**d)

def example_func(pram1, pram2):
    """
    Example function with types documented in the docstring.

    Args:
        :param1 (int): The first parameter.
        :param2 (str): The second parameter.

    Returns:
        bool: The return value.True for success.
    """

    print(pram1)
    print(pram2)
    return True

print(example_func.__doc__)

def circle_area_func(pi):
    def circle_ares(radius):
        return pi * radius * radius
    return circle_ares

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

#f = print_info(add_num)
#r = f(10, 20)
#print(r)

r = add_num(30, 50)

l = ['Mon', 'tue', 'Wed', 'thu', 'fri']

def change_words(words, func):
    for word in words:
        print(func(word))

change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())
