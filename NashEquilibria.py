import sys
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
            print(filtered_lines)
    print(filtered_lines)
    for line in filtered_lines:
        n = int(filtered_lines[0])
        li = line.strip()
        print(li)
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
print(choices)
