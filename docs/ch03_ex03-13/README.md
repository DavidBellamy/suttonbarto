# Exercise 3.13 - Action-value function in terms of state-value function

**Problem Statement**
Give an equation for $q_\pi$ in terms of $v_\pi$ and [the dynamics function] $p(s', r | s, a)$.

Where 

$v_\pi(s) \doteq \mathbb{E}_\pi[G_t | S_t = s]$ and $q_\pi(s,a) \doteq \mathbb{E}_\pi[G_t | S_t=s, A_t=a]$.

# Solution
The key insight behind this derivation is to realize that in order to get rid of the conditioning on $A_t$ present in $q_\pi$ we must use the Law of Total Expectation ("LOTE") over $S_{t+1}$ then invoke the Markov property to remove that conditioning. However, if we condition on $S_{t+1}$ then the corresponding return that we are taking the expectation of must have a matching time step. So $G_{t+1}$ for $S_{t+1}$ not $G_t$. Hence the flow is to first introduce $G_{t+1}$ then use LOTE to introduce $S_{t+1}$, invoke the Markov property to drop conditioning on $A_t, S_t$ and then rewrite the result in terms of $v_\pi$. 

The way to introduce $G_{t+1}$ into the definition of $q_\pi$ is to use the recurrence relation $G_t = R_{t+1} + \gamma G_{t+1}$. So by definition of $q_\pi$,

$q_\pi(s,a) \doteq \mathbb{E}_\pi[G_t | S_t=s, A_t=a] = \mathbb{E}_\pi[R_{t+1} + \gamma G_{t+1} | S_t=s, A_t=a]$

By linearity of expectation

$q_\pi(s,a) = \mathbb{E}_\pi[R_{t+1}|S_t=s,A_t=a] + \gamma\mathbb{E}_\pi[G_{t+1} | S_t=s,A_t=a]$

By definition of expectation, the first expectation term is

$\mathbb{E}_\pi[R_{t+1} | S_t=s, A_t=a] = \sum\limits_{r \in \mathcal{R}} r p(r | s, a)$

We can relate $p(r|s,a)$ to the dynamics function $p(s',r|s,a)$ via marginalization: 

$p(r|s,a) = \sum\limits_{s' \in \mathcal{S}} p(s',r|s,a)$

So the expected term term becomes

 $\mathbb{E}_\pi[R_{t+1} | S_t=s, A_t=a] = \sum\limits_{s' \in \mathcal{S}} \sum\limits_{r \in \mathcal{R}} r p(s', r | s, a)$

 Now if we could condition the second expectation term above on $S_{t+1}$ (to match the time step with $G_{t+1}$) we could rewrite it in terms of $v_\pi(s) \doteq \mathbb{E}_\pi[G_t | S_t=s]$. We can achieve this using the Law of Total Expectation:

$\mathbb{E}_\pi[G_{t+1} | S_t=s,A_t=a] = \sum\limits_{s' \in \mathcal{S}} \sum\limits_{r \in \mathcal{R}} \mathbb{E}_\pi[G_{t+1} | S_{t+1}=s', R_{t+1}=r, S_t=s, A_t=a] p(s', r | s, a)$

But the expected return only depends on *future* rewards ($t+2$ and beyond) which means conditioning on $R_{t+1}$ (or not) has no effect on the expectation. Similarly, since we are working with an MDP, conditioning on $S_t, A_t$ has no effect once we condition on $S_{t+1}$ by the Markov property. Therefore:

$\mathbb{E}_\pi[G_{t+1} | S_{t+1}=s', R_{t+1}=r, S_t=s, A_t=a] = \mathbb{E}_\pi[G_{t+1} | S_{t+1}=s'] = v_\pi(s')$

Rewriting everything above altogether, we obtain

$q_\pi(s,a) = \left( \sum\limits_{s' \in \mathcal{S}} \sum\limits_{r \in \mathcal{R}} r p(s', r | s, a) \right) + \left( \gamma \sum\limits_{s' \in \mathcal{S}} \sum\limits_{r \in \mathcal{R}} v_\pi(s') p(s', r | s, a) \right)$

Since both parenthetical terms share the same double sum, we can combine them

$q_\pi(s,a) = \sum\limits_{s' \in \mathcal{S}} \sum\limits_{r \in \mathcal{R}} r p(s', r | s, a) + \gamma v_\pi(s') p(s', r | s, a)$

And finally we can factor out the common term $p(s',r|s,a)$

$\therefore \boxed{q_\pi(s,a) = \sum\limits_{s' \in \mathcal{S}} \sum\limits_{r \in \mathcal{R}} p(s',r|s,a)[r + \gamma v_\pi(s')]} \quad \square$

So the action-value function $q_\pi$ is the average immediate reward $\mathbb{E}_\pi[R_{t+1}|S_t=s, A_t=a]$ plus the expected gamma-discounted next-state value $v_\pi(s')$ under the environment's transition probabilities.