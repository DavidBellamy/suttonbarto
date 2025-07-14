# Exercise 3.12 - State-value function in terms of action-value function

**Problem Statement**
Give an equation for $v_\pi$ in terms of $q_\pi$ and $\pi$. Where

$v_\pi(s) \doteq \mathbb{E}_\pi[G_t | S_t = s]$ and $q_\pi(s,a) \doteq \mathbb{E}_\pi[G_t | S_t=s, A_t=a]$.

# Solution
$q_\pi$ is the expected future return given a particular (state, action) pair under policy $\pi$. $v_\pi$ is the expected future return given a particular state under policy $\pi$ and averages over all possible actions the agent may choose from in state $S_t = s$. So if we average the action-value function across all possible actions $A_t$, weighing each term by the probability that action is chosen $\pi(a | s)$ then we obtain $v_\pi$. 

$\therefore v_\pi(s) = \sum\limits_{a \in \mathcal{A}(s)} q_\pi(s, a) \pi(a | s)$