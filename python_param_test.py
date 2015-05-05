Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
def storyy(**kwds):
	return 'Once upon a time ,there war a '\
	       '%(job)s called %(name)s.
SyntaxError: EOL while scanning string literal
>>> def storyy(**kwds):
	return 'Once upon a time ,there war a '\
	       '%(job)s called %(name)s.'%kwds
def power(x,y,*others):
	
SyntaxError: invalid syntax
>>> def story(**kwds):
	return 'Once upon a time ,there war a '\
	       '%(job)s called %(name)s.'%kwds

>>> def power(x,y,*other):
	if others:
		print'Received redundant parameters:'. others
		
SyntaxError: invalid syntax
>>> def power(x,y,*other):
	if others:
		print('Received redundant parameters:'. others)

		
>>> def interval(start,stop=None,step=1):
	'Imitates range() for step>0'
	if stop is None:
		start,stop=0,start
	result = []
	i = start
	while i<stop:
		result.append(i)
		i += step
	return result

>>> def power(x,y,*other):
	if others:
		print('Received redundant parameters:', others)

		
>>> print story(job='king',name='gumby')
SyntaxError: invalid syntax
>>>  def story(**kwds):
	return 'Once upon a time ,there war a '\
	       '%(job)s called %(name)s.'%kwds
SyntaxError: unexpected indent
>>> 
>>> def story(**kwds):
	return 'Once upon a time ,there war a '\
	       '%(job)s called %(name)s.'%kwds

>>> print(story(job='1',name='2'))
Once upon a time ,there war a 1 called 2.
>>> params={'job':'language','name':'python'}
>>> print story(**params)
SyntaxError: invalid syntax
>>> def story(**kwds):
	return 'Once upon a time ,there war a '\
	       '%(job)s called %(name)s.'%kwds

>>> print(story(**params))
Once upon a time ,there war a language called python.
>>> power(2,3)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    power(2,3)
  File "<pyshell#24>", line 2, in power
    if others:
NameError: name 'others' is not defined
>>> def power(x,y,*other):
	if others:
		print('Received redundant parameters:'. others)
	return pow(x,y)

>>> power(2,3)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    power(2,3)
  File "<pyshell#39>", line 2, in power
    if others:
NameError: name 'others' is not defined
>>> def power(x,y,*others):
	if others:
		print('Received redundant parameters:'. others)
	return pow(x,y)

>>> power(2,3)
8
>>> params=(5,)*2
>>> power(*params)
3125
>>> params
(5, 5)
>>> pow(5,5)
3125
>>> power(5,5 params)
SyntaxError: invalid syntax
>>> params=(5,)*2
>>> power(5,5,params)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    power(5,5,params)
  File "<pyshell#42>", line 3, in power
    print('Received redundant parameters:'. others)
AttributeError: 'str' object has no attribute 'others'
>>> print(params)
(5, 5)
>>> 
>>> def power(x,y,*others):
	if others:
		print('Received redundant parameters:',others)
	return pow(x,y)
SyntaxError: invalid syntax
>>> 
>>> 
>>> def power(x,y,*others):
	if others:
		print('Received redundant parameters:',others)
	return pow(x,y)

>>> power(5,5,params)
Received redundant parameters: ((5, 5),)
3125
>>> print(paramse)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(paramse)
NameError: name 'paramse' is not defined
>>> print(paramse)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(paramse)
NameError: name 'paramse' is not defined
>>> print(params)
(5, 5)
>>> print('123',params)
123 (5, 5)
>>> 
