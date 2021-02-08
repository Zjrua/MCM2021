import matplotlib as plt
import numpy as np
import pandas as pd
import csv
from sklearn.decomposition import PCA
import math

id_list = []
vec_aritst = []
Index2Ndoe = {}
Node2Index = {}

def Generate_G():
    G = {}
    with open("influence_data.csv", "r", encoding="UTF-8") as csvFile:
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num == 1:
                continue
            else:
                if item[0] not in id_list:
                    id_list.append(item[0])
                
                if item[4] not in id_list:
                    id_list.append(item[4])
                
                if item[0] not in G:
                    G[item[0]] = {item[4] : 1}
                    #print(G[item[0]])
                else:
                    G[item[0]][item[4]] = 1
                
                if item[4] not in G:
                    G[item[4]] = {item[0] : 0}
                    #print(G[item[0]])
                else:
                    G[item[4]][item[0]] = 0
    #print(len(G))
    return G

def init_artist_data():
     with open("data_by_artist.csv", "r", encoding="UTF-8") as dba:
        artist_reader = csv.reader(dba)
        for line in artist_reader:
            if artist_reader.line_num == 1:
                continue
            else:
                vec_aritst.append(line[2:-1])
                if line[1] not in id_list:
                    id_list.append(line[1])
                Index2Ndoe[id_list.index(line[1])] = line[1]
                Node2Index[line[1]] = id_list.index(line[1])
                n = len(vec_aritst) - 1
                vec_aritst[n] = list(map(float, vec_aritst[n]))
                # print(vec_aritst[n])

def similiarity(a, b):
    sum1 = 0.0
    for i in a:
        sum1 = sum1 + float(i) ** 2
    sum2 = 0.0
    for i in b:
        sum2 = sum2 + float(i) ** 2
    dott = np.dot(a, b)
    result = dott / (math.sqrt(sum1 * sum2))
    # print(dott, sum1, sum2, result)
    return result

if __name__ == '__main__':
    G = Generate_G()
    init_artist_data()
    n = len(vec_aritst) + 1
    pca = PCA(n_components=6)
    vec_aritst1 = pca.fit_transform(vec_aritst)
    
    sim = {}
    for a in G:
        for b in G[a]:
            if a not in sim:
                if (a not in Node2Index) or (b not in Node2Index):
                    continue
                a1 = vec_aritst[(Node2Index[a])]
                b1 = vec_aritst[(Node2Index[b])]
                sim[a] = {b:similiarity(a1, b1)}
            else :
                sim[a][b] = similiarity(a1, b1)
    result = []
    for a in sim:
        for b in sim[a]:
            result.append([a, b, sim[a][b]])

    with open("output_data2.csv", "w", encoding="UTF-8") as output:
        writer = csv.writer(output)
        for line in result:
            writer.writerow(line)