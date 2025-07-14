# Exercise 3.8 - Computing returns from rewards

**Problem Statement**
Suppose $\gamma = 0.5$ and the following sequence of rewards is received $R_1 = -1, R_2 = 2, R_3 = 6, R_4 = 3, R_5 = 2$ with $T=5$. What are $G_0, G_1, ..., G_5$? Hint: Work backwards.

# Solution
Since $T$ is defined, we are under an episodic reward/return formulation:

$$G_0 = R_1 + \gamma R_2 + \gamma^2 R_3 + \gamma^3 R_4 + \gamma^4 R_5$$

And by recurrence,

$$G_0 = R_1 + \gamma G_1$$

So $G_1 = R_2 + \gamma G_2$, $G_2 = R_3 + \gamma G_3$, $G_3 = R_4 + \gamma G_4$, $G_4 = R_5 + \gamma G_5$ and $G_5 = 0$ since no more rewards can be obtained once the terminal state at $t=5$ has been reached. 

Working backwards, we get that $G_4 = 2, G_3 = 3 + 2\gamma = 4, G_2 = 6 + 4\gamma = 8, G_1 = 2 + 8\gamma = 6, G_0 = -1 + 6\gamma = 2$.

$\therefore$ $G_0 = 2, G_1 = 6, G_2 = 8, G_3 = 4, G_4 = 2, G_5 \doteq 0$. 
