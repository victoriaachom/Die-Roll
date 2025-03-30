import random

class DieRollGame:
    def __init__(self):
        self.player_rolls = [0, 0]
        self.rolls_made = 0
        self.curr_player = 0

    def getProperMoves(self):
        return []

    def startMove(self, player):
        if self.player_rolls[player] == 0:
            self.player_rolls[player] = random.randint(1, 6)
        self.rolls_made += 1
        self.curr_player = 1

    def isTerminal(self):
        return self.rolls_made == 2

    def getWinner(self):
        if not self.isTerminal():
            return -1
        if self.player_rolls[0] > self.player_rolls[1]:
            return 0
        elif self.player_rolls[1] > self.player_rolls[0]:
            return 1
        else:
            return -1

    def currState(self, ms=1000):
        print(f"Player 1 rolled: {self.player_rolls[0]}")
        print(f"Player 2 rolled: {self.player_rolls[1]}")
        if self.isTerminal():
            winner = self.getWinner()
            if winner == 0:
                print("Player 1 wins!")
            elif winner == 1:
                print("Player 2 wins!")
            else:
                print("It's a draw!")

class Game:
    def __init__(self, prob, pZero, pOne, isTrue=True):
        self.prob = prob
        self.players = [pZero, pOne]
        self.isTrue = isTrue
        if self.isTrue:
            self.prob.currState()

    def playGame(self):
        pCur = 0
        while self.prob.isTerminal() == False:
            self.prob.startMove(pCur)
            if self.isTrue:
                self.prob.currState()
            pCur = 1

        results = self.prob.getWinner()
        if results == -1:
            winner = "DRAW"
        else:
            winner = self.players[results]
        print(f"The Winner is {winner} ({results})!")
        if self.isTrue:
            self.prob.currState(4000)
        return results