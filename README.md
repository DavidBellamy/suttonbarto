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
|3|[3.9](./docs/ch03_ex03-09/README.md) | Early Returns with Infinite Horizons | Infinite-horizon returns are easily computable when rewards are constant |
|3|[3.10](./docs/ch03_ex03-10/README.md) | Proof of the infinite geometric series identity | Telescoping-sum method works here |
|3|[3.11](./docs/ch02_ex03-11/README.md) | Expected Reward in terms of Policy | The product of policy and marginalized dynamics function yields the agent's expected rewards |
|3|[3.12](./docs/ch03_ex03-12/README.md) | State-value function in terms of action-value function | State-value is the expectation of action-value under the policy's action probabilities in that state |
|3|[3.13](./docs/ch03_ex03-13/README.md) | Action-value function in terms of state-value function | Action-value is the expected immediate reward plus the discounted expected next-state value |
|3|[3.14](./docs/ch03_ex03-14/README.md) | Center state-value in Gridworld | When state-values of successor states are known it is easy to derive the state-value of a predecessor state from them |
|3|[3.15](./docs/ch03_ex03-15/README.md) | Adding a constant to all rewards in a continuing task | This adds a constant to all state-values, leaving their relative values unchanged |
|3|[3.16](./docs/ch03_ex03-16/README.md) | Adding a constant to all rewards in an episodic task | This shifts state-values randomly depending on episode length. Positive constants incentivize longer episodes. Negative constants incentivize shorter ones. |
|3|[3.17](./docs/ch03_ex03-17/README.md) | Bellman equation for action-values | Action-values are the expected {immediate reward plus discounted action-value of successor state/actions} | 
|3|[3.18](./docs/ch03_ex03-18/README.md) | State-value in terms of action-value | State-value is the expected action-value |