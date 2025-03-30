
import problems as prb
import algorithms as alg

print("demo.py is running! ")

# Run with Minimax
print("\n--- Minimax vs. Random ---")
demoGame = prb.Game(prb.DieRollGame(), alg.MinimaxAgent(), alg.RandomAgent())
demoGame.playGame()

#demoGame = prb.Game(prb.DieRollGame(), alg.RuleBasedAgent(), alg.RandomAgent())
#demoGame.playGame()