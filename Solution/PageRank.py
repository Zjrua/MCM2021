import csv
import numpy as np

csvFile = open("E:\\StudyAndWork\\MCM2021\\Problem\\2021_ICM_Problem_D_Data\\influence_data.csv", "r", encoding='UTF-8')
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
            g[id_list.index(item[0])][id_list.index(item[4])] = 1

create_matrix()
#print(g)

for i in range(0, 5604):
    sum = 0
    for j in range(0, 5604):
        sum = sum + g[i][j]
    if sum == 0:
        continue
    for j in range(0, 5604):
        g1[i][j] = g[i][j] / sum
#print(g1)

v = np.zeros((0, 5604), dtype = np.float)
for i in range(0, 5604):
    v[i] = 1 / 5604
print(v)
for times in range(1, 1000):
    v = np.dot(v, g1)
print(v)