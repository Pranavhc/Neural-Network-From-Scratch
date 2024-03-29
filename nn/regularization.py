import numpy as np

class Regularization():
    def __init__(self, norm: str, lambda_: float ):
        if norm not in ["L1", "L2"]: raise ValueError("Invalid norm!")
        
        self.lambda_ = lambda_
        self.norm = norm

    def L1(self, weights: np.ndarray) -> np.ndarray:
        return self.lambda_ * np.sign(weights)
    
    def L2(self, weights: np.ndarray) -> np.ndarray:
        return 2 * self.lambda_ * weights

    def __call__(self, weights: np.ndarray) -> np.ndarray:
        if self.norm == "L1":
            return self.L1(weights)
        return self.L2(weights)

# Regularization norms -
# L1 = lamda * sum(|W|)
# L2 = lambda * Sum(W^2)

# Derivative w.r.t W -
# L1 = lambda * sign(W)
# L2 = 2 * lambda * W