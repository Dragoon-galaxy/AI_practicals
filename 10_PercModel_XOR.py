import numpy as np


class NeuralNetwork:
    def __init__(self):
        # Initialize weights and biases for the hidden layer and output layer
        self.input_size = 2
        self.hidden_size = 2
        self.output_size = 1
        self.learning_rate = 0.1

        self.w1 = np.random.randn(self.input_size, self.hidden_size)
        self.b1 = np.zeros((1, self.hidden_size))
        self.w2 = np.random.randn(self.hidden_size, self.output_size)
        self.b2 = np.zeros((1, self.output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, X):
        # Compute the output for the hidden layer
        self.z1 = np.dot(X, self.w1) + self.b1
        self.a1 = self.sigmoid(self.z1)

        # Compute the output for the output layer
        self.z2 = np.dot(self.a1, self.w2) + self.b2
        self.a2 = self.sigmoid(self.z2)

        return self.a2

    def backward(self, X, y, output):
        # Compute the loss
        loss = y - output

        # Compute the gradient for the output layer
        delta2 = loss * self.sigmoid_derivative(output)

        # Compute the loss for the hidden layer
        loss_hidden = delta2.dot(self.w2.T)

        # Compute the gradient for the hidden layer
        delta1 = loss_hidden * self.sigmoid_derivative(self.a1)

        # Update weights and biases
        self.w2 += self.a1.T.dot(delta2) * self.learning_rate
        self.b2 += np.sum(delta2, axis=0, keepdims=True) * self.learning_rate
        self.w1 += X.T.dot(delta1) * self.learning_rate
        self.b1 += np.sum(delta1, axis=0, keepdims=True) * self.learning_rate

    def train(self, X, y, epochs):
        for _ in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)


# Example usage:
if __name__ == '__main__':
    # Define the training data and labels (for XOR gate)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Create a neural network
    model = NeuralNetwork()

    # Train the network
    model.train(X, y, epochs=10000)

    # Test the trained network
    predictions = model.forward(X)
    print("Predictions for test data (XOR GATE):")
    for i in range(len(predictions)):
        print(f"Inputs: {X[i]}, Prediction: {predictions[i]}")
