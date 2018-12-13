# Deep_Reinforcement_Learning_on_Car_Racing_Game
## Task
Our project explores the algorithms of reinforcement learning (RL) used in game playing. We study several RL algorithms and implement them in a car racing game. The RL methods include, but not limited to, DQN, Double DQN, and Dueling DQN. After the RL methods been implemented, we make comparison between these results and analyze the characteristics of each method.

## Related Work
[Playing Atari with Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)

[Human-level control through deep reinforcement learning](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf)

[Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/pdf/1509.06461.pdf)

[Dueling Network Architectures for Deep Reinforcement Learning](http://proceedings.mlr.press/v48/wangf16.pdf)

## Game Environment
[Car Racing-v0](https://gym.openai.com/envs/CarRacing-v0/)

![](https://media.giphy.com/media/3og0IEKu84Ros9izyU/giphy.gif)

## Algorithm
We try DQN, Double DQN(DDQN) and dueling DQN. Please refer to the [presentation](https://github.com/guozhonghao1994/Deep_Reinforcement_Learning_on_Car_Racing_Game/blob/master/Presentation.pdf) for detailed algorithm explanation. Also, you should have some basic knowledge on [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning) and [Q-learning](https://en.wikipedia.org/wiki/Q-learning). 

## Installation
1. `pip install -r requirements.txt`

    necessary module: `tensorflow`, `pygame`, `gym`, `Box2D`, `VC++ 14.0` ...

2. In DQN/DDQN/dueling DQN folder, run `python car_runner_main.py`

3. If you'd like to utilize the trained model, `load_checkpoint = True` in *python car_runner_main.py*

4. On CPU, it takes about 8 hours to get a well-trained model.

## Result
### Training Result


### Test Result

<p align="center">
    <img src="https://img-blog.csdn.net/20180904102458446?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xvdmVjaHJpczAw/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="Sample"  width="250" height="140">
    <p align="left">
        <em>图片示例2</em>
    </p>
</p>
