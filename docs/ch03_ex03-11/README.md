# Exercise 3.11 - Expected Reward in terms of Policy

**Problem Statement**
If the current state is $S_t$, and actions are selected according to stochastic policy $\pi$, then what is the expectation of $R_{t+1}$ in terms of $\pi$ and the four-argument function $p$ below:

$$p(s',r|s,a) \doteq \Pr\{S_t=s', R_t=r|S_{t-1}=s, A_{t-1}=a\} \quad \forall s',s \in \mathcal{S}, a \in \mathcal{A}(s)$$

# Solution
We are given the current state and would like to know the expected reward the agent receives in the next step. This is the conditional expectation $\mathbb{E}[R_{t+1} | S_t = s]$.

The next reward depends on what action the agent takes, which is chosen by $\pi$ as well as the average reward the agent receives for the chosen action. Given a state $S_t=s$ and action $a$, the dynamics function can be used to compute the average reward:

$$\sum_{s' \in \mathcal{S}} \sum_{r \in \mathcal{R}} r \times p(s',r|s,a)$$

So the expected next reward will this average reward itself averaged over all possible actions the agent may take – weighted by the probability of the agent taking that action:

$\mathbb{E}[R_{t+1} | S_t = s] = \sum_{a \in \mathcal{A}(s)} \pi(a | s) \sum_{s' \in \mathcal{S}} \sum_{r \in \mathcal{R}} r \times p(s', r | s, a)$.