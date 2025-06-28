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

class NonstationaryBandit:
    def __init__(self, k=10, mu=0.0, sigma=1.0, walk_std=0.01):
        self.k = k
        self.q_true = np.ones(k) * mu
        self.sigma = sigma
        self.walk_std = walk_std

    def step(self):
        self.q_true += np.random.normal(0, self.walk_std, self.k)

    def reward(self, action):
        return np.random.normal(self.q_true[action], self.sigma)

def run_experiment(k=10, steps=10000, runs=2000, epsilon=0.1, alpha=0.1):
    avg_rewards_sample = np.zeros(steps)
    avg_rewards_const = np.zeros(steps)
    optimal_action_counts_sample = np.zeros(steps)
    optimal_action_counts_const = np.zeros(steps)

    for run in range(runs):
        bandit = NonstationaryBandit(k=k)
        Q_sample = np.zeros(k)
        Q_const = np.zeros(k)
        N = np.zeros(k)
        optimal_action = np.argmax(bandit.q_true)

        for t in range(steps):
            # Sample-average method
            if np.random.rand() < epsilon:
                action_sample = np.random.randint(k)
            else:
                action_sample = np.argmax(Q_sample)
            reward_sample = bandit.reward(action_sample)
            N[action_sample] += 1
            Q_sample[action_sample] += (reward_sample - Q_sample[action_sample]) / N[action_sample]

            # Constant step-size method
            if np.random.rand() < epsilon:
                action_const = np.random.randint(k)
            else:
                action_const = np.argmax(Q_const)
            reward_const = bandit.reward(action_const)
            Q_const[action_const] += alpha * (reward_const - Q_const[action_const])

            bandit.step()
            optimal_action = np.argmax(bandit.q_true)

            avg_rewards_sample[t] += reward_sample
            avg_rewards_const[t] += reward_const
            if action_sample == optimal_action:
                optimal_action_counts_sample[t] += 1
            if action_const == optimal_action:
                optimal_action_counts_const[t] += 1

    avg_rewards_sample /= runs
    avg_rewards_const /= runs
    optimal_action_counts_sample = 100 * optimal_action_counts_sample / runs
    optimal_action_counts_const = 100 * optimal_action_counts_const / runs

    return avg_rewards_sample, avg_rewards_const, optimal_action_counts_sample, optimal_action_counts_const

if __name__ == "__main__":
    steps = 10000
    avg_rewards_sample, avg_rewards_const, opt_sample, opt_const = run_experiment(steps=steps)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(avg_rewards_sample, label="Sample-average")
    plt.plot(avg_rewards_const, label="Constant step-size (α=0.1)")
    plt.xlabel("Steps")
    plt.ylabel("Average reward")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(opt_sample, label="Sample-average")
    plt.plot(opt_const, label="Constant step-size (α=0.1)")
    plt.xlabel("Steps")
    plt.ylabel("% Optimal action")
    plt.legend()

    plt.tight_layout()
    plt.show()