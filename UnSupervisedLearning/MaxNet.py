import numpy as np
class Maxnet:
    def __init__(self, num_neurons, learning_rate):
        self.num_nuerons = num_neurons
        self.learning_rate =  learning_rate
        self.weights = np.random.rand(num_neurons, num_neurons)

    def train(self, data, num_epochs):
        for epoch in range(num_epochs):
            for i in range(len(data)):
                x = data[i]
                y = np.dot(self.weights, x)
                y[y<0] = 0
                y_max = np.max(y)
                delta = self.learning_rate*(y-y_max)
                self.weights+=np.outer(delta, x)
    def predict(self, data):
        y = np.dot(self.weights, data)
        y[y<0]=0
        return y

data = np.array([[0,1,1],[1,0,1],[1,1,0]])
maxnet = Maxnet(num_neurons=3, learning_rate=0.1)
maxnet.train(data, num_epochs=100)
print(maxnet.predict(np.array([0,0,1])))
















