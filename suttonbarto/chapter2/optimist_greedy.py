import numpy as np

# --- parameters -----------------------------------------------------------
k, T, runs = 10, 10_000, 2_000
eps, alpha, sigma_rwlk = 0.0, 0.1, 0.01
# --------------------------------------------------------------------------

def optimistic_greedy(runs, k, T, eps, alpha, sigma, q0):
    q_true  = np.zeros((runs, k))
    q_hat   = np.full_like(q_true, q0)
    avg_r   = np.zeros(T)
    avg_opt = np.zeros(T)

    for t in range(T):
        greedy = q_hat.argmax(axis=1)
        explore = np.random.randint(0, k, runs)
        acts = np.where(np.random.rand(runs) < eps, explore, greedy)

        r = np.random.randn(runs) + q_true[np.arange(runs), acts]
        q_hat[np.arange(runs), acts] += alpha * (r - q_hat[np.arange(runs), acts])
        q_true += np.random.randn(runs, k) * sigma

        avg_r[t]   = r.mean()
        avg_opt[t] = (acts == q_true.argmax(axis=1)).mean()

    return avg_r, avg_opt
