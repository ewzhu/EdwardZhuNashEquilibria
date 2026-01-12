x = input("Input a file for me to read: ")
inputArr = [] 
for line in open(x):
	li = line.strip() # 
	if li != "" and not li.startswith("#"):
        inputArr.append([li.split()])
