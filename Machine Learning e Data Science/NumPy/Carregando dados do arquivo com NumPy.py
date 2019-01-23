Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> val1, val2, val3 = np.loadtxt('dados.txt',skiprows=1, unpack=True)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    val1, val2, val3 = np.loadtxt('dados.txt',skiprows=1, unpack=True)
  File "/home/gledon/.local/lib/python3.5/site-packages/numpy/lib/npyio.py", line 926, in loadtxt
    fh = np.lib._datasource.open(fname, 'rt', encoding=encoding)
  File "/home/gledon/.local/lib/python3.5/site-packages/numpy/lib/_datasource.py", line 262, in open
    return ds.open(path, mode, encoding=encoding, newline=newline)
  File "/home/gledon/.local/lib/python3.5/site-packages/numpy/lib/_datasource.py", line 618, in open
    raise IOError("%s not found." % path)
OSError: dados.txt not found.
>>> 
