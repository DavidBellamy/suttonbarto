# Exercise 3.10 - Proof of the infinite geometric series identity

**Problem Statement**
Prove the following equality:

$$\sum\limits_{k=0}^\infty \gamma^k = \frac{1}{1 - \gamma}$$

# Solution
First let's define the *finite* partial sum up to power $n$:
$$S_n = 1 + \gamma + \gamma^2 + ... + \gamma^n$$

We can get most terms in the sum to cancel if we multiply by $1-\gamma$:
$$(1-\gamma)S_n = (1-\gamma)(1 + \gamma + \gamma^2 + ... + \gamma^n) = 1 - \gamma^{n+1}$$

Hence $S_n = \frac{1 - \gamma^{n+1}}{1 - \gamma}$

Now let $n \rarr \infty$. Since $|\gamma| \lt 1$, then $\gamma^{n+1} \rarr 0$. So 

$\therefore \boxed{S_\infty = \frac{1}{1 - \gamma}}$

Note that this is a standard proof of the geometric series identity. The technique is known as an algebraic 'telescoping' proof and can be used to prove the identity for many sums.