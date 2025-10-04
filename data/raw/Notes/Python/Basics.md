# Data Types

## Int
## Float
2727.0  
-9.7  
## String
'hello'  
"hello"  
'"hello"'  
"4.6"  

## Bool
True  
False  

### Basic Functions

```python
print("hello world!")
print(4.5, "hello")  # add a space in between
print(4.5)

print("hello", end='\n')  # add the line break at the end
# default is also line break
```

# Variables

```python
hello = 'tim'
world = "world"
world = hello
hello = 'no'

print(hello, world)  # print no hello
# default is the deep copy
```

# Input

```python
some_variable = input('Name: ')  # default input is in string type
print(some_variable)
```

# Arithmetic Operations

```python
x = 9
y = 3
result = x / y
print(result)  # prints 3.0
print(int(result))  # prints 3

print(x // y)  # prints 3

x = "hello"
y = 3
print(x * y)  # prints hellohellohello
```

# Type

```python
print(type(var))
```

# Method

```python
hello = "hello".upper()
print(hello)  # prints HELLO
```

# Conditional Operator

```python
print('a' > 'Z')  # compares using the int value representations
print('ab' > 'ad')  # compares from left to right character
```

result1 = True
result2 = False
result3 = True
result4 = result1 or result2 or result3
print(not False)

precedance not -> and -> or

# Collections

## list
x = [4, "t"]
print(len(x))

x.append(True)
// adds at the end

x.extend([2,3,4])
// adds all element at the end of the list

x.pop()
// returns and remove the last element of the list

x.pop(2)
// return and remove value on and index in the list

List stores the reference the the element stores in it. 
y = x
x[0] = "hello"
// makes the update to the list y as well. 
y = x[:]
// makes a deep copy of the list. 


## tuple

c = (4,5,6)

its immutable

# Look

for i in range(10):
    print(i)

range (start, stop, step)

x = [3,4,5,6,7]

for i, element in enumerate(x):
    print(i, element). // print element and the index

# Slice

x = [1,2,3,4,5,6,7,8]
s = 'hello' 

sliced = x[0:4:2]
// slice[start:stop:step]

# Set

x = set() // this is set
y = {} // this is dictionary
s = {4,32,2,2} // this is set
s2 = [1,2,3,4,4]
s.remove(5) // give key error

print(4 in s) // check if it is in set or not. complexity - O(1)
print(3 in s2) // linear complexity O(n) 

# Dictionary

x = {'key': 4}
x[2] = [1,2,3,4]

print('key' in s) // checks if the key exist in dictionary.
print(list(x.values())) // return the list of values in dictionary.
print(list(x.keys()))

del x['key']

for key, value in x.items():
    print(key, value)

for key in x:
    print(key, x[key])

# Comprehensions

```python
x = [x for x in range(5)]
print(x)  # [0, 1, 2, 3, 4]

x = [x + 5 for x in range(5)]
print(x)  # [5, 6, 7, 8, 9]
```

# Function

```python
def func():
    print('Run')

def func(x, y, z=None):
    print("Run", x, y)
    return x * y, x / y

print(func(5, 6))  # prints in form of tuple
r1, r2 = func(5, 6)
```

# Args & **kwargs

kwargs = keyword arguments
def func(x):
    def func2():
        print(x)
    return func2
func(3)()
// print 3

def func(*args, **kwargs):
    pass

x = [1,2,3,4]
print(x)
print(*x)

// [1, 2, 3, 4]
// 1 2 3 4


def func(x, y):
    print(x, y)

pairs = [(1, 2), (3, 4)]

for pair in pairs:
    func(pair[0], pair[1]) // naive
    func(*pair) // python way

// single * is for tuple or list
// double ** is for dictionary

func(**{'x': 2, 'y': 5})

def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4,5, one=0, two=1)

// print (1,2,3,4,5) {'one': 0, 'two': 1}

# Scope and Global

```python
x = 'tim'

def func(name):
    x = name  # local

print(x)
func('changed')
print(x)  # tim, tim

def func(name):
    global x
    x = name  # global

print(x)
func('changed')
print(x)  # tim, changed
```

# Exception

```python
try:
    x = 7 / 0
except Exception as e:
    print(e)








