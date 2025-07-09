# Exercise 3.2 - Limits of MDPs

**Problem Statement**
Is the MDP framework adequate to usefully represent *all* goal-directed learning tasks? Can you think of any clear exceptions?

# Solution
For a system of variables (or signals) to fit the MDP framework it must admit the following elements (according to Bellman, 1957):
1. $\mathcal{S}$: state space. 
2. $\mathcal{A}$: action space.
3. $P(s', r | s, a)$: a transition kernel.
4. $\gamma$ or $T$: a discount factor $\gamma$ for MDPs with infinite horizons or a finite horizon of length $T$. $0 \le \gamma \le 1$ ensures that the expectation of future rewards is finite.
5. $\mu$: an initial state distribution.

Where the Markov property holds, namely:

$P(s', r | s, a, \text{history}) = P(s', r | s, a), \forall \text{history}.$

There are several ways to pose a challenge to the MDP framework but there are work-arounds for almost all of them:

**Non-stationarity**: $P(s',r|s,a)$ changes with $t$. We can fold this into the MDP framework by parameterizing the transition kernel with time and satisfying the Markov property *per time step*: 

$$P_t(s',r|s,a, \text{history}) = P_t(s',r|s,a) \forall t, \text{history}$$

or by folding the clock into the state: $\tilde{S}_t = (S_t, t)$ and satisfying the original Markov property.

**Partial observability**: where the agent observes $O_t = g(S_t, \text{noise})$ at time $t$ instead of the underlying state itself. Despite the observations breaking the Markov property:

$$P(O_{t+1} | O_t,A_t) \neq P(O_{t+1}|O_{0:t},A_{0:t})$$

we can assert or assume that the underlying state dynamics do obey the original Markov property. This is a fair assumption at a microscopic level if we believe that the Universe is fully deterministic (i.e. Laplace's demon) and that its apparent randomness emerges due to chaotic dynamics or other means. However, it is not always obvious when we are asserting this for a system of coarse-grained variables, which may not behave deterministically due to hidden degrees of freedom. 

**Infinite state or action spaces**: an MDP must admit a transition kernel but there is no restriction that says this kernel must be over finite $\mathcal{S,A}$. When $\mathcal{S,A}$ are infinite, we need the transition kernel $P(s', r | s, a)$ to be a valid probability measure and that just means that we can define a $\sigma$-algebra over the state space and reward domain, e.g. $\mathcal{B}_\mathcal{S} \otimes \mathcal{B}_\R$ and for all events (i.e. measurable $(s', r)$ pairs) $B \in \mathcal{B}_\mathcal{S} \otimes \mathcal{B}_\R$, $P(B | s,a) \ge 0, P(\mathcal{S} \times \R | s,a) = 1$ and $P$ is countably additive.

**Continuous time**: there are natural extensions to continuous-time MDPs. 

**Ill-defined rewards**: the MDP framework requires a well-defined scalar reward. This is not always available for all problems such as those that have complex evaluations that are difficult to distill into a scalar. Vector-valued rewards are work-able although they require some scalarization. 

**Multiple agents**: this may cause the MDP's dynamics to be nonstationary, but we discussed a workaround for this already. Another workaround in this scenario is to incorporate observations about other agents into the observations of a given agent. 

Where the usefulness of MDPs is particularly stretched: 
* Very long (even infinite)-horizon tasks with very sparse rewards, i.e. sequences $\{S, A, R\}_i$ where $R$ is mostly $0$ and $i$ is very large. It can still be represented by an MDP but it might not be the most useful representation since the reward signal $R$ takes the trivial value most of the time. 
* Tasks with very poor observability. In the limit, if the observations $O_t$ become pure noise then they take their trivial value, contributing no information to the MDP. 
* Tasks that do not admit a well-defined scalar reward signal (see above).
* Systems with rapidly evolving dynamics, i.e. transition kernels. In the limit, if the dynamics change at infinitesimally small time steps, then there is no decision rule to be learned – the environment is simply too chaotic.
* Inverse RL, where the goal is to infer the reward signal. In this setting, only dynamics are observed $P(s'|s,a)$ without reward signal. This is a learning task but perhaps doesn't qualify as "goal-directed" per the problem. That is a bit ambiguous. 