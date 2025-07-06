# Exercise 2.10 - Contextual Bandits

**Problem Statement**
Suppose you face a 2-armed bandit task whose true action values change randomly from time step to time step. Specifically, suppose that, for any time step, the true action values of actions 1 and 2 are respectively 0.1 and 0.2 with probability 0.5 (case A), and 0.9 and 0.8 with probability 0.5 (case B). If you are not able to tell which case you face at any step, what is the best expectation of success you can achieve and how should you behave to achieve it? Now suppose that on each step you are told whether you are facing case A or case B (although you still don't know the true action values). This is an associative search task. What is the best expectation of success you can achieve in this task, and how should you behave to achieve it?

# Solution

$q_*(1) = \begin{cases} 0.1, \text{with prob 0.5} \\ 0.9, \text{with prob 0.5} \end{cases}$

$q_*(2) = \begin{cases} 0.2, \text{with prob 0.5} \\ 0.8, \text{with prob 0.5} \end{cases}$

Note that each action has an average true value of 0.5. So in expectation, choosing either action at random will result in an average reward of 0.5. Therefore, if the bandit cannot tell which case it faces at any step, it should behave randomly or, equivalently, always take the same action since they have the same expected reward.

If the bandit knows which case it faces, then we want the bandit to try both actions in both cases A and B enough times to learn that action 1 is superior in case B and action 2 is superior in case A. This means the bandit must explore and so it should use $\epsilon$-greedy, UCB or equivalent with an associative component to maintain separate action-value estimates for each (case, action) tuple. Once sufficient exploration has been done, the bandit will know which action to take in each case. This means in case A it will receive 0.2 reward and in case B it will receive 0.9 reward. If we assume that these 2 cases occur with equal frequency, then the contextual bandit's best expected reward per step is $(0.9+0.2)/2 = 0.55$.