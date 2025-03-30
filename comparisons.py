import problems as prb
import algorithms as alg

num_games = 1000

# Random vs. Random
wins_random = 0
ties_random = 0
losses_random = 0
comps = [0, 1]

for _ in range(num_games):
    game = prb.Game(prb.DieRollGame(), alg.RandomAgent(), alg.RandomAgent(), False)
    winner = game.playGame()
    if winner == 0:
        wins_random += 1
    elif winner == 1:
        losses_random += 1
    else:
        ties_random += 1
print(f"\nRandom vs. Random - Wins: {wins_random}, Losses: {losses_random}, Ties: {ties_random}")

# Rule vs. Random
agent_rule = alg.RuleBasedAgent()
wins_rule = 0
ties_rule = 0
losses_rule = 0
for _ in range(num_games):
    game = prb.Game(prb.DieRollGame(), agent_rule, alg.RandomAgent(), False)
    winner = game.playGame()
    if winner == 0:
        wins_rule += 1
    elif winner == 1:
        losses_rule += 1
    else:
        ties_rule += 1
    agent_rule.update_results(winner)  
print(f"Rule vs. Random - Wins: {wins_rule}, Losses: {losses_rule}, Ties: {ties_rule}")
print(f"Rule based agent total wins: {agent_rule.wins}, losses: {agent_rule.losses}, ties: {agent_rule.ties}") 

# Minimax vs. Random
wins_minimax = 0
ties_minimax = 0
losses_minimax = 0
for _ in range(num_games):
    game = prb.Game(prb.DieRollGame(), alg.MinimaxAgent(), alg.RandomAgent(), False)
    winner = game.playGame()
    if winner == 0:
        wins_minimax += 1
    elif winner == 1:
        losses_minimax += 1
    else:
        ties_minimax += 1
print(f"Minimax vs. Random - Wins: {wins_minimax}, Losses: {losses_minimax}, Ties: {ties_minimax}")

# Q-Learning vs. Random
wins_qlearn = 0
ties_qlearn = 0
losses_qlearn = 0
agent_qlearn = alg.QLearningAgent()  
for _ in range(num_games):
    game = prb.Game(prb.DieRollGame(), agent_qlearn, alg.RandomAgent(), False)
    winner = game.playGame()
    if winner == 0:
        wins_qlearn += 1
    elif winner == 1:
        losses_qlearn += 1
    else:
        ties_qlearn += 1
print(f"Q-Learning vs. Random - Wins: {wins_qlearn}, Losses: {losses_qlearn}, Ties: {ties_qlearn}")