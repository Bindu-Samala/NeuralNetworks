import numpy as np

class ART1:
    def __init__(self, num_clusters, vigilance):
        self.num_clusters = num_clusters  # Number of clusters
        self.vigilance = vigilance  # Vigilance parameter
        self.weights = None  # Weight matrix

    def fit(self, X):
        num_features = X.shape[1]
        self.weights = np.random.rand(self.num_clusters, num_features)  # Initialize weight matrix
        while True:
            for x in X:
                while True:
                    y = self.predict(x)
                    if y is not None:
                        # Update weight matrix
                        self.weights[y, :] = np.maximum(self.weights[y, :], x)
                        if np.all(self.weights[y, :] == x):
                            break
                    else:
                        # Create a new cluster
                        if self.num_clusters <= X.shape[0]:
                            return
                        self.num_clusters -= 1
                        self.weights[self.num_clusters-1, :] = x
            if self.num_clusters == X.shape[0]:
                break

    def predict(self, x):
        for i in range(self.num_clusters):
            if np.sum(np.minimum(self.weights[i, :], x)) / np.sum(np.maximum(self.weights[i, :], x)) >= self.vigilance:
                return i
        return None

# Create an instance of ART1 with 3 clusters and vigilance of 0.6
art1 = ART1(num_clusters=3, vigilance=0.6)

# Generate some random input data
X = np.random.rand(10, 5)

# Train the ART1 model on the input data
art1.fit(X)

# Predict the cluster for a new input
x = np.random.rand(5)
y = art1.predict(x)
print(f"Input {x} belongs to cluster {y}")
