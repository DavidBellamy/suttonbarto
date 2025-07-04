"""
Exercise 2.5

Design and conduct an experiment to demonstrate the difficulties that
sample-average methods have for nonstationary problems. Use a modified
version of the 10-armed testbed in which all the q_*(a) start out equal
and then take independent random walks (say by adding a normally 
distributed increment with mean zero and standard deviation 0.01 to all 
the q_*(a) on each step). Prepare plots like Figure 2.2 for an action-
-value method using a constant step-size parameter, \alpha = 0.1. Use
\epsilon = 0.1 and longer runs, say of 10,000 steps.
"""

import matplotlib.pyplot as plt
import numpy as np

# --- parameters -----------------------------------------------------------
k, T, runs = 10, 10_000, 2_000
eps, alpha, sigma_rwlk = 0.1, 0.1, 0.01
# --------------------------------------------------------------------------

def bandit(runs, k, T, eps, alpha, sigma):
    q_true  = np.zeros((runs, k))
    q_hat   = np.zeros_like(q_true)
    avg_r   = np.zeros(T)
    avg_opt = np.zeros(T)

    for t in range(T):
        greedy = q_hat.argmax(1)
        explore = np.random.randint(0, k, runs)
        acts = np.where(np.random.rand(runs) < eps, explore, greedy)

        r = np.random.randn(runs) + q_true[np.arange(runs), acts]
        q_hat[np.arange(runs), acts] += alpha * (r - q_hat[np.arange(runs), acts])
        q_true += np.random.randn(runs, k) * sigma

        avg_r[t]   = r.mean()
        avg_opt[t] = (acts == q_true.argmax(1)).mean()

    return avg_r, avg_opt

avg_r, avg_opt = bandit(runs, k, T, eps, alpha, sigma_rwlk)

plt.plot(avg_r)
plt.xlabel("Steps")
plt.ylabel("Average reward")
plt.savefig("docs/ch02_ex02-05/avg_reward.png")
plt.clf()

plt.plot(avg_opt)
plt.xlabel("Steps")
plt.ylabel("% optimal")
plt.ylim(0, 1)
plt.savefig("docs/ch02_ex02-05/avg_optimal.png")
plt.clf()
