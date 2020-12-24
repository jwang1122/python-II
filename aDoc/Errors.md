# Python Errors

## Machine Learning
```
Python: 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)]
scipy: 1.5.4
numpy: 1.19.3
matplotlib: 3.3.0
pandas: 1.1.5
sklearn: 0.24.0
```
* Check the versions of libraries

```py
# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))
```

* Runtime Error
```
RuntimeError: The current Numpy installation ('c:\\Users\\12818\\workspace\\python-I\\env\\lib\\site-packages\\numpy\\__init__.py') fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information: https://tinyurl.com/y3dm3h86
```
* Caused: 
Failed Version | Success Version |
|--- |--- |
matplotlib-3.3.3 | matplotlib-3.3.0
numpy-1.19.4     | numpy-1.19.3

* Solution
```
pip install numpy==1.19.3
pip install matplotlib==3.3.0

```
