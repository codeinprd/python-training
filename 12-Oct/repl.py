C:\Windows\System32>python
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x=2
>>> exit()

C:\Windows\System32>python
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x=2
>>> 2a='ram'
  File "<stdin>", line 1
    2a='ram'
    ^
SyntaxError: invalid decimal literal
>>> x-y=3
  File "<stdin>", line 1
    x-y=3
    ^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> x-Y=3
  File "<stdin>", line 1
    x-Y=3
    ^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> x_Y=3
>>> is_variable=4
>>> _is_variable=4
>>> 4_is_variable=4
  File "<stdin>", line 1
    4_is_variable=4
     ^
SyntaxError: invalid decimal literal
>>>
>>>
>>> '4_is_variable'.isidentifier()
False
>>>
>>>
>>> '_is_variable'.isidentifier()
True
>>> print =4
>>> print(''hello)
  File "<stdin>", line 1
    print(''hello)
          ^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> def hello_world():
...     print('hello world')
...
>>> hello_world()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in hello_world
TypeError: 'int' object is not callable
>>> exit()

C:\Windows\System32>python
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def hello_world():
...     print('testing')
...
>>> hello_world()
testing
>>> x=4
>>> x
4
>>> type(x)
<class 'int'>
>>> y='ram'
>>> type(y)
<class 'str'>
>>> x
4
>>> id(x)
140723780375432
>>> del x
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> x=9
>>> x
9
>>> id(x)
140723780375592
>>> y1=23.45
>>> type(y)
<class 'str'>
>>> type(y1)
<class 'float'>
>>>
>>>
>>> print(type(y1))
<class 'float'>
>>> 2+2
4
>>> x='ram'
>>> x[0]
'r'
>>> x=['ram','krishna']
>>> x
['ram', 'krishna']
>>> type(x)
<class 'list'>
>>> len(x)
2
>>> x[0]
'ram'
>>> x[1]
'krishna'
>>> for x in x:
... for x1 in x:
  File "<stdin>", line 2
    for x1 in x:
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for x1 in x:
...     print(x1)
...
ram
krishna
>>> y1=['ram',23,True]
>>> y1
['ram', 23, True]
>>> x=5
>>> type(y1[0])
<class 'str'>
>>> type(y1[1])
<class 'int'>
>>> type(y1[2])
<class 'bool'>
>>>
>>> z={ 'x' : 10, 'y': 20}
>>> type(z)
<class 'dict'>
>>>
>>> z['x']
10
>>> z['y']
20
>>> z1= [ { 'x' : 20 }, { 'v1' : 40} ]
>>> type(z1)
<class 'list'>
>>>
>>>
>>> type(z1[0])
<class 'dict'>
>>>
>>>
>>> z1[0]['x']
20
>>> x=Tue
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Tue' is not defined. Did you mean: 'True'?
>>> x=True
>>>
>>>
>>> x
True
>>> type(x)
<class 'bool'>
>>> x='ram'
>>> x[0]
'r'
>>>
>>>
>>>
>>> x='10'
>>> type(x)
<class 'str'>
>>> x2=int(x)
>>> x2
10
>>> type(x2)
<class 'int'>
>>> y1=34.45
>>> type(y1)
<class 'float'>
>>> y2=int(y1)
>>> y2
34
>>> z1='ram'
>>> z2=int(z1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'ram'
>>> z2 = 'ram'
>>> z2
'ram'
>>>
>>>
>>> y3=10
>>> y4=float(y3)
>>> y4
10.0
>>>