import matplotlib.pyplot as plt
import numpy as np


def gradient_bandit(T: int, runs: int, k: int, alpha: float, sigma: float):
    q_true         = np.zeros((runs, k))
    H_t            = np.zeros((runs, k))
    avg_r          = np.zeros(T)
    avg_opt        = np.zeros(T)
    average_reward = np.zeros(runs)

    for t in range(1, T + 1):
        exp_H = np.exp(H_t)
        pi = exp_H / np.sum(exp_H, axis=1, keepdims=True)
        
        u = np.random.rand(runs, 1)          # one uniform(0,1) per bandit
        acts = (u < pi.cumsum(axis=1)).argmax(1)   # vectorised multinomial sample

        r = np.random.randn(runs) + q_true[np.arange(runs), acts]
        
        # Update action preferences (stochastic gradient ascent)
        H_t[np.arange(runs), acts] += alpha * (r - average_reward) * (1 - pi[np.arange(runs), acts])
        mask = np.ones_like(H_t, dtype=bool)
        mask[np.arange(runs), acts] = False
        update = alpha * (r - average_reward)[:, None] * pi[mask].reshape(runs, k - 1)
        H_t[mask] -= update.ravel()

        average_reward = (average_reward * t + r) / (t + 1)
        
        q_true += np.random.randn(runs, k) * sigma

        avg_r[t - 1]   = r.mean()
        avg_opt[t - 1] = (acts == q_true.argmax(axis=1)).mean()
    
    return avg_r, avg_opt


if __name__ == "__main__":
    avg_r, avg_opt = gradient_bandit(10000, 100, 10, 0.1, 0.1)
