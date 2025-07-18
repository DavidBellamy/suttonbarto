# Exercise 3.29 - Rewriting Bellman equations

**Problem Statement**
Rewrite the four Bellman equations for the four value functions ($v_\pi, v_*, q_\pi, q_*$) in terms of the three argument function $p$ from equation 3.4 and the two-argument function $r$ from equation 3.5. 

## Equations 3.4 and 3.5

$$p(s'|s,a) \doteq \Pr\{S_t=s' | S_{t-1}=s, A_{t-1}=a\} = \sum\limits_{r \in \mathcal{R}} p(s', r | s, a) \tag{3.4}$$

$$r(s,a) \doteq \mathbb{E}[R_t | S_{t-1} = s, A_{t-1}=a] = \sum\limits_{r \in \mathcal{R}} r \sum\limits_{s' \in \mathcal{S}} p(s', r | s, a) \tag{3.5}$$

# Solution
Start with the Bellman equation for $v_\pi$ (equation 3.14)

$v_\pi(s) = \sum\limits_a \pi(a|s) \sum\limits_{s', r} p(s', r | s,a)[r + \gamma v_\pi(s')] \quad \forall s \in \mathcal{S}$

Distribute $p(s',r|s,a)$ 

$v_\pi(s) = \sum\limits_a \pi(a|s) \left( \sum\limits_{s', r}r p(s', r | s,a) + \gamma \sum\limits_{s',r} p(s', r | s, a) v_\pi(s') \right)$

Since $v_\pi(s')$ does not change with $r$, we can pull it in front of the sum over $r$.

$v_\pi(s) = \sum\limits_a \pi(a|s) \left( \sum\limits_{s', r}r p(s', r | s,a) + \gamma \sum\limits_{s'} v_\pi(s') \sum\limits_r p(s', r | s, a) \right)$

We can substitute $p(s'|s,a)$ now

$v_\pi(s) = \sum\limits_a \pi(a|s) \left( \sum\limits_{s', r}r p(s', r | s,a) + \gamma \sum\limits_{s'} v_\pi(s') p(s' | s,a) \right)$

Similarly, $r$ does not change with $s'$ so we can pull it in front of that sum

$v_\pi(s) = \sum\limits_a \pi(a|s) \left( \sum\limits_{r}r \sum\limits_{s'} p(s', r | s,a) + \gamma \sum\limits_{s'} v_\pi(s') p(s' | s,a) \right)$

Now we can substitute $r(s,a)$

$\therefore \boxed{v_\pi(s) = \sum\limits_a \pi(a|s)\left[r(s,a) + \gamma \sum\limits_{s'} v_\pi(s')p(s'|s,a)\right]} \quad \forall s \in \mathcal{S}$

For $v_*(s)$, start with the Bellman optimality equation for $v_*$ (equation 3.19)

$v_*(s) = \max\limits_a \sum\limits_{s', r} p(s', r|s,a)[r + \gamma v_*(s')]$

We follow the same steps of distributing $p(s', r | s, a)$, splitting the sum, pulling $r$ in front of the sum over $s'$ and pulling $v_*(s')$ in front of the sum over $r$ then substituting in $r(s,a)$ and $p(s'|s,a)$

$\boxed{v_*(s) = \max\limits_{a \in \mathcal{A}(s)} [r(s, a) + \gamma \sum\limits_{s'} p(s' | s, a) v_*(s')}$

For $q_\pi$ we can follow a similar derivation. We know from [Exercise 3.17](../ch03_ex03-17/README.md) that the Bellman equation for $q_\pi$ is

$q_\pi(s, a) = \sum\limits_{s', r}\left(p(s',r|s,a)[r + \gamma \sum\limits_{a'}q_\pi(s',a')\pi(a'|s')]\right) \quad \forall a, s \in \mathcal{S, A}(s)$

Again distribute $p(s', r|s,a)$ and apply the same steps as before

$\boxed{q_\pi(s, a) = r(s, a) + \gamma \sum\limits_{s'} p(s'|s,a) \sum\limits_{a'} q_\pi(s', a') \pi(a'|s')} \quad \forall a,s \in \mathcal{S, A}(s)$

And for $q_*$ we can begin from its Bellman optimality equation (equation 3.20)

$q_*(s,a) = \sum\limits_{s', r} p(s',r|s,a)[r + \gamma \max\limits_{a'} q_*(s', a')]$

Apply the same steps as above

$\boxed{q_*(s, a) = r(s, a) + \gamma \sum\limits_{s'} p(s' | s, a) \max\limits_{a'} q_*(s', a')} \quad \forall a, s \in \mathcal{S, A}(s)$

In summary, the rewritten Bellman equations are

$v_\pi(s) = \sum\limits_a \pi(a|s)\left[r(s,a) + \gamma \sum\limits_{s'} v_\pi(s')p(s'|s,a)\right] \quad \forall s \in \mathcal{S}$

$v_*(s) = \max\limits_{a \in \mathcal{A}(s)} [r(s, a) + \gamma \sum\limits_{s'} p(s' | s, a) v_*(s') \quad \forall s \in \mathcal{S}$

$q_\pi(s, a) = r(s, a) + \gamma \sum\limits_{s'} p(s'|s,a) \sum\limits_{a'} q_\pi(s', a') \pi(a'|s') \quad \forall a,s \in \mathcal{S, A}(s)$

$q_*(s, a) = r(s, a) + \gamma \sum\limits_{s'} p(s' | s, a) \max\limits_{a'} q_*(s', a') \quad \forall a, s \in \mathcal{S, A}(s)$

$\square$