Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.array([[1,2],[3,4],[5,6]])
>>> a
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> a[a>3]
array([4, 5, 6])
>>> a[a>1]
array([2, 3, 4, 5, 6])
>>> idx  = (a > 2)
>>> idx
array([[False, False],
       [ True,  True],
       [ True,  True]])
>>> 
