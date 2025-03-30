import problems as prb
import algorithms as alg

comps = [0, 1]

if 0 in comps:
    wins_random = 0
    ties_random = 0
    losses_random = 0
    for _ in range(100):
        game = prb.Game(prb.DieRollGame(), alg.RandomAgent(), alg.RandomAgent(), False)
        winner = game.playGame()
        if winner == 0:
            wins_random += 1
        elif winner == 1:
            losses_random += 1
        else:
            ties_random += 1
    print(f"Random vs. Random - Wins: {wins_random}, Losses: {losses_random}, Ties: {ties_random}")

if 1 in comps:
    agent = alg.RuleBasedAgent()
    wins_rule = 0
    ties_rule = 0
    losses_rule = 0
    for _ in range(100):
        game = prb.Game(prb.DieRollGame(), agent, alg.RandomAgent(), False)
        winner = game.playGame()
        if winner == 0:
            wins_rule += 1
        elif winner == 1:
            losses_rule += 1
        else:
            ties_rule += 1
        agent.update_results(winner)
    print(f"Rule vs. Random - Wins: {wins_rule}, Losses: {losses_rule}, Ties: {ties_rule}")
    print(f"Rule based agent total wins: {agent.wins}, losses: {agent.losses}, ties: {agent.ties}")