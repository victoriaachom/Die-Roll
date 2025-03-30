
import problems as prb
import algorithms as alg

print("demo.py is running! ")

# Run with Minimax
print("\n Minimax vs. Random ")
demoGame = prb.Game(prb.DieRollGame(), alg.MinimaxAgent(), alg.RandomAgent())
demoGame.playGame()

# Run with Q-Learning
print("\nQ-Learning vs. Random ")
demoGame = prb.Game(prb.DieRollGame(), alg.QLearningAgent(), alg.RandomAgent())
demoGame.playGame()
