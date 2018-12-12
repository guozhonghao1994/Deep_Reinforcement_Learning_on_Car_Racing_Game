# plot curve
import numpy as np
import matplotlib.pyplot as plt

# read data
loss_list = ['loss_DQN.npy','loss_DDQN.npy','loss_dueling.npy']
q_list = ['q_DQN.npy','q_DDQN.npy','q_dueling.npy']
reward_list = ['reward_DQN.npy','reward_DDQN.npy','reward_dueling.npy']

try:
	loss_DQN = np.load(loss_list[0])
	loss_DDQN = np.load(loss_list[1])
	loss_dueling = np.load(loss_list[2])

	q_DQN = np.load(q_list[0])
	q_DDQN = np.load(q_list[1])
	q_dueling = np.load(q_list[2])

	reward_DQN = np.load(reward_list[0])
	reward_DDQN = np.load(reward_list[1])
	reward_dueling = np.load(reward_list[2])
except:
	print("load data failed!")

# moving average
def moving_average(a, n=3) :
	ret = np.cumsum(a, dtype=float)
	ret[n:] = ret[n:] - ret[:-n]
	return ret[n - 1:] / n

# plot single figure
def plot_single(data,ylabel,title):
	plt.figure()
	plt.plot(data)
	plt.xlabel('episode')
	plt.ylabel(ylabel)
	plt.title(title)

# plot comparison
def comparison(DQN,DDQN,dueling,ylabel,title):
	plt.figure()
	plt.plot(range(len(DQN)),DQN,range(len(DDQN)),DDQN,range(len(dueling)),dueling)
	plt.xlabel('episode')
	plt.ylabel(ylabel)
	plt.title(title)
	plt.legend(['DQN','DDQN','dueling'])

# set nan to 0
q_dueling[np.isnan(q_dueling)] = 0
loss_dueling[np.isnan(loss_dueling)] = 0
q_DQN[np.isnan(q_DQN)] = 0
loss_DQN[np.isnan(loss_DQN)] = 0
q_DDQN[np.isnan(q_DDQN)] = 0
loss_DDQN[np.isnan(loss_DDQN)] = 0

# moving average
q_DQN = moving_average(q_DQN[500:],100)
q_DDQN = moving_average(q_DDQN[500:],100)
q_dueling = moving_average(q_dueling[500:],100)

reward_DQN = moving_average(reward_DQN[:3550],40)
reward_DDQN =moving_average(reward_DDQN[:3550],40)
reward_dueling = moving_average(reward_dueling[:3550],40)

loss_DQN = moving_average(loss_DQN[500:],50)
loss_DDQN = moving_average(loss_DDQN[500:],50)
loss_dueling = moving_average(loss_dueling[500:],50)

# plot single graph
plot_single(q_dueling,'avg Q','average Q dueling')
plot_single(reward_dueling,'avg reward','average reward dueling')
plot_single(loss_dueling,'loss','loss dueling')

plot_single(q_DQN,'avg Q','average Q DQN')
plot_single(reward_DQN,'avg reward','average reward DQN')
plot_single(loss_DQN,'loss','loss DQN')

plot_single(q_DDQN,'avg Q','average Q DDQN')
plot_single(reward_DDQN,'avg reward','average reward DDQN')
plot_single(loss_DDQN,'loss','loss DDQN')

# comparison
comparison(q_DQN,q_DDQN,q_dueling,'avg Q','average Q comparison between DQN,DDQN and dueling DQN')
comparison(reward_DQN,reward_DDQN,reward_dueling,'avg reward','reward comparison between DQN,DDQN and dueling DQN')
comparison(loss_DQN,loss_DDQN,loss_dueling,'loss','loss comparison between DQN,DDQN and dueling DQN')

plt.show()
