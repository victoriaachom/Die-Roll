import random

class RandomAgent:
    def __str__(self):
        return "Random Agent"

    def getMove(self, problem):
        return None  

class RuleBasedAgent:
    def __str__(self):
        return "Cheating Agent"

    def getMove(self, problem):
        problem.player_rolls[problem.current_player] = 6
        return None

class MinimaxAgent:
    def __str__(self):
        return "Predicting Agent"

    def getMove(self, prob):
        if prob.rolls_made == 1:
            # Simulate Minimax prediction (simplified for demonstration)
            predicted_roll = random.randint(1, 6) + 1
            if predicted_roll > 6:
                predicted_roll = 6
            print(f"Minimax Agent predicted roll: {predicted_roll}")
            prob.player_rolls[1] = predicted_roll
        return None

class QLearningAgent:
    def __init__(self, learn_rate=0.1, disc_factor=0.9, exp_rate=1.0):
        self.learn_rate = learn_rate
        self.disc_factor = disc_factor
        self.exp_rate = exp_rate
        self.q_table = {}

    def __str__(self):
        return "Q-Learning Agent"

    def getNextMove(self, probm):
        state = str(prob.rolls_made)
        if state not in self.q_table:
            self.q_table[state] = [0] * 6

        if random.random() < self.exp_rate:
            roll = random.randint(1, 6)
        else:
            roll = self.q_table[state].index(max(self.q_table[state])) + 1

        prob.player_rolls[prob.current_player] = roll

        print(f"Q-Learning Agent Q-values: {self.q_table[state]}, Rolled: {roll}")
        prob.player_rolls[prob.curr_player] = roll

        if prob.rolls_made == 1:
            reward = prob.getWinner()
            self.q_table[state][roll - 1] = (1 - self.learn_rate) * self.q_table[state][roll - 1] + self.learn_rate * (reward + self.disc_factor * max(self.q_table[str(prob.rolls_made)]))

        self.exp_rate *= 0.995 

        return None