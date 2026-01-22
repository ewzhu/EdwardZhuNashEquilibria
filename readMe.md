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
Prisoners Dilemma:
User: python NashEquilibria.py pd.txt
Computer: 
Reading pd.txt...
The payoff matrix for your game is: [[-1, -1], [-12, 0], [0, -12], [-8, -8]]
The name of your game is: Prisoner's Dilemma Game
The strategies your players have are: ['quiet', 'confess']
Your graphs will be displayed shortly:
<img width="923" height="713" alt="image" src="https://github.com/user-attachments/assets/9f4c277d-7511-44f8-b976-8e52d78161bb" />
<img width="965" height="811" alt="image" src="https://github.com/user-attachments/assets/b51a6688-4ccf-4759-9bd8-c846ee51bca6" />
<img width="960" height="803" alt="image" src="https://github.com/user-attachments/assets/082d7f1b-2820-46ec-acd9-ec84e8f7cbeb" />
<img width="948" height="797" alt="image" src="https://github.com/user-attachments/assets/14bca020-3f2f-4dfc-af37-46b64b639da9" />
<img width="947" height="805" alt="image" src="https://github.com/user-attachments/assets/b24b5734-2136-4d1b-ad35-d346ef83c6ac" />



User: python NashEquilibria.py sh.txt
Computer:
Reading sh.txt...
The payoff matrix for your game is: [[3, 3], [0, 2], [2, 0], [1, 1]]
The name of your game is: Stag and Hare Game
The strategies your players have are: ['quiet', 'confess']
Your graphs will be displayed shortly:

User: python NashEquilibria.py battlesexes.txt
Computer: 
Reading battlesexes.txt...
The payoff matrix for your game is: [[3, 2], [0, 0], [0, 0], [2, 3]]
The name of your game is: Battle of the Sexes
The strategies your players have are: ['quiet', 'confess']
Your graphs will be displayed shortly:

User: python NashEquilibria.py rps.txt
Computer:
Reading rps.txt...
The payoff matrix for your game is: [[0, 0], [-1, 1], [1, -1], [1, -1], [0, 0], [-1, 1], [-1, 1], [1, -1], [0, 0]]
The name of your game is: Rock Paper Scissors
The strategies your players have are: ['rock', 'paper', 'scissors']
Your graphs will be displayed shortly:
<img width="949" height="763" alt="image" src="https://github.com/user-attachments/assets/e05828bd-7125-4c13-aeab-9e7378086e59" />
<img width="953" height="819" alt="image" src="https://github.com/user-attachments/assets/0b474ae0-bfd2-4415-93a9-71f6c94e7f8f" />
<img width="943" height="818" alt="image" src="https://github.com/user-attachments/assets/cfb07057-7360-4fa7-a3d4-30ba8fbfc43c" />
<img width="956" height="753" alt="image" src="https://github.com/user-attachments/assets/21db1803-2a71-48f9-9197-b3334567f996" />
<img width="965" height="822" alt="image" src="https://github.com/user-attachments/assets/84a69409-9e36-49fe-8cbd-523793f53e79" />






Other Important Information: This file was written on Python version 3.12.5.
The Python libraries used are random, math,sys, ternary, numpy and matplotlib.
