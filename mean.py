import csv

with open("height-weight.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

#sorting
fileData.pop(0)
newData = []

for i in range(len(fileData)):
    number = fileData[i][1]
    newData.append(float(number))

#mean
n = len(newData)
total = 0

for i in newData:
    total += i
mean = total/n

print("Mean is " + str(mean))


