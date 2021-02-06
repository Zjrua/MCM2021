import csv
import numpy as np

csvFile = open("E:\\StudyAndWork\\MCM2021\\Problem\\2021_ICM_Problem_D_Data\\influence_data.csv", "r", encoding='UTF-8')
reader = csv.reader(csvFile)
g = np.zeros((5604, 5604), dtype = np.bool)
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
            g[id_list.index(item[0])][id_list.index(item[4])] = True

create_matrix()
