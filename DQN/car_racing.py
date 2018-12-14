# BU EC500 Deep Learning Project
# Reinforcemant Learning Playing Car Racing Game
# Minghe Ren, Yuxuan Jiang, Zhonghao Guo, Jiahao Zhang
# {sawyermh, jwx0728, gzh1994,jiahaozh }@bu.edu

from dqn.agent import CarRacingDQN
import os
import sys
import re
import gym
import tensorflow as tf
import _thread


# Training model configuration, you can tweak the parameters you like
model_config = dict(
    min_epsilon=0.1,
    max_negative_rewards=12,
    min_experience_size=int(1e4),
    num_frame_stack=3,
    frame_skip=3,
    train_freq=4,
    batchsize=64,
    epsilon_decay_steps=int(1e5),
    network_update_freq=int(1e3),
    experience_capacity=int(4e4),
    gamma=0.95
    )


# A function to save model
def save_model():
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    path = os.path.join(model_path, "m.model")
    saver.save(sess, path, dqn_agent.global_counter)
    print("model has saved to %s -- %d" % (path, dqn_agent.global_counter))


# A function to play one episode 
def play_episode():
    reward, frames , q_values, loss = dqn_agent.play_episode()
    print("episode: %d, reward: %f, length: %d, total steps: %d, q_values: %f, loss: %f"%
        (dqn_agent.episode_counter, reward, frames, dqn_agent.global_counter, q_values, loss))
    save_condition = (dqn_agent.episode_counter % save_freq_episodes == 0 and model_path is not None and dqn_agent.do_training)
    if save_condition:
        save_model()
    return reward,q_values,loss


def thread(list):
    input("Press enter to stop\n")
    list.append("OK")

# A main function to keeping play episodes until the condition meets
def main():
    list = []
    reward_list = []
    q_list = []
    loss_list = []
    _thread.start_new_thread(thread, (list,))
    while True:
        if list:
            break
        if dqn_agent.do_training and dqn_agent.episode_counter > train_episodes:
            break
        reward, q_values,loss =  play_episode()
        reward_list.append(reward)
        q_list.append(q_values)
        loss_list.append(loss)

    np.save("reward_DQN", reward_list)
    np.save("q_DQN",q_list)
    np.save("loss_DQN",loss_list)
    print("done")


# Setting game environment
env_name = "CarRacing-v0"
env = gym.make(env_name)


# Train without loading pretrained model
load_model = False
model_path = "./tmp/checkpoint01"
train_episodes = 4000
save_freq_episodes = 200

# Train with loading existing model
# load_model = True
# model_path = "./data/checkpoint02"
# train_episodes = 0

# Start Tensorflow session
dqn_agent = CarRacingDQN(env=env, **model_config)
dqn_agent.build_graph()
sess = tf.InteractiveSession()
dqn_agent.session = sess
saver = tf.train.Saver(tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES), 'parameters',max_to_keep=50)


# Load model
if not load_model:
    if model_path is not None:
        assert not os.path.exists(model_path), "mdoel already exists please set load_model true or delete the saved model"
    tf.global_variables_initializer().run()
else:
    print("load the newest model from %s" % model_path)
    model = tf.train.get_checkpoint_state(model_path)
    assert model, "model path not found" 
    global_counter = int(re.findall("-(\d+)$", model.model_model_path)[0])
    saver.restore(sess, model.model_model_path)
    dqn_agent.global_counter = global_counter

# Start training
if train_episodes > 0:
    sys.stdout.flush()
    main()
    save_model()
    print("training finished")

# Start playing
sys.stdout.flush()
dqn_agent.max_neg_rewards = 100
dqn_agent.do_training = False
sys.stdout.flush()
main()
