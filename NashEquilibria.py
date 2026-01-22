"""Project: Nash Equilibria Final Project

Author		Edward Zhu
Date		1/22/2026

Description: This program simulates a 10 player round robin tournament. The two players in each
game will play a game, either prisoner's dilemma, stag and hare, battle of the sexes, or rock paper scissors. 
As the players play the game repeatedly, they will eventually pick strategies that are most optimal, or
in other words, will converge to the Nash Equilibria for each game. The graphs of the 5 games are then
outputted.

AI Usage: 	Gemini was asked: "What function to create a legend with python?"
                                "Function to group a list of values close to each other python"
Sources: 	python documentation of: python ternary, matplotlib, wikipedia
"""
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import ternary
from Player import Player
file = sys.argv[1] #takes in command-line argument of the file user input
inputArr = [] 
payoff = []
choices = []
firstLine = ""
#takes in the file, reads, and formats it
print("Reading " + str(file) + "...")
with open(file, 'r') as file:
    lines = file.readlines()
    filtered_lines = [] #contains lines with content in it, without trailing spaces/tabs
    for line in lines:
        li = line.strip()
        if li != "" and not li.startswith("#"):
            filtered_lines.append(li)
    for line in filtered_lines:
        n = int(filtered_lines[0])
        li = line.strip()
        words = li.split()
        choices.append(words[0])
        for i in range(1, len(words)-1, 2):
            try:
                onePayoff = words[i:i+2]
                int_array = list(map(int, onePayoff))
                payoff.append(int_array)
            except:
                break
    #firstLine is the name of the game
    firstLine = filtered_lines[1]
#tells the user what the program is doing
print("The payoff matrix for your game is: " + str(payoff))
print("The name of your game is: " + str(firstLine))
print("The strategies your players have are: " + str(choices[2:]))
print("Your graphs will be displayed shortly: ")
def playGame(gameName, player1, player2, xLabel, yLabel, n):
    if n == 2:
        p1 = Player(0, 2)
        p2 = Player(1, 2)
        P1y = []
        P1x = []
        P2y = []
        P2x = []
        count = []
        for i in range(500):
            P1y.append(p1.getPrefs()[0])
            P2y.append(p2.getPrefs()[0])
            p1strat = p1.getLastStrategy()
            p2strat = p2.getLastStrategy()
            p2.updateScore(p1strat, payoff)
            p2.updatePrefs()
            p1.updateScore(p2strat, payoff)
            p1.updatePrefs()
        for P1yVal in P1y:
            P1x.append(P1yVal) # generate the x value as 1-y
        for P2yVal in P2y:
            P2x.append(P2yVal) # generate the x value as 1-y

        # P2 Sizes (Dummy Data)
        sizes1 = np.histogram(P1y, bins = 20, range=(0,1))[0]
        P1sizes = [100*sizes1[i] for i in range(len(sizes1))]
        sizes2 = np.histogram(P1y, bins = 20, range=(0,1))[0]
        P2sizes = [100*sizes1[i] for i in range(len(sizes1))]
        # plot
        fig, ax = plt.subplots()
        ax.scatter([i/20 for i in range(20)],  [(20-i)/20 for i in range(20)], s=P1sizes, color='blue', label='P1', alpha=0.3)
        ax.scatter([i/21 for i in range(20)],  [(21-i)/21 for i in range(20)], s=P2sizes, color='orange', label='P2', alpha=0.4)
        # labels and title
        ax.set_xlabel(xLabel, fontsize=10)
        ax.set_ylabel(yLabel, fontsize=10)
        ax.set_title(gameName)
        # show grid
        ax.grid(True)
        # create some mock scatterpoints for the legend, otherwise
        # the circles in the legend are too big
        # this seems like not the best way to do it but i'm tired
        p1LegendX = [0.5]
        p1LegendY = [0.5]
        p1LegendSize = [50]
        p1CollectionLegend = ax.scatter(p1LegendX, p1LegendY, s=p1LegendSize, c='blue', alpha=0.3)
        p2LegendX = [0.5]
        p2LegendY = [0.5]
        p2LegendSize = [50]
        p2CollectionLegend = ax.scatter(p2LegendX, p2LegendY, s=p2LegendSize, c='orange', alpha=0.4)
        plt.legend([p1CollectionLegend, p2CollectionLegend], [player1, player2])
        # end legend code
        # show plot
        plt.show()
    if n == 3:
        p1 = Player(0, 3)
        p2 = Player(1, 3)
        P1y = []
        P1x = []
        P2y = []
        P2x = []
        count = []
        history1 = []
        history2 = []
        for i in range(100):
            P1y.append(p1.getPrefs()[0])
            P2y.append(p2.getPrefs()[0])
            p1strat = p1.getLastStrategy()
            p2strat = p2.getLastStrategy()
            p2.updateScore(p1strat, payoff)
            p2.updatePrefs()
            p1.updateScore(p2strat, payoff)
            p1.updatePrefs()
            history1.append([p1.getPrefs()[0], p1.getPrefs()[1], p1.getPrefs()[2]]) # generate the x value as 1-y
            history2.append([p1.getPrefs()[0], p1.getPrefs()[1], p1.getPrefs()[2]]) # generate the x value as 1-y
        scale = 1
        figure, tax = ternary.figure(scale=scale)
        # Draw Boundary and Gridlines
        tax.boundary(linewidth=2.0)
        tax.gridlines(color="black", multiple=5)
        tax.gridlines(color="blue", multiple=1, linewidth=0.5)
        # Set Axis labels and Title
        fontsize = 20
        tax.set_title("Rock Paper Scissors", fontsize=fontsize)
        tax.left_axis_label("Rock", fontsize=fontsize)
        tax.right_axis_label("Paper", fontsize=fontsize)
        tax.bottom_axis_label("Scissors", fontsize=fontsize)
        # Set ticks
        tax.ticks(axis="lbr", linewidth=1)
        p1Scatter = tax.scatter(history1, s = 100, c="blue", alpha=0.2, label=str(player1) + " = blue")
        p2Scatter = tax.scatter(history2, s = 100, c = "orange", alpha = 0.07, label=str(player2) + " = orange")
        #less alpha so that the blue actually shows up
        tax.clear_matplotlib_ticks()
        tax.legend()
        ternary.plt.show()
playGame(firstLine, "Player1", "Player2", choices[2], choices[3], int(choices[0]))
playGame(firstLine, "Player3", "Player4", choices[2], choices[3], int(choices[0]))
playGame(firstLine, "Player5", "Player6", choices[2], choices[3], int(choices[0]))
playGame(firstLine, "Player7", "Player8", choices[2], choices[3], int(choices[0]))
playGame(firstLine, "Player9", "Player10", choices[2], choices[3], int(choices[0]))