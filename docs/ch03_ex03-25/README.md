# Exercise 3.25 - Optimal state-value in terms of optimal action-value

**Problem Statement**
Give an equation for $v_*$ in terms of $q_*$.

# Solution
We know from this chapter that

$$v_*(s) = \max\limits_{a \in \mathcal{A}(s)} q_{\pi_*}(s, a) \quad \forall s \in \mathcal{S}$$

But $q_* \doteq q_{\pi_*}$ – this is just a difference in notation. Both refer to the optimal action-value function, that is, the expected return for taking action $a$ in state $s$ and thereafter following an optimal policy. 

$$\therefore \boxed{v_*(s) = \max\limits_{a \in \mathcal{A}(s)} q_*(s,a) \quad \forall s \in \mathcal{S}}$$