# Exercise 3.7 - The issue with sparse rewards

**Problem Statement**
Imagine that you are designing a robot to run a maze. You decide to give it a reward of +1 for escaping from the maze and a reward of zero at all other times. The task seems to break down naturally into episodes — the successive runs through the maze — so you decide to treat it as an episodic task, where the goal is to maximize expected total reward (3.7). After running the learning agent for a while, you find that it is showing no improvement in escaping from the maze. What is going wrong? Have you effectively communicated to the agent what you want it to achieve? 

$$G_t \doteq R_{t+1} + R_{t+2} + R_{t+3} + ... + R_T \tag{3.7}$$

# Solution
In the first episode, the robot is unlikely to solve the maze and so its returns are likely to remain fixed at $0$. This fails to incentivize the robot to try to solve the maze because the non-zero rewards are too sparse. From the robot's perspective, whether it sits still or moves around randomly, its return will be the same, i.e. $0$. 

In theory we have effectively communicated what we want the agent to achieve. We want the agent to solve the maze and our reward signal gives a reward of +1 for that, 0 otherwise. This avoids the temptation to bake in prior knowledge into the reward signal (e.g. giving a reward inversely proportional to the agent's distance to the maze's exit).

To encourage more exploration, we might give a small negative reward at each time step. This densifies the reward signal and combats the earlier sparsity issue.