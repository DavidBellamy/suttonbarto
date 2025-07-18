# Exercise 3.28 - Optimal policy in terms of optimal state-values and dynamics

**Problem Statement**
Give an equation for $\pi_*$ in terms of $v_*$ and the four-argument $p$.

# Solution
As in [Exercise 3.27](../ch03_ex03-27/README.md), the optimal policy will be greedy with respect to the optimal state-value function as well. However, it will need to use the environment dynamics to do a one-step look-ahead search over state transitions. Intuitively, the optimal policy selects the actions that maximize the expected immediate reward plus the discounted optimal state-value of the next states where the expectation is taken over all possible successor states. 

$\pi_*(a | s) = \begin{cases} 1 \quad \text{if } a \in \argmax\limits_{a \in \mathcal{A}(s)} \mathbb{E}[R_{t+1} + \gamma v_*(S_{t+1}) | S_t = s, A_t=a] \\
0 \quad \text{otherwise} \end{cases}$

By the definition of this expectation

$$\pi_*(a|s) = \begin{cases} 1 \quad \text{if } a \in \argmax\limits_{a \in \mathcal{A}(s)} \sum\limits_{s', r} p(s', r| s, a)[r + \gamma v_*(s')] \\
0 \quad \text{otherwise} \end{cases}$$

Another way to see this is the fact that 

$$q_*(s,a) = \sum\limits_{s', r} p(s', r | s,a)[r + \gamma v_*(s')]$$

As shown in [Exercise 3.26](../ch03_ex03-26/README.md). And by [Exercise 3.27](../ch03_ex03-27/), the optimal policy places probability 1 on the action(s) that maximize $q_*(s, a)$. 