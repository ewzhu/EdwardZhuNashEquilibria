Title: ModSim Final Project - NashEquilibrium

Objective: This project is meant to simulate Nash Equilibria over the course of many games
and, importantly, display the results using graphs.

Project Description: This program simulates a 10 player round robin tournament of games with payoff matrices.
The two players in each game will play a game, either prisoner's dilemma, stag and hare, battle of the sexes, or rock paper scissors. 
As the players play the game repeatedly, they will eventually pick strategies that are most optimal, or
in other words, will converge to the Nash Equilibria for each game. The graphs of the 5 games are then
outputted.


File Descriptions: battlesexes.txt, pd.txt, rps.txt, and sh.txt are the text files that include payoff matrices
for battle of the sexes, prisoner's dilemma, rock paper scissors, and stag and hare respectively. 
Player.py includes methods that help simulate a player playing these games in real life, including updating preferences.
NashEquilibria.py is where the simulations and games occur.

Running code: 
To run the code, simply navigate to NashEquilibria.py and then type, in the commandline argument,
python NashEquilibria.py [text file name]

Example outputs: 
User: python NashEquilibria.py pd.txt
Computer: 
Reading pd.txt...
The payoff matrix for your game is: [[-1, -1], [-12, 0], [0, -12], [-8, -8]]
The name of your game is: Prisoner's Dilemma Game
The strategies your players have are: ['quiet', 'confess']
Your graphs will be displayed shortly:


Other Important Information: This file was written on Python version 3.12.5.
The Python libraries used are random, math,sys, ternary, numpy and matplotlib.