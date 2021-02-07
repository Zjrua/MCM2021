import csv
import numpy as np
import pandas as pd

csvFile = open("influence_data.csv", "r", encoding='UTF-8')
reader = csv.reader(csvFile)
g = np.zeros((5604, 5604), dtype = np.int)
g1 = np.zeros((5604, 5604), dtype = np.float)
id_list = []
def create_matrix():
    for item in reader:
        if reader.line_num == 1:
           continue
        else:
            if item[0] not in id_list:
                id_list.append(item[0])
            if item[4] not in id_list:
                id_list.append(item[4])
            g[id_list.index(item[4])][id_list.index(item[0])] = 1
#exit()
create_matrix()

for i in range(0, 5604):
    sum = 0
    for j in range(0, 5604):
        sum = sum + g[i][j]
    if sum == 0:
        #print(i)
        continue
    for j in range(0, 5604):
        g1[i][j] = g[i][j] / sum
#print(g1)
v = [1/5603 for x in range(0, 5604)]
for times in range(1, 1000):
    v = np.dot(v, g1)

print(v)

with open("output.csv", "w", newline="") as csvFile:
    reader = csv.writer(csvFile, dialect="excel")
    reader.writerow(id_list)
    reader.writerow(v)