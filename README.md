# Deep_Reinforcement_Learning_on_Car_Racing_Game
## Task
Our project explores the algorithms of reinforcement learning (RL) used in game playing. We study several RL algorithms and implement them in a car racing game. The RL methods include, but not limited to, DQN, Double DQN, and Dueling DQN. After the RL methods been implemented, we make comparison between these results and analyze the characteristics of each method.

## Related Work
[Playing Atari with Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)

[Human-level control through deep reinforcement learning](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf)

[Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/pdf/1509.06461.pdf)

[Dueling Network Architectures for Deep Reinforcement Learning](http://proceedings.mlr.press/v48/wangf16.pdf)

## Game Environment
Car-Racing-v0 from gym library as our basic environment \n
Agent: car
States: pics taken every 4 frames of 96×96 pixels
Actions: forward, brake, left, right
Reward: 
if action detected, reward -= 0.1
if running out of playfield, reward -= 150



