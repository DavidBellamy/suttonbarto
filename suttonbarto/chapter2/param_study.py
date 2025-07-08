"""
Exercise 2.11
"""

import matplotlib.pyplot as plt
import numpy as np

from suttonbarto.chapter2.epsilon_greedy  import epsilon_greedy
from suttonbarto.chapter2.ucb             import ucb
from suttonbarto.chapter2.gradient_bandit import gradient_bandit
from suttonbarto.chapter2.optimist_greedy import optimistic_greedy


# ------------------------------------------------------------------
# shared bandit settings
k, T, runs        = 10, 200_000, 2000
alpha, sigma_rwlk = 0.1, 0.01                     # step-size & random-walk σ
# ------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 4))

# ——————————————————— ε-greedy ————————————————————
epsilons     = [1/512, 1/256, 1/128, 1/64, 1/32, 1/16, 1/8]
avg_rewards  = []
for eps in epsilons:
    print('next')
    avg_r, _ = epsilon_greedy(runs, k, T, eps, alpha, sigma_rwlk)
    avg_rewards.append(avg_r[-100_000:].mean())
ax.plot(epsilons, avg_rewards, color='tab:red', label=r'$\varepsilon$-greedy', marker='o')
print('done')
# ——————————————————— gradient bandit ————————————————
alphas       = [2**(-16), 2**(-15), 2**(-14), 2**(-13), 2**(-12), 2**(-11)]
avg_rewards  = []
for a in alphas:
    print('next')
    avg_r, _ = gradient_bandit(T, runs, k, a, sigma_rwlk)
    avg_rewards.append(avg_r[-100_000:].mean())
ax.plot(alphas, avg_rewards, color='tab:green', label='gradient bandit', marker='o')
print('done')
# ——————————————————— UCB ————————————————————————
cs           = [8, 16, 32, 64, 128, 256]
avg_rewards  = []
for c in cs:
    print('next')
    avg_r, _ = ucb(runs, k, T, c, alpha, sigma_rwlk)
    avg_rewards.append(avg_r[-100_000:].mean())
ax.plot(cs, avg_rewards, color='tab:blue', label='UCB', marker='o')
print('done')
# ——————————————————— optimistic greedy ——————————————
q0s          = [1/512, 1/128, 1/32, 1/8, 1/2, 2, 8]
avg_rewards  = []
for q in q0s:
    print('next')
    avg_r, _ = optimistic_greedy(runs, k, T, 0.0, alpha, sigma_rwlk, q)
    avg_rewards.append(avg_r[-100_000:].mean())
ax.plot(q0s, avg_rewards, color='k', label='greedy (optimistic $Q_0$)', marker='o')
print('done')
# ——————————————————— decorations ———————————————————
ax.set_xscale('log', base=2)
ax.set_ylabel('Average reward (last 100 k steps)')
ax.grid(True, which='both', ls='--', lw=0.4, alpha=0.7)
ax.legend(frameon=False, fontsize='small')

# geometric midpoint in log space
geo_mid = lambda seq: 2**((np.log2(seq[0]) + np.log2(seq[-1])) / 2)

# collect (midpoint, symbol, colour) tuples and sort by midpoint
families = sorted([
    (geo_mid(epsilons), r'$\varepsilon$', 'tab:red'),
    (geo_mid(alphas),   r'$\alpha$',      'tab:green'),
    (geo_mid(cs),       r'$c$',           'tab:blue'),
    (geo_mid(q0s),      r'$Q_0$',         'k')
], key=lambda t: t[0])

# equally-spaced x positions (very close together, ~0.03 apart)
gap   = 0.03                     # ≈ one-tenth of the old 0.25 spacing
start = 0.5 - 1.5*gap            # centre block of 4 symbols around 0.5
x_pos = start + np.arange(4)*gap # [0.455, 0.485, 0.515, 0.545]

for (mid, txt, col), x in zip(families, x_pos):
    ax.text(x, -0.12, txt, color=col,
            transform=ax.transAxes, ha='center', va='top',
            fontsize='large', clip_on=False)

fig.tight_layout()
plt.savefig("docs/ch02_ex02-11/param_study.png")
plt.clf()
