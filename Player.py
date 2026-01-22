
# SahuPlayer.py
# Author sahwho
'''
    Represent a Player for Mod/Sim Fall 2024 Project 1 (MBHS)
    A Player has an id (like "P1"), as well as preferences for 2 strategies (which sum to 1.0).
    and keeps track of how many games they've played, plus their total score and average score.
    If you use this class, feel free to rename it Player.py

    Inspiration drawn from the work done by Dr. Andrew Davison (PSU)

    sample usage: p1 = SahuPlayer("P1")
'''

import random

class Player:
    def __init__(self, id, n):
        self.id = int(id)
        self.prefs = [] # strategy1, strategy2 #edit this to take in 3 strats
        self.n = n
        for i in range(n):
            self.prefs.append(1.0/n)
        self.currentGameScore = 0
        self.numGamesPlayed = 0.0
        self.totalScore = 0
        self.averageScore = 0
        self.lastStrategy = 0
    def getId(self):
        return self.id

    def getPrefs(self):
        return self.prefs

    # no getters needed for currentGameScore, numGamesPlayed, totalScore, or averageScore,
    # since those are used internally within these methods
    # todo: based on the preferences, pseduorandomly select strategy1 or strategy2
    def getStrategy(self):
        strategyIndices = range(0, len(self.prefs))
        return int(random.choices(strategyIndices, weights = self.prefs, k =1)[0])
    def getLastStrategy(self):
        return self.lastStrategy
    # todo: update totalScore, numGamesPlayed, and averageScore
    # this method assumes that a game has been played
    def updateScore(self, opponentStrat, arr):
        self.lastStrategy = self.getStrategy()
        score = arr[self.lastStrategy*self.n+opponentStrat][int(self.id)]
        self.currentGameScore = score
        self.numGamesPlayed +=1
        self.totalScore += self.currentGameScore
        self.averageScore = self.totalScore/self.numGamesPlayed
    # todo: use a formula to update the current Player's preferences
    #Better updateprefs formula cuz original one went negative
    '''
    def updatePrefs(self):
        factor = 1.05  
        for i in range(len(self.prefs)):
            if i == self.getStrategy():
                self.prefs[i] *= factor
            else:
                self.prefs[i] /= factor
    # normalize so sum = 1
        total = sum(self.prefs)
        self.prefs = [p / total for p in self.prefs]
        '''
    def updatePrefs(self):
        strat = self.lastStrategy
        for i in range(len(self.prefs)):
            if i != strat:#updates rest of the preferences
                self.prefs[i] = self.prefs[i] - (self.currentGameScore - self.averageScore)/(100*(len(self.prefs)-1))
            else:
                self.prefs[i] = self.prefs[i] + (self.currentGameScore - self.averageScore)/100
        for i in range(len(self.prefs)):
            if self.prefs[i] < 0:
                self.prefs[i] = 0
            elif self.prefs[i] >1:
                self.prefs[i] = 1
        total = sum(self.prefs)
        for i in range(len(self.prefs)):
            self.prefs[i] = self.prefs[i] / total
    # format the object for printing: P1: <0.5, 0.5>

    def __str__(self):
        return str(self.id) + ': <' + str(self.prefs[0]) + ',' + str(self.prefs[1]) + '>'