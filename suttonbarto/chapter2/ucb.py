import numpy as np


def ucb(runs, k, T, c, alpha, sigma):
    q_true  = np.zeros((runs, k))
    q_hat   = np.zeros_like(q_true)
    N_t_a   = np.zeros_like(q_true, dtype=int)
    avg_r   = np.zeros(T)
    avg_opt = np.zeros(T)

    for t in range(1, T + 1):
        bonus = np.where(N_t_a == 0, np.inf, c * np.sqrt(np.log(t) / N_t_a))
        ucbs = q_hat + bonus
        acts = ucbs.argmax(axis=1)

        r = np.random.randn(runs) + q_true[np.arange(runs), acts]
        N_t_a[np.arange(runs), acts] += 1
        q_hat[np.arange(runs), acts] += alpha * (r - q_hat[np.arange(runs), acts])
        q_true += np.random.randn(runs, k) * sigma

        avg_r[t - 1]   = r.mean()
        avg_opt[t - 1] = (acts == q_true.argmax(axis=1)).mean()

    return avg_r, avg_opt
