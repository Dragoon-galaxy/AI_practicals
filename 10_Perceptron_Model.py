import numpy as np


class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(input_size)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, inputs):
        # Compute the weighted sum
        summation = np.dot(inputs, self.weights)
        # Apply the step function as the activation
        return 1 if summation >= 2 else 0  # Adjusted threshold for AND gate

    def train(self, training_data, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                # Update the weights using the perceptron learning rule
                self.weights += self.learning_rate * (label - prediction) * inputs


# Example usage:
if __name__ == '__main__':
    # Define the training data and labels (for AND gate)
    training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels = np.array([0, 0, 0, 1])

    # Create a Perceptron with 2 input features
    perceptron = Perceptron(input_size=2)

    # Train the Perceptron
    perceptron.train(training_data, labels)

    # Test the trained Perceptron
    test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    predictions = [perceptron.predict(inputs) for inputs in test_data]

    print("Predictions for test data ( AND GATE ):")
    for inputs, prediction in zip(test_data, predictions):
        print(f"Inputs: {inputs}, Prediction: {prediction}")
