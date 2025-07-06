# Exercise 2.9 - Gradient Bandits

**Problem Statement**
Show that in the case of two actions, the soft-max distribution [in equation 2.11 (below)] is the same as that given by the logistic, or sigmoid, function often used in statistics and artificial neural networks.

$$\Pr\{A_t=a\} \doteq \frac{e^{H_t(a)}}{\sum_{b=1}^k e^{H_t(b)}} \tag{2.11}$$

# Solution

With only two actions, the probability of selecting action 1 is

$$\Pr\{A_t=1\} = \frac{e^{H_t(1)}}{e^{H_t(1)} + e^{H_t(2)}}$$

Divide by $e^{H_t(1)}$

$$\Pr\{A_t=1\} = \frac{1}{1 + e^{H_t(2) - H_t(1)}}$$

Negate the exponent

$$\Pr\{A_t=1\} = \frac{1}{1 + e^{-(H_t(1) - H_t(2))}}$$

Let $x = H_t(1) - H_t(2)$. Then

$$\Pr\{A_t=1\} = \frac{1}{1 + e^{-x}} = \sigma(x) \quad \square$$

$\therefore$ With two actions, the softmax distribution in equation 2.11 can be reduced to a sigmoid function where the argument is the difference between numerical preferences $H_t(1) - H_t(2)$.