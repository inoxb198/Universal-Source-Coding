import numpy as np

def loss_function(X, y, w, lambda1, lambda2):
    # Compute the predictions
    y_pred = X @ w
    
    # Compute the mean squared error
    mse = 0.5 * np.mean((y_pred - y)**2)
    
    # Compute L1 norm of the weights
    l1_norm = np.sum(np.abs(w))
    
    # Compute L2 norm of the weights
    l2_norm = np.sqrt(np.sum(w**2))
    
    # Total loss
    total_loss = mse + lambda1 * l1_norm + lambda2 * l2_norm
    
    return total_loss

def gradient(X, y, w, lambda1, lambda2):
    # Compute the predictions
    y_pred = X @ w
    
    # Compute the gradient of the mean squared error
    mse_gradient = X.T @ (y_pred - y) / len(y)
    
    # Compute the gradient of L1 norm
    l1_gradient = lambda1 * np.sign(w)
    
    # Compute the gradient of L2 norm
    l2_gradient = lambda2 * w / np.sqrt(np.sum(w**2))
    
    # Total gradient
    total_gradient = mse_gradient + l1_gradient + l2_gradient
    
    return total_gradient

def exponential_gradient_descent(X, y, lambda1, lambda2, learning_rate=0.1, max_iter=1000, tol=1e-6):
    # Initialize weights
    w = np.ones(X.shape[1]) / X.shape[1]
    
    # Initialize learning rate
    eta = learning_rate
    
    # Initialize previous loss
    prev_loss = np.inf
    
    # Perform gradient descent
    for i in range(max_iter):
        # Compute gradient
        grad = gradient(X, y, w, lambda1, lambda2)
        
        # Update weights using exponential learning rate
        w -= eta * grad
        
        # Apply constraint: sum of elements of w is 1
        w /= np.sum(w)
        
        # Ensure non-negativity of weights
        w = np.maximum(w, 0)
        
        # Compute current loss
        current_loss = loss_function(X, y, w, lambda1, lambda2)
        
        # Check convergence
        if abs(prev_loss - current_loss) < tol:
            break
        
        # Update previous loss
        prev_loss = current_loss
        
        # Update learning rate exponentially
        eta *= 0.99  # Adjust the decay rate as needed
        
    return w

# Example usage
# Generate random data
np.random.seed(0)
X = np.random.randint(1, 100,size=(100,26))
y = np.sum(X,axis=1)
z = np.sum(X,axis=0)
u = np.sum(y)
# Hyperparameters
lambda1 = 0.1
lambda2 = 0.1
learning_rate = 0.1
max_iter = 1000
tol = 1e-6

# Perform exponential gradient descent
w_optimal = exponential_gradient_descent(X, y, lambda1, lambda2, learning_rate, max_iter, tol)

print("Optimal Weights:")
print(w_optimal)
print(z)
print(u)