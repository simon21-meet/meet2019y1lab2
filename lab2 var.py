Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
a-5
Traceback (most recent call last):
  File "<pyshell#0>", line 2, in <module>
    a-5
NameError: name 'a' is not defined
>>> a=10
>>> a=5
>>> b=10
>>> a=b
>>> b=a
>>> a
10
>>> b
10
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> b
10
>>> a=5
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
5
>>> four='4'
>>> print(four*3)
444
>>> five=4
>>> print(five*3)
12
>>> 
>>> my_name='student'
>>> print("hi", + my_name)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print("hi", + my_name)
TypeError: bad operand type for unary +: 'str'
>>> print("HI",+my_name)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print("HI",+my_name)
TypeError: bad operand type for unary +: 'str'
>>> print("hi"+my_student)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print("hi"+my_student)
NameError: name 'my_student' is not defined
>>> print("hi"+my_name)
histudent
>>> my_age+15
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    my_age+15
NameError: name 'my_age' is not defined
>>> my_age=15
>>> print("I am"+my_age+'years old')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print("I am"+my_age+'years old')
TypeError: must be str, not int
>>> my_age="15"
>>> print("I am" + my_age + 'years old')
I am15years old
>>> score=4
>>> count='5'
>>> total=score*count
>>> print(total)
5555
>>> score=4
>>> count='5'
>>> total=score * count
>>> 
>>> print(toal)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(toal)
NameError: name 'toal' is not defined
>>> print(total)
5555
>>> 
