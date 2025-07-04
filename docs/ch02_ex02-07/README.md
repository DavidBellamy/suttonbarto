# Exercise 2.7 – Unbiased Constant-Step-Size Trick

**Problem Statement**
In most of this chapter we have used
sample averages to estimate action values because sample averages do not produce the
initial bias that constant step sizes do (see the analysis leading to (2.6)). However, sample
averages are not a completely satisfactory solution because they may perform poorly
on nonstationary problems. Is it possible to avoid the bias of constant step sizes while
retaining their advantages on nonstationary problems? One way is to use a step size of

$\beta_n \doteq \alpha/\bar{o}_n,$

to process the $n$ th reward for a particular action, where $\alpha>0$ is a conventional constant step size, and $\bar{o}_n$ is a trace of one that starts at 0:

$\bar{o}_n \doteq \bar{o}_{n-1} + \alpha(1-\bar{o}_{n-1}), $ for $n \geq 0$, with $\bar{o}_0 \doteq 0.$

Carry out an analysis like that in (2.6) to show that $Q_n$ is an exponential recency-weighted average *without initial bias*. 

# Solution

Per the exercise, the update rule is as follows:

$$Q_{n+1} \doteq Q_n + \beta_n[R_n - Q_n] = \beta_n R_n + (1-\beta_n)Q_n$$

Recall equation 2.6 in the main text:

$$ Q_{n+1} = (1-\alpha)Q_1 + \sum\limits_{i=1}^n \alpha(1-\alpha)^{n-i} R_i$$

The sum over past rewards $R_i$ is an exponential recency-weighted average, since the weight on each reward term decays exponentially in the exponent $n-i$, which measures recency of the reward. So we would like to show that the update rule above is equal to this summation without the term for $Q_1$, i.e. without initial bias.

Substitute the definition of $Q_n$ into the update rule:

$$Q_{n+1} = \beta_n R_n + (1-\beta_n)\left[\beta_{n-1} R_{n-1} + (1-\beta_{n-1})Q_{n-1}\right]$$

Substitute in the definition of $Q_{n-1}$ for the recursive pattern to reveal itself:

$$Q_{n+1} = \beta_n R_n + (1-\beta_n)\left[\beta_{n-1} R_{n-1} + (1-\beta_{n-1})\left[\beta_{n-2} R_{n-2} + (1 - \beta_{n-2}) Q_{n-2} \right]\right]$$

Let's make a table for the coefficients on reward terms:

| Term | Coefficient |
|---------|----------|
| $R_n$ | $\beta_n$ |
| $R_{n-1}$ | $(1 - \beta_n) \beta_{n-1}$|
|$R_{n-2}$| $(1 - \beta_n) (1 - \beta_{n-1})\beta_{n-2}$ |
| ...| ...|
| $R_{k}$ | $ \beta_k \prod\limits_{j=k+1}^n (1 - \beta_j)$ |

And the same for the coefficients on past value estimates:

| Term | Coefficient |
|---------|----------|
| $Q_n$ | $1 - \beta_n$ |
| $Q_{n-1}$ | $(1 - \beta_n)(1 - \beta_{n-1})$ |
| $Q_{n-2}$ | $(1 - \beta_n)(1 - \beta_{n-1})(1 - \beta_{n-2})$|
| ... | ... |
| $Q_1$ | $(1 - \beta_n)(1 - \beta_{n-1}) ... (1 - \beta_{1})$ |

However, by definition $\bar{o}_1 = \bar{o}_0 + \alpha(1 - \bar{o}_0) = \alpha$ since $\bar{o}_0 \doteq 0$. This causes the term $(1 - \beta_1) = (1 - \alpha/\bar{o}_1)$ to equal $0$, which makes the cumulative product weight on $Q_1$ equal $0$. Therefore, there is *no initial bias*. 

Therefore, the update rule can be written as:

$$Q_{n+1} = \sum\limits_{k=1}^n \left[ \beta_k \prod_{j=k+1}^n (1 - \beta_j) \right] R_k $$

The term in square brackets is the one we wish to show is an exponential recency-weighted average.

Let's unpack the recursion of $\bar{o}_n$:

$$\bar{o}_n = \bar{o}_{n-1} + \alpha(1 - \bar{o}_{n-1}) = (1-\alpha)\bar{o}_{n-1} + \alpha$$

Substitute the definition of $\bar{o}_{n-1}$

$$\bar{o}_n = (1-\alpha)((1 - \alpha)\bar{o}_{n-2} + \alpha) + \alpha$$

Hence $\bar{o}_n = (1 - \alpha)^n \bar{o}_0 + \alpha \sum\limits_{k=0}^{n-1} (1 - \alpha)^k =\alpha \sum\limits_{k=0}^{n-1} (1 - \alpha)^k.$

By geometric series, the sum is

$$\frac{1 - (1 - \alpha)^n}{1 - (1 - \alpha)}$$

So $\bar{o}_n = 1 - (1 - \alpha)^n$. 

Let $A \doteq 1 - \alpha$ then $\beta_n = \frac{\alpha}{\bar{o}_n} = \frac{1 - A}{1 - A^n}$. 

So $1 - \beta_j = 1 - \frac{1 - A}{1 - A^j} = \frac{1 - A^j - (1 - A)}{1 - A^j} = \frac{A(1-A^{j-1})}{1 - A^j}$

Let $W_k$ be the weight in the update rule for an arbitrary reward $R_k$. Substitute these expressions for $\beta$ and $1-\beta$:

$$W _{k} \doteq \beta_k \prod\limits_{j=k+1}^n (1 - \beta_j) = \frac{1-A}{1-A^k} A^{n-k} \prod\limits_{j=k+1}^n \frac{1 - A^{j-1}}{1 - A^j}$$

Note that each $1-\beta_j$ term in the product contains a multiplicative factor $A$ so we can pull out $A^{n-k}$ such terms from the product over $n-k$ indices. 

The cumulative product cancels all but it's final denominator of $1 - A^n$ since each denominator is equal to the subsequent term's numerator. The outside term $1 - A^k$ cancels with the first term's numerator. All that is left is the final denominator of the cumulative product $1 - A^n$. 

So $W_k = \frac{(1 - A) A^{n-k}}{1 - A^n} = \frac{\alpha (1 - \alpha)^{n-k}}{1 - (1 - \alpha)^n}$. 
 
Substituting $W_k$ back into the update rule, we obtain:

$$Q_{n+1} = \sum\limits_{k=1}^n \frac{\alpha (1 - \alpha)^{n-k}}{1 - (1 - \alpha)^n} R_k = \frac{\alpha}{1 - (1 - \alpha)^n} \sum\limits_{k=1}^n (1-\alpha)^{n-k} R_k$$

It seems likely that the problem statement forgot to mention that $0 < \alpha < 1$ (it only said $\alpha > 0$). With this assumption, then $0 < 1-\alpha < 1$, which means that $(1-\alpha)^{n-k}$ will decay towards $0$ exponentially as the exponent $n-k$ grows. This exponent measures how long ago the reward $R_k$ was encountered since it grows as $k \rarr 1$. 

 This clearly reveals that the weight $(1-\alpha)^{n-k}$ on each reward $R_k$ decays exponentially as a function of how recent the reward was obtained. This proves that $Q_n$ is an exponential recency-weighted average *without initial bias* $\square$.