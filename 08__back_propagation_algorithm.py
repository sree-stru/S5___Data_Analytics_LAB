import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(output):
    return output * (1 - output)

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

np.random.seed(42)

input_neurons = 2
hidden_neurons = 2
output_neurons = 1

W1 = np.random.uniform(low=-1, high=1, size=(input_neurons, hidden_neurons))
b1 = np.random.uniform(low=-1, high=1, size=(1, hidden_neurons))

W2 = np.random.uniform(low=-1, high=1, size=(hidden_neurons, output_neurons))
b2 = np.random.uniform(low=-1, high=1, size=(1, output_neurons))

eta = 0.5

epochs = 10000

for epoch in range(epochs):
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    final_output = sigmoid(final_input)

    error = y - final_output

    d_output = error * sigmoid_derivative(final_output)

    error_hidden = np.dot(d_output, W2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    W2 += np.dot(hidden_output.T, d_output) * eta
    b2 += np.sum(d_output, axis=0, keepdims=True) * eta

    W1 += np.dot(X.T, d_hidden) * eta
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * eta

print("\n--- Final Predictions after Training ---")
print(np.round(final_output, 3))
