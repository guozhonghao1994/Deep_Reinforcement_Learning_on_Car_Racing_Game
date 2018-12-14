# Deep_Reinforcement_Learning_on_Car_Racing_Game

![License](https://img.shields.io/badge/license-apache2_2-blue.svg)

## Task
The aim of our team was to explore three different DQN reinforcement learning networks. First, we learned and implemented Deep Q-network (DQN). Then, to improve Q value estimation method, we implemented Double Deep Q-network (DDQN), after that, we managed to improve improve network structure, so we implemented Dueling Deep Q-network (Dueling DQN). In experimental part, we trained each model for more than 10 hours and recorded and plotted average reward and average Q value of each model as  experimental results. Finally, we made comparison among these results and it showed that DDQN performed best; followed by DQN while Dueling network had the worst performance.

## Related Work
[Playing Atari with Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)

[Human-level control through deep reinforcement learning](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf)

[Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/pdf/1509.06461.pdf)

[Dueling Network Architectures for Deep Reinforcement Learning](http://proceedings.mlr.press/v48/wangf16.pdf)

## Game Environment
OpenAI [Car Racing-v0](https://gym.openai.com/envs/CarRacing-v0/)

![](https://media.giphy.com/media/3og0IEKu84Ros9izyU/giphy.gif)

## Algorithm
We try DQN, Double DQN(DDQN) and dueling DQN. Please refer to the [presentation](https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/Presentation.pdf) for detailed algorithm explanation. Also, you should have some basic knowledge on [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning) and [Q-learning](https://en.wikipedia.org/wiki/Q-learning). 

## Installation
1. `pip install -r requirements.txt`

    necessary module: `tensorflow`, `pygame`, `gym`, `Box2D`, `VC++ 14.0` ...

2. In DQN/DDQN/dueling DQN folder, run `python car_runner_main.py`

3. If you'd like to utilize the trained model, switch `load_checkpoint = True` in *python car_runner_main.py*

4. On CPU, it takes about 8 hours to get a well-trained model.

## Introduction
The DQN,DDQN and dueling DQN have similar structures. Take DQN for example:

`DQN/car_runner_main.py` - main entrance, the executable file

`DQN/dqn/agent.py` - DQN model

`DQN/dqn/experience_replay.py` - experience replay

`data/plot.py` - plot figures

## Result
### Training Result
<p align="center">
    <img src="https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/figure/Figure_10.png" alt="Sample"  width="352" height="260">
    <img src="https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/figure/Figure_11.png" alt="Sample"  width="352" height="260">
    <img src="https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/figure/Figure_12.png" alt="Sample"  width="352" height="260">

### Test Result
<p align="center">
    <img src="https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/figure/start.gif" alt="Sample"  width="300" height="260">
    <img src="https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/figure/play.gif" alt="Sample"  width="300" height="260">
    
| DQN    | DDQN   | Dueling DQN | Human   |
| ---    | ---    | ---         | ---     |
|  755   | 784.95 | 737.35      | 216.35  |

<p align="center">
    <img src="https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/figure/score.png" alt="Sample" alt="Sample"  width="410" height="254">

The dueling DQN doesn't perform as well as we expected. Some speculated reasons are in the presentation.

## Timeline
Oct.15,2018 [Project Proposal](https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/Project%20Proposal.pdf)

Nov.19,2018 [Project Progress](https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/Project%20Update.pdf)

Dec.12,2018 [Presentation](https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/Presentation.pdf)

Dec.14,2018 [Final Report]
(https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/Final%20Report.pdf)

## References
1. car_racing.py is our gaming environment which we adopted from gym library.
2. Three DQN networks were implemented by us where we chose same hyperparameters as those in the three main referencing papers.
3. Three main DQN networks loss functions were modified by us.
4. The experience_replay part is referenced from diegoalejogm's github.

    
