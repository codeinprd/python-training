Python 3.10.11 (v3.10.11:7d4cc5aa85, Apr  4 2023, 19:05:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> name = "Aviral"
>>> type(name)
<class 'str'>
>>> name = "aviral"
>>> name.title()
'Aviral'
>>> name.upper()
'AVIRAL'
>>> name.lower()
'aviral'
>>> "AVIRAL".lower()
'aviral'
>>> 
>>> len(name)
6
>>> name[0]
'a'
>>> name[1]
'v'
>>> name[2]
'i'
>>> name[3]
'r'
>>> name[4]
'a'
>>> name[5]
'l'
>>> for letter in name:
...     print(letter)
... 
a
v
i
r
a
l
>>> name[:2]
'av'
>>> name[:3]
'avi'
>>> name[:-3]
'avi'
>>> name[-3:]
'ral'
>>> email = "aviral.vishnoi@gmail.com"
>>> email.split("@")
['aviral.vishnoi', 'gmail.com']
>>> fullname = email.split("@")
>>> fullname[0].split(".")
['aviral', 'vishnoi']
>>> name = fullname[0].split(".")
>>> name
['aviral', 'vishnoi']
>>> first_name = name[0].title()
>>> last_name = name[1].title()
>>> first_name
'Aviral'
>>> last_name
'Vishnoi'
>>> final_name = f"{first_name} {last_name}"
>>> final_name
'Aviral Vishnoi'
>>> email.splt("@")[0].split(".")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'splt'. Did you mean: 'split'?
>>> email.split("@")[0].split(".")
['aviral', 'vishnoi']