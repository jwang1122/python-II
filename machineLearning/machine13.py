import random
from numpy import *
from sklearn.linear_model import LogisticRegression

y = []
x = arange(0,10,0.1)
z = []
for i in x:
    y.append([i,i*i +random.random()])
    z.append(i*i)

model = LogisticRegression(solver='lbfgs')
model.fit(y, z)
output = model.predict([5.5])

print(output)