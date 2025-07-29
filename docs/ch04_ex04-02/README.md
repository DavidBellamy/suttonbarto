# Exercise 4.2 - Changing one transition in the dynamics

**Problem Statement**
In Example 4.1 (see [Exercise 4.1](../ch04_ex04-01/README.md)), suppose a new state 15 is added to the gridworld just below state 13, and its actions, left, up, right, and down, take the agent to states 12, 13, 14, and 15, respectively. Assume that the transitions *from* the original states are unchanged. What, then, is $v_\pi(15)$ for the equiprobable random policy? Now suppose the dynamics of state 13 are also changed, such that action down from state 13 takes the agent to the new state 15. What is $v_\pi(15)$ for the equiprobable random policy in this case?

# Solution
Recall the state-value Bellman equation

$$v_\pi(s) =
\sum\limits_a \pi(a|s) \sum\limits_{s', r} p(s', r|s,a)[r + \gamma v_\pi(s')] \quad \forall s \in \mathcal{S}$$

We know that $\pi(a|s) = 0.25$ for all $a$. We also know that $p(s',r|s,a) = 1$ for all legal state transitions and 0 otherwise. And we know that $r=-1$ for all legal state transitions. Also, $\gamma=1$ because this is an undiscounted task. Therefore, the double sum over $(s', r)$ pairs will only have one legal term once the action $a$ is fixed. Substituting this into the Bellman equation

$$v_\pi(15) = 0.25[(-1 + v_\pi(12)) + (-1 + v_\pi(13)) + (-1 + v_\pi(14)) + (-1 + v_\pi(15))]$$

From Figure 4.1 (again, see [Exercise 4.1](../ch04_ex04-01/README.md)) we know the state-values of 12, 13, 14 so we can substitute these.

$$v_\pi(15) = 0.25(-4 - 22 -20 - 14 + v_\pi(15)) = 0.25v_\pi(15) - 15$$

$$\therefore \boxed{v_\pi(15) = -20}$$

For the second part, once the dynamics of state 13 are changed, this *could* change its state-value too per the Bellman equation above. However, because the Bellman equations for the neighbors of 13 ($v_\pi(12), v_\pi(9), v_\pi(14)$) depend on $v_\pi(13)$, their state-values will also change if $v_\pi(13)$ changes. By the same reasoning, the state-values of all non-terminal states will change due to this single modification of a transition from state 13 *if $v_\pi(13)$ is changed due to this modification. This would mean that the state-values in Figure 4.1 no longer apply and we must recompute the entire value function under the new dynamics.

I will walk through the process of recomputing the state-values followed by a discussion of a shorter solution below.

From the undiscounted Bellman equation we can set up a system of linear equations:

$$v_\pi(s) = \sum\limits_a \pi(a|s) \sum\limits_{s',r} p(s',r|s,a)[r+v_\pi(s')] \tag{1}$$

We can split the bracket and pull the sums inside

$$v_\pi(s) = \sum\limits_a \pi(a|s) \sum\limits_{s',r}p(s',r|s,a)r + \sum\limits_a \pi(a|s) \sum\limits_{s',r} p(s',r|s,a)v_\pi(s')$$

We know that $r=-1$ and $p(s',r|s,a)=1$ for legal state transitions and 0 otherwise. So the first term simplifies to $\sum_a \pi(a|s)\sum_{s',r}p(s',r|s,a)r = - \sum_a \pi(a | s) = -1$. So

$$v_\pi(s) = -1 + \sum\limits_a \pi(a|s) \sum\limits_{s',r} p(s',r|s,a)v_\pi(s')$$

Since $v_\pi(s')$ does not depend on $r$, we can simplify the dynamics function to just the state-transition probability measure

$$v_\pi(s) = -1 + \sum\limits_a \pi(a|s) \sum\limits_{s'}p(s'|s,a)v_\pi(s')$$

Once again we know that the state transitions are deterministic so $p(s'|s,a) = 1$ for legal transitions and 0 otherwise. We also know the policy in question is equiprobable random so $\pi(a|s) = 0.25$ for all $a \in \mathcal{A}(s), s$. So this simplifies to

$$v_\pi(s) = -1 + 0.25(v_\pi(\text{up nb}) + v_\pi(\text{down nb}) + v_\pi(\text{left nb}) + v_\pi(\text{right nb}))$$

Where $v_\pi(\text{up nb})$ denotes the state-value of the 'up-neighbor' of state $s$ and so on for down, left and right.

Upon close inspection, we can recognize the $0.25(...)$ term as a dot product between a policy-specific transition vector and the unknown state-values. For the equiprobable random policy, this vector consists of four 0.25 entries on each of the four legal state transitions from the current state and 0 otherwise. 

If we stack all $|\mathcal{S}|$ of these equations, we get the following system of equations:

$$v_\pi = r_\pi + P_\pi v_\pi$$

Let $n = |\mathcal{S}|$. Then $v_\pi \in \R^n$ with $v_\pi(i) = v_\pi(s_i)$, $r_\pi \in \R^n$ which has entries of -1, and $P_\pi \in \R^{n \times n}$. Rearranging 

$$v_\pi - P_\pi v_\pi = r_\pi$$

$$(I - P_\pi)v_\pi = r_\pi$$

$$v_\pi = (I - P_\pi)^{-1} r_\pi$$

We can solve this numerically. This is done by the code [here](../../suttonbarto/chapter4/exercise4_2.py). 

This code confirms that when we compute the 14 state-values with the original gridworld rules we obtain the numbers from Figure 4.1 in the case of $k=\infty$. This confirms the correctness of the code. When we add a state 15, we obtain $v_\pi(15) = -20$, confirming our calculation above as well. Interestingly, when we alter the transition dynamics for state 13 as per the problem, its state-value remains unchanged, i.e. $v_\pi(13) = -20$, and same for state 15, 

$$\therefore \boxed{v_\pi(15) = -20}$$

How could this be? 

## Discussion of a shorter solution
Observe that before the alteration, the 'down' action returned the agent to state 13, which has an original state-value of -20. We also know that the state-value of state 15 is -20. The key observation is that the state-value of state 15 *is not affected* by the alteration to state 13. This is because the value of a state only depends on the values of its *successor* states. In other words, allowing state 13 to transition *into* state 15 adds a predecessor but does not alter the successor states of state 15. Therefore, the state-value of state 15 remains unchanged at -20. 

So the pre-alteration value of state 13 was -20 and the value of state 15 is -20 before and after the alteration to state 13's dynamics. Once we make the alteration, the value of the successor state is actually unchanged. Pre-alteration, the 'down' action leads to state 13, which has value -20. Post-alteration, the 'down' action leads to state 15, which also has value -20. As a result, the value of state 13 is unchanged after the alteration. And since state 13's value is unchanged, so is state 15's. Hence $v_\pi(15) = -20$. 

We can confirm this argument empirically by altering the transition dynamics of state 15 such that the 'left' action moves to state 4 instead of state 12. Now, state 15 has a value of -17.3 and so when we alter state 13's dynamics, all of the state values in the grid change. So we conclude that this exercise displayed a very special case in which the alteration of a state dynamic happened to leave all state-values unchanged solely because the state-values being 'swapped' in the dynamics were exactly equal.