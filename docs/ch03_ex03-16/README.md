# Exercise 3.16 - Adding a constant to all rewards in an episodic task

**Problem Statement**
[Following on from [Exercise 3.15](../ch03_ex03-15/README.md)] Now consider adding a constant $c$ to all the rewards in an *episodic* (emphasis mine) task, such as maze running. Would [adding a constant to all rewards] have any effect, or would it leave the task unchanged as in the continuing task above? Why or why not? Give an example.

# Solution
In Exercise 3.15, we showed that 

$$G'_t = G_t + c\sum\limits_{k=0}^\infty \gamma^k$$

without assuming that the task is continuing or episodic. However, in an episodic task the horizon is finite and varies in length between episodes. Let $T$ be the random variable representing the length of each episode. Then

$$G'_t = G_t + c \sum\limits_{k=0}^{T-1} \gamma^k$$

For a finite geometric series, the sum is equal to $\frac{1 - \gamma^T}{1-\gamma}$. Since $T$ is a random variable, the value of this fraction is random too. So

$$G'_t = G_t + \frac{c(1-\gamma^T)}{1-\gamma}$$

Substituting this into the expression for state-value

$$v'_\pi(s) = \mathbb{E}_\pi[G'_t | S_t = s] = \mathbb{E}_\pi\left[G_t + \frac{c(1-\gamma^T)}{1-\gamma} | S_t = s\right]$$

Where $v'_\pi$ denotes the modified state-values obtained by adding a constant $c$ to all rewards. By linearity of expectation

$$v_\pi(s) = \mathbb{E}_\pi[G_t | S_t = s] + \mathbb{E}_\pi\left[\frac{c(1-\gamma^T)}{1-\gamma} | S_t = s\right]$$

Recognizing the first expectation as $v_\pi(s)$ and pulling constants out of the second expectation

$$v'_\pi(s) = v_\pi(s) + \frac{c}{1-\gamma}(1 - \mathbb{E}_\pi[\gamma^T | S_t=s])$$

The expectation $\mathbb{E}_\pi[\gamma^T | S_t=s]$ is not necessarily constant in an episodic task. If all episodes were the same length, say $T_\text{max}$, then this would be a constant and so all state-values $v'_\pi$ would be offset by a constant like in the continuing case. If episodes end after each step with state-independent probability $p$ then $T$ follows a geometric distribution $\Pr(T=k) = p(1-p)^{k-1}, k=1,2,3,...$ and the expectation of a geometric random variable is known $\mathbb{E}[\gamma^T] = \frac{p\gamma}{1 - \gamma(1-p)}$. As $p \rarr 0$, $\mathbb{E}[\gamma^T] \rarr 0$ and so $v'_\pi$ approaches its values in the continuing case. 

But we cannot assume that episodes end after each step with *state-independent probability* in general. And we can't assume that each episode has the same length. 

So we conclude that adding a constant to all rewards in an episodic task does have an effect on the task since the quantity added to the state-values varies from policy to policy and from state to state (i.e. $\mathbb{E}_\pi[\gamma^T | S_t=s]$ depends on $\pi, s$). This incentivizes different (optimal) behavior depending on the sign and magnitude of $c$. 

Example: in a maze running task, if we add $c=1$ to every reward, a path that wanders $k$ extra steps gains $\sum_{i=0}^{k-1} \gamma^i > 0$ extra return and so the agent will prefer longer episodes and will loop instead of heading straight to the exit. Conversely, $c=-1$ encourages the shortest path more strongly than if $c=0$ because there is a penalty incurred for longer paths. 