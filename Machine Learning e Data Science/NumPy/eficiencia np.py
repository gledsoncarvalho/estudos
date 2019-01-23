Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> soma = 0
>>> for i in range(1, 100000001):
	soma += i

	
>>> import numpy as np
>>> np.arrange(1, 100000001).sum()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    np.arrange(1, 100000001).sum()
AttributeError: module 'numpy' has no attribute 'arrange'
>>> np.arange(1, 100000001).sum()
5000000050000000
>>> print(soma)
5000000050000000
>>> # criando arranjo com numpy
>>> 
