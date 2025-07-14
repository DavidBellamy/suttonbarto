# Exercise 3.6 - Episodic vs. Continuing Returns of Pole-Balancing

**Problem Statement**
Suppose you treated pole-balancing as an episodic task but also used discounting, with all rewards zero except for -1 upon failure. What then would the return be at each time? How does this return differ from that in the discounted, continuing formulation of this task?

# Solution
The discounted return for an episodic task is

$$G_t \doteq R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ... \gamma^{T-1 - t} R_T = \sum\limits_{k=0}^{T-1-t} \gamma^k R_{t+k+1} \quad \text{for } t < T$$

Let's define $G_T = 0$ since no reward can be obtained once a terminal state has been reached in an episode.

The problem states that $R_k = 0$ for $0 \le k \le {T-1}$. Hence regardless of the value of the discount factor $\gamma$, $G_t = \gamma^{T-1-t} R_T$. However, since an episode only ends if the agent fails this means that $R_T = -1$. Therefore, $\boxed{G_t = -\gamma^{T-1 - t}}$. Note that when $t=T-1$, $G_{T-1} = -\gamma^0 = -1$. 



$G_t$ is an increasing function in $T$ and for $0 \le \gamma \le 1$ it has a minimum value of -1 and a maximum value of 0. So this would indeed incentivize the agent to balance the pole for as long as possible. 

$\therefore$ The returns are $\{-1, -\gamma, -\gamma^2, -\gamma^3, ..., 0\} \in [-1, 0]$. Only the single failure at time $T$ contributes, discounted by how many steps in the future it is.

In the discounted, continuing formulation of the task, the return is 
$G_t \doteq \sum\limits_{k=0}^\infty \gamma^k R_{t + k+1}$ and $R_k = 0$ for all $R_k$ except the failures, which have a reward of -1. This causes all but those failure terms in the sum to vanish. In the continuing formulation, the agent makes infinitely many attempts at balancing the pole, hence it also encounters infinite failures. Therefore, the reward sequence looks like
$$0,0,0,...,0,-1,0,0,0,...$$

Where the gaps between -1s vary. Let $K_1, K_2, K_3, ...$ be the random numbers of steps between successive failures and define the partial sums $S_n = K_1 + K_2 + ... + K_n$ (with $S_0 = 0$). Then from any time-step $t$ the return is:

$$G_t = - \sum\limits_{n=1}^\infty \gamma^{S_n-t} 1\{S_n > t\}$$

This return quantifies how often failures happen *forever*. Under a fixed policy, $\mathbb{E}[G_t]$ is stationary – the distribution of time until the next failure is the same independent of $t$.

If no failures ever occur, then every future reward is 0 so the upper bound on the return is 0. The lower bound is if failure occurs every step. Then the return becomes $-\sum\limits_{k=0}^\infty \gamma^k = -\frac{1}{1-\gamma} \in [-\infty, -1] \quad \text{for } 0 \lt \gamma \lt 1$.

$\therefore$ So the returns in the continuing case lie in $[-\frac{1}{1-\gamma}, 0]$, which can reach $[-\infty, 0]$ as $\gamma \rarr 1$. These returns lie on a wider interval than those from the episodic formulation.