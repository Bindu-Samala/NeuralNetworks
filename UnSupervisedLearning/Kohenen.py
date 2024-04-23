import numpy as np
import matplotlib.pyplot as plt

class KohonenSOM:
    def __init__(self, input_shape, map_shape, num_epochs, learning_rate):
        self.input_shape = input_shape
        self.map_shape = map_shape
        self.num_epochs = num_epochs
        self.learning_rate = learning_rate
        self.weights = np.random.rand(*map_shape, *input_shape)

    def train(self, data):
        for epoch in range(self.num_epochs):
            for x in data:
                winner = np.unravel_index(np.argmin(np.linalg.norm(x - self.weights, axis=-1)), self.map_shape)
                for i, j in np.ndindex(self.map_shape):
                    dist = np.linalg.norm(np.array([i, j]) - np.array(winner))
                    if dist <= self.learning_rate:
                        self.weights[i, j] += (x - self.weights[i, j]) * dist / self.learning_rate

    def predict(self, data):
        predictions = np.zeros((len(data), *self.map_shape))
        for i, x in enumerate(data):
            predictions[i] = np.exp(-np.linalg.norm(x - self.weights, axis=-1))
        return predictions

# example usage
data = np.random.rand(100, 2)
kohonen = KohonenSOM(input_shape=(2,), map_shape=(10, 10), num_epochs=100, learning_rate=0.5)
kohonen.train(data)
predictions = kohonen.predict(data)
plt.imshow(predictions.mean(axis=0), cmap='gray')
plt.show()
