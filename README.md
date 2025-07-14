# Setup

From the root of this repo, do:
```
python3.10 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
```

# Exercise Discussions

For discussions of specific exercises, see their respective folders:

| Chapter | Exercise | Topic | Notes |
|---------|----------|-------|-------|
| 2       | [2.5](./docs/ch02_ex02-05/README.md) | Non-stationary bandit | Random walk on values $\rarr$ noisier, slower convergence |
| 2       | [2.6](./docs/ch02_ex02-06/README.md) | Mysterious Spikes | &uarr; initial optimism $\implies$ &uarr; initial determinism in greedy policy |
|2 |[2.7](./docs/ch02_ex02-07/README.md) | Unbiased Constant-Step-Size Trick | Divide $\alpha$ by a function $f: \N \rarr [0, 1) $ which tends to 1 from below. Offsets bias of $Q_1$ by permitting larger-than-$\alpha$ updates at first, converging to $\alpha$-sized updates in the limit. |
|2|[2.8](./docs/ch02_ex02-08/README.md)|UCB Spikes| &uarr; exploration budget $\implies$ larger initial spike since bandit is 'forced off' the action with highest empirical mean |
|2|[2.9](./docs/ch02_ex02-09/README.md)|Gradient Bandits| 2-variable softmax $\equiv$ sigmoid/logistic function |
|2|[2.10](./docs/ch02_ex02-10/README.md)|Contextual bandits| With no context, acting randomly is best; with context, associating action-value estimates to states plus exploring  leads to higher average reward |
|2|[2.11](./docs/ch02_ex02-11/README.md) | Nonstationary bandit parameter study | $\epsilon$-greedy is best here vs. worst on stationary testbed; optimistic greedy is unimpacted by $Q_0$|
|3| [3.1](./docs/ch03_ex03-01/README.md) | Finite MDP Examples | MDPs are very general! |
|3|[3.2](./docs/ch03_ex03-02/README.md) | Limits of MDPs | Ill-defined reward signal; very noisy observations of underlying state; very sparse rewards; highly unstable dynamics
|3|[3.3](./docs/ch03_ex03-03/README.md) | Picking the agent-environment boundary | There is a Pareto front of controllability + complexity |
|3|[3.4](./docs/ch03_ex03-04/README.md) | Deriving one-step dynamics from state transition probabilities | The dynamics can be read off the state diagram | 
|3| [3.5](./docs/ch03_ex03-05/README.md) | Episodic Modification for the Transition Distribution | Dynamics function can't condition on terminal states else probabilities are undefined |
|3|[3.6](./docs/ch03_ex03-06/README.md) | Episodic vs. Continuing Returns of Pole-Balancing | Returns lie on a wider interval for continuing formulations than episodic |
|3|[3.7](./docs/ch03_ex03-07/README.md) | The issue with sparse rewards | Sparse rewards inhibit exploration; densifying the reward signal can help |
|3|[3.8](./docs/ch03_ex03-08/README.md) | Computing returns from rewards | Recurrence lets us compute earlier returns from later ones |