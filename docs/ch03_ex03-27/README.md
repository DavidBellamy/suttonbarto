# Exercise 3.27 - Optimal policy in terms of optimal action-values

**Problem Statement**
Give an equation for $\pi_*$ in terms of $q_*$. 

# Solution
By definition, the action that has maximal optimal action-value is the one that will produce the greatest return. Hence the optimal policy is simply the one that is greedy (over actions) with respect to the optimal action-value function. This policy selects the action that yields the greatest returns in every state. Specifically,

$$\pi_*(a | s) = \begin{cases}1 \quad \text{if } a \in \argmax\limits_{a' \in \mathcal{A}(s)} q_*(s, a') \\ 0 \quad \text{otherwise} \end{cases}$$

If there are multiple actions that maximize the action-value function, then they are all equally optimal by definition and so ties can be broken arbitrarily. 