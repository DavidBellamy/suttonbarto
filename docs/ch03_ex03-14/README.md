# Exercise 3.14 - Center state-value in Gridworld

**Problem Statement**
The Bellman equation (3.14; below) must hold for each state for the value function $v_\pi$ shown in Figure 3.2 (right; also below) of Example 3.5 (also below). Show numerically that this equation holds for the center state, valued at +0.7, with respect to its four neighboring states, valued at +2.3, +0.4, -0.4, and +0.7. (These numbers are accurate only to one decimal place.)

$$v_\pi(s) = \sum\limits_a \pi(a|s) \sum\limits_{s',r} p(s',r|s,a)[r + \gamma v_\pi(s')] \quad \forall s \in \mathcal{S} \tag{3.14}$$

**Example 3.5: Gridworld**
Figure 3.2 (left; below) shows a rectangular gridworld representation of a simple finite MDP. The cells of the grid correspond to the states of the environment. At each cell, four actions are possible: north, south, east and west, which deterministically cause the agent to move one cell in the respective direction on the grid. Actions that would take the agent off the grid leave its location unchanged, but also result in a reward of -1. Other actions result in a reward of 0, except those that move the agent out of the special states A and B. From state A, all four actions yield a reward of +10 and take the agent to A'. From state B, all actions yield a reward of +5 and take the agent to B'. 

![fig3-2](./fig3-2.png)
Figure 3.2: Gridworld example: exceptional reward dynamics (left) and state-value function for the equiprobable random policy (right). 

# Solution
Let $s=12$ denote the center state mentioned in the problem and $s=7, 11, 13, 17$ be its four neighbors with state-values of 2.3, 0.7, 0.4, and -0.4, respectively. This is following row-major order with zero-indexing in the top left corner of the grid.

Regardless of which state $s$ the agent is in, the policy is equiprobable random and so $\pi(a|s) = 0.25$ for all $a \in \mathcal{A}$. Note that $\mathcal{A}$ does not depend on the state $s$ in Gridworld so we do not denote it by $\mathcal{A}(s)$. This lets us pull $\pi(a|s)$ out in front of the sum over actions.

$v_\pi(12) = 0.25 \sum\limits_a \sum\limits_{s', r} p(s',r | s,a)[r + \gamma v_\pi(s')]$ 

We can further simplify this equation by noting the fact that $p(s',r|s,a) = 1$ for the $(s',r)$ pair that deterministically follows from $(s,a)$ and 0 otherwise. This means that the double sum over $(s', r)$ pairs simplifies to the single term where $p(s',r|s,a) = 1$. Denote this successor state and reward $s'(s, a)$ and $r(s, a)$, respectively. The Bellman equation becomes

$v_\pi(12) = 0.25 \sum\limits_a [r(s,a) + \gamma v_\pi(s'(s,a))]$

The sum over all actions $a \in \mathcal{A}$ consists of four terms for moving North, South, East and West. We know that all four reward terms are 0 since none hit an edge and the center state is neither of the two special states A or B. Therefore, $r(s,a) = 0$ for all $a$ in this equation.

$v_\pi(12) = 0.25 \gamma \sum\limits_a v_\pi(s'(s,a))$

We already know the state-values of the four states surrounding the center state $s=12$ so we can plug these into the equation.

$v_\pi(12) = 0.25 \times 0.9 \left(2.3 + 0.7 + 0.4 - 0.4 \right) = 0.25 \times 0.9 \times 3 = 0.675 \approx 0.7$

$\therefore \boxed{v_\pi(12) = 0.675 \approx 0.7}$ which confirms the state-value for the center state in Figure 3.2 above.