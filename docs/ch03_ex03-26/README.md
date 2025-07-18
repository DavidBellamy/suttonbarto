# Exercise 3.26 - Optimal action-value in terms of optimal state-value and dynamics

**Problem Statement**
Give an equation for $q_*$ in terms of $v_*$ and the four-argument $p$.

# Solution

The four-argument $p$ refers to the environment dynamics $p(s', r | s, a)$.

As shown in [Exercise 3.19](../ch03_ex03-19/README.md), the action-value can be expressed in terms of the state-value as follows

$$q_\pi(s, a) = \mathbb{E}[R_{t+1} + \gamma v_\pi(S_{t+1}) | S_t = s, A_t = a]$$

So under the optimal policy $\pi_*$ this relationship becomes

$$q_*(s, a) = \mathbb{E}[R_{t+1} + \gamma v_*(S_{t+1}) | S_t = s, A_t = a]$$

This expected value is taken with respect to the four-argument $p$ hence

$$\therefore \boxed{q_*(s,a) = \sum\limits_{s', r} p(s', r | s,a)[r + \gamma v_*(s')]}$$

The optimal action-value is the average of the immediate reward and the discounted optimal state-value over successor states.