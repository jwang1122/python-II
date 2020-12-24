# make a single prediction with the model
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_blobs
# create the inputs and outputs
X, y = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=2)
# define model
model = LogisticRegression(solver='lbfgs')
# fit model
model.fit(X, y)
# define input
new_input = [[2.12309797, -1.41131072]]
# get prediction for new input
new_output = model.predict(new_input)
# summarize input and output
print(new_input, new_output)

new_input = [[ -1.25884111,  -8.57055785]]
# get prediction for new input
new_output = model.predict(new_input)
# summarize input and output
print(new_input, new_output)