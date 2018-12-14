
class ExperienceReplay:
    """
    This is the Experience Replay Cache.
    Store (s,a,r,s')
    Frame_window is the location of wanted state in the cache
    """

    def __init__(self,
            num_frame_stack=4,
            capacity=int(1e5),
            pic_size=(96, 96)
    ):
        self.num_frame_stack = num_frame_stack
        self.capacity = capacity
        self.pic_size = pic_size
        self.counter = 0
        self.frame_window = None
        self.init_caches()
        self.expecting_new_episode = True


    def init_caches(self):
	# init cache capacity

        self.rewards = np.zeros(self.capacity, dtype="float32")
        self.prev_states = -np.ones((self.capacity, self.num_frame_stack),
            dtype="int32")
        self.next_states = -np.ones((self.capacity, self.num_frame_stack),
            dtype="int32")
        self.is_done = -np.ones(self.capacity, "int32")
        self.actions = -np.ones(self.capacity, dtype="int32")

        self.max_frame_cache = self.capacity + 2 * self.num_frame_stack + 1
        self.frames_cache = -np.ones((self.max_frame_cache,) + self.pic_size, dtype="float32")


    def add_experience(self, frame, action, done, reward):
    #store (s,a,r,s') into frame_cache

        assert self.frame_window is not None, "start episode first"
        self.counter += 1
        frame_idx = self.counter % self.max_frame_cache
        exp_idx = (self.counter - 1) % self.capacity

        self.prev_states[exp_idx] = self.frame_window
        self.frame_window = np.append(self.frame_window[1:], frame_idx)
        self.next_states[exp_idx] = self.frame_window
        self.actions[exp_idx] = action
        self.is_done[exp_idx] = done
        self.frames_cache[frame_idx] = frame
        self.rewards[exp_idx] = reward
        if done:
            self.expecting_new_episode = True

    def start_new_episode(self, frame):

        assert self.expecting_new_episode, "previous episode didn't end yet"
        frame_idx = self.counter % self.max_frame_cache
        self.frame_window = np.repeat(frame_idx, self.num_frame_stack)
        self.frames_cache[frame_idx] = frame
        self.expecting_new_episode = False

    def sample_mini_batch(self, n):
    	# random sampling from ExperienceReply cache

        count = min(self.capacity, self.counter)
        batchidx = np.random.randint(count, size=n)

        prev_frames = self.frames_cache[self.prev_states[batchidx]]
        next_frames = self.frames_cache[self.next_states[batchidx]]

        return {
            "reward": self.rewards[batchidx],
            "prev_state": prev_frames,
            "next_state": next_frames,
            "actions": self.actions[batchidx],
            "done_mask": self.is_done[batchidx]
        }

    def current_state(self):
    #return current state
        assert self.frame_window is not None, "do something first"
        return self.frames_cache[self.frame_window]


