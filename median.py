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
n = len(newData)
newData.sort()

#median
if n%2 == 0:
    median1 = float(newData[n//2])

    median2 = float(newData[n//2 -1])

    median = (median1+median2)/2
else:
    median = newData[n//2]
print("Median is " +str(median))

