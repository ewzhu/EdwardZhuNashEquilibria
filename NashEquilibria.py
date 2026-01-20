import sys
import math
import matplotlib.pyplot as plt
from Player import Player
file = sys.argv[1]
inputArr = [] 

payoff = []
choices = []
print("Reading " + str(file))
with open(file, 'r') as file:
    lines = file.readlines()
    filtered_lines = []
    for line in lines:
        li = line.strip()
        if li != "" and not li.startswith("#"):
            filtered_lines.append(li)
    for line in filtered_lines:
        n = int(filtered_lines[0])
        li = line.strip()
        words = li.split()
        choices.append(words[0])
        for i in range(1, len(words)-1, n):
            try:
                onePayoff = words[i:i+n]
                int_array = list(map(int, onePayoff))
                payoff.append(int_array)
            except:
                break
print(payoff)
p1 = Player(0, 2)
p2 = Player(1, 2)
P1y = []
P1x = []
P2y = []
P2x = []
for i in range(300):
    P1y.append(p1.getPrefs()[0])
    P2y.append(p2.getPrefs()[1])
    p1strat = p1.getStrategy()
    p2strat = p2.getStrategy()
    p2.updateScore(p1strat, payoff)
    p2.updatePrefs()
    p1.updateScore(p2strat, payoff)
    p1.updatePrefs()
for P1yVal in P1y:
    P1x.append(1-P1yVal) # generate the x value as 1-y

# P1 Sizes (Dummy Data)
P1sizes = [-200*math.log(1 - x) for x in P1y]
P2sizes = [-200*math.log(1 - x) for x in P2y]
# P2 Preferences (Dummy Data)

for P2yVal in P2y:
    P2x.append(1-P2yVal) # generate the x value as 1-y

# P2 Sizes (Dummy Data)


# plot
fig, ax = plt.subplots()
ax.scatter(P1x, P1y, s=P1sizes, c='blue', label='P1', alpha=0.3)
ax.scatter(P2x, P2y, s=P2sizes, c='orange', label='P2', alpha=0.4)

# labels and title
ax.set_xlabel('quiet', fontsize=10)
ax.set_ylabel('confess', fontsize=10)
ax.set_title('Prisoner\'s Dilemma')

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

plt.legend([p1CollectionLegend, p2CollectionLegend], ['P1', 'P2'])
# end legend code

# show plot
plt.show()


