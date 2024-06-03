import gymnasium as gym
from gymnasium import spaces
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

class MazeEnv(gym.Env):
    metadata = {'render_modes': ['human']}

    def __init__(self):
        super(MazeEnv, self).__init__()
        self.grid_size = 10
        self.action_space = spaces.Discrete(4)  # 4 mögliche Aktionen: 0: hoch, 1: rechts, 2: runter, 3: links
        self.observation_space = spaces.Box(low=0, high=3, shape=(self.grid_size, self.grid_size), dtype=np.int32)
        self.maze = None
        self.agent_pos = None
        self.goal_pos = None
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.maze = np.zeros((self.grid_size, self.grid_size), dtype=np.int32)
        self.agent_pos = [0, 0]
        self.goal_pos = self._get_random_position()  # Zuerst das Ziel initialisieren
        self._generate_maze()  # Dann das Labyrinth erstellen
        return self._get_observation(), {}

    def _generate_maze(self):
        np.random.seed(2)  # For reproducibility
        self.maze = np.random.choice([0, 1], size=(self.grid_size, self.grid_size), p=[0.7, 0.3])
        self.maze[0, 0] = 0  # Start position
        self.maze[self.goal_pos[0], self.goal_pos[1]] = 3  # Zielposition

    def _get_observation(self):
        obs = np.copy(self.maze)
        obs[self.agent_pos[0], self.agent_pos[1]] = 2  # Mark agent's position
        return obs

    def _get_random_position(self):
        position = [np.random.randint(self.grid_size), np.random.randint(self.grid_size)]
        while self.maze[position[0], position[1]] == 1:  # Wand
            position = [np.random.randint(self.grid_size), np.random.randint(self.grid_size)]
        return position

    def step(self, action):
        new_pos = list(self.agent_pos)
        if action == 0 and self.agent_pos[0] > 0:  # hoch
            new_pos[0] -= 1
        elif action == 1 and self.agent_pos[1] < self.grid_size - 1:  # rechts
            new_pos[1] += 1
        elif action == 2 and self.agent_pos[0] < self.grid_size - 1:  # runter
            new_pos[0] += 1
        elif action == 3 and self.agent_pos[1] > 0:  # links
            new_pos[1] -= 1

        if self.maze[new_pos[0], new_pos[1]] == 1:  # Hit a wall
            return self._get_observation(), -1, False, False, {}

        self.agent_pos = new_pos

        if self.agent_pos == self.goal_pos:
            return self._get_observation(), 10, True, False, {}  # Reached goal

        return self._get_observation(), -0.1, False, False, {}

    def render(self, mode='human'):
        obs = self._get_observation()
        print('___')
        for row in obs:
            row_str = ''
            for item in row:
                if item == 0:
                    row_str += 'O'
                elif item == 1:
                    row_str += 'X'  # Wand
                elif item == 2:
                    row_str += 'A'  # Agent
                elif item == 3:
                    row_str += 'G'  # Ziel
            print(row_str)
        print()

# Registrierung der Umgebung
from gymnasium.envs.registration import register

register(
    id='Maze-v0',
    entry_point='__main__:MazeEnv',
)

def train_model():
    # Initialisieren der Maze-Umgebung
    env = gym.make('Maze-v0')

    # Überprüfen der Umgebung
    check_env(env, warn=True)

    # Erstellen des PPO-Modells
    model = PPO("MlpPolicy", env, verbose=1)

    # Trainieren des Modells
    model.learn(total_timesteps=10000)

    # Speichern des Modells
    model.save("ppo_maze")

def test_model():
    # Initialisieren der Maze-Umgebung
    env = gym.make('Maze-v0')

    # Laden des trainierten Modells
    model = PPO.load("ppo_maze")

    # Testen des trainierten Modells
    obs, _ = env.reset()
    for _ in range(100):
        action, _states = model.predict(obs)
        obs, rewards, done, truncated, info = env.step(action)
        env.render()
        if done or truncated:
            break

    env.close()

if __name__ == "__main__":
    # Trainieren des Modells
    train_model()
    # Testen des Modells
    test_model()
