import numpy as np

# Activation Function
def sigmoid(w_sum):
    return 1/(1+np.exp(-w_sum))

# Get Model Output
def get_prediction(features, weights, bias):
    return sigmoid(np.dot(features, weights) + bias)

# Loss Function
def cross_entropy(target, pred):
    return -(target*np.log10(pred)+(1-target)*(np.log10(1-pred)))

# Update Weights
def gradient_descent(feature, weights, target, prediction, l_rate, bias):
    '''
    argument data types:
        feature, weights = list with 3 items
        target = integer (0 or 1)
        prediction, l_rate, bias = floating point numbers
    returns (tuple):
        new weights, new bias    
    '''
    new_weight = []
    bias += l_rate*(target-prediction)
    for x,w in zip(feature, weights):
        new_weight.append(w + l_rate*(target-prediction)*x)
    return new_weight, bias 
    
# Data
features = np.array(([0.1,0.5,0.2],
                     [0.2,0.3,0.1],
                     [0.7,0.4,0.2],
                     [0.1,0.4,0.3]))

targets = np.array([0,1,0,1])
weights = np.array([0.4, 0.2, 0.6])
bias = 0.5
l_rate = 0.1

# Gradient Descent Steps Over 10 Epochs
for epoch in range(10):
    for x, y in zip(features, targets):
        pred = get_prediction(x, weights, bias)
        error = cross_entropy(y, pred)
        weights, bias = gradient_descent(x, weights, y, pred, l_rate, bias)
        
    # Calculate and Print Average Loss
    predictions = get_prediction(features, weights, bias)
    average_loss = np.mean(cross_entropy(targets, predictions))
    print("*****************************")
    print("EPOCH", str(epoch))
    print("*****************************")
    print("Average Loss: ", average_loss)