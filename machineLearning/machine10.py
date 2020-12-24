# example of creating a test dataset
from sklearn.datasets import make_blobs
from matplotlib import pyplot

# create the inputs and outputs
X, y = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=2)
# summarize the shape of the arrays
print(X.shape, y.shape)

pyplot.boxplot(y)
pyplot.title('Algorithm Comparison')
pyplot.show()

x1 = list(map(lambda z: z[0], X))
x2 = list(map(lambda z: z[1], X))
pyplot.scatter(x1, y, label="x[0]")
# pyplot.scatter(x2, y, label="x[1]")
pyplot.legend(loc=2)
pyplot.show()
