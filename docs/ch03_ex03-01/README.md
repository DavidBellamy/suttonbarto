# Exercise 3.1 - Finite MDP Examples

**Problem Statement**
Devise three example tasks of your own that fit into the MDP framework, identifying for each its states, actions, and rewards. Make the three examples as *different* from each other as possible. The framework is abstract and flexible and can be applied in many different ways. Stretch its limits in some way in at least one of your examples.

# Solution

Example 1: Self-driving car. States: moment-by-moment data from a collection of sensors on the car: lidar, cameras, current speed and acceleration, gas level. Actions: applicaton of the gas and brake pedals, turning of the steering wheel, turning indicators, windshield wipers, car lights, horn. Reward: a scalar that is a linear combination of how close the current speed is to the speed limit (perhaps squared distance), how jerky the motion is, and a +/- 1 reward for every traffic rule that is obeyed vs. violated (e.g. stopping at a stop sign, yielding for pedestrians). This would not be safe to use in the real world!

Example 2: Predictive coding by the human brain's deep pyramidal "immitation" neurons in cortical layers 5 & 6. States: recent neuron firing activity from neurons in shallower cortical layers, e.g. layers 2 & 3. Actions: genetic and epigenetic changes to the L5/6 neurons to adjust their synaptic weights and firing patterns. Rewards: the error signal computed as the signed difference between the L2/3 neuron firing pattern and the L5/6 neurons' prediction of that firing pattern.

Example 3: Intrinsic reward on a space-faring humanoid robot. States: various sensor inputs on the humanoid (camera vision, mechanosensors, etc.). Actions: various actuators on the humanoid. Rewards: the mutual information (or a variational approximation) between the current state and a sequence of future (state, action) tuples of length H; $r_t = I(a_{t:t+H}; s_{t:t+H} | s_t)$.