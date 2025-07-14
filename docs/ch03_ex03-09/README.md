# Exercise 3.9 - Early Returns with Infinite Horizons

**Problem Statement**
Suppose $\gamma=0.9$ and the reward sequence is $R_1=2$ followed by an infinite sequence of 7s. What are $G_1$ and $G_0$? 

# Solution
As in [Exercise 3.8](../ch03_ex03-08/README.md), we can use the recurrence relation between time-adjacent returns. 

$$G_0 = R_1 + \gamma G_1 \\ G_1 = R_2 + \gamma G_2$$

We know that $R_k = 7$ for $k \gt 1$. So $G_2 = \sum\limits_{k=0}^\infty 7 \gamma^k = 7 \sum\limits_{k=0}^\infty \gamma^k = \frac{7}{1 - \gamma} = 70.$

$\therefore$ $G_1 = 7 + 0.9*70 = 70$ and $G_0 = 2 + 0.9*70 = 65.$
