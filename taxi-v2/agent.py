import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6, nS=500, epsilon=0.9, alpha=0.16, gamma=1):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        - nS: number of possible states. There are 500 possible states.
        - epsilon: How much are we leeting the taxi experiment and learn new things.
        - alpha: This is the step-size parameter for the update step.
        - gamma: This is the discount rate. It must be a value between 0 and 1, inclusive (default value: 1).
        """
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.ns = nS
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.i_episode = 1
        self.policy_s = None


    def update_Q(self, Qsa, Qsa_next, reward, alpha, gamma):
        """ updates the action-value function estimate using the most recent time step """
        return Qsa + (alpha * (reward + (gamma * Qsa_next) - Qsa))

    def epsilon_greedy_probs(self, Q_s, i_episode, eps=None):
        """ obtains the action probabilities corresponding to epsilon-greedy policy """
        self.epsilon = 1.0 / self.i_episode
        if eps is not None:
            self.epsilon = eps
        policy_s = np.ones(self.nA) * self.epsilon / self.nA
        policy_s[np.argmax(Q_s)] = 1 - self.epsilon + (self.epsilon / self.nA)
        return policy_s

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        # Set new policy
        self.policy_s = self.epsilon_greedy_probs(self.Q[state], self.i_episode, 0.0005)
        # Increment episode number to calc epsilon
        self.i_episode += 1
        # Return action choice
        return np.random.choice(np.arange(self.nA), p=self.policy_s)


    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        
        self.Q[state][action] = self.update_Q(self.Q[state][action], np.dot(self.Q[next_state], self.policy_s), \
                                                  reward, self.alpha, self.gamma) 
