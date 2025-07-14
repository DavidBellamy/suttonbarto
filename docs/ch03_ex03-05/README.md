# Exercise 3.5 - Episodic Modification for the Transition Distribution

**Problem Statement**
The equations in Section 3.1 are for the continuing case and need to be modified (very slightly) to apply to episodic tasks. Show that you know the modifications needed by giving the modified version of equation 3.3: 
$$\sum\limits_{s' \in \mathcal{S}} \sum\limits_{r \in \mathcal{R}} p(s',r|s,a) = 1, \quad \forall s \in \mathcal{S}, a \in \mathcal{A}(s) \tag{3.3}$$

# Solution

Equation 3.3 is an instance of the law of total probability ("LOTP"). It says that, for any fixed state $s$ and action $a$, the probabilities of all possible $(s', r)$ outcomes must sum to 1, ensuring the distribution $p(s',r | s,a)$ is valid. 

This constraint on the one-step transition distribution of an MDP applies equally to continuing tasks as to episodic tasks. However, with episodic tasks we must also specify the termination condition and its associated probabilities. Namely, a terminal state is one where there are no actions available, i.e. $\mathcal{A}(s_T) = \empty$ for all terminal states $s_T$. This means that the distribution $p(s',r|s,a)$ is undefined for $s = s_T$ since the conditioning event $(s_T, a)$ cannot occur for any $a$ by definition of a terminal state. 

To avoid this from happening, we must only condition the distribution on non-terminal states. However, we must sum over terminal states (in addition to non-terminal states) to obtain unity since terminal states are possible destinations in the transition graph of an MDP. 

If we use $\mathcal{S}$ to denote the states excluding the terminal ones, and $\mathcal{S^+} = S \cup \{s_T\}$ as the set of states including terminal ones, then the LOTP for episodic tasks is:

$$\sum\limits_{s' \in \mathcal{S^+}} \sum\limits_{r \in \mathcal{R}} p(s',r|s,a) = 1, \quad \forall s \in \mathcal{S}, a \in \mathcal{A}(s)$$