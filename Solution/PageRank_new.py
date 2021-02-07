import numpy as np
import pandas as pd
import csv

def PageRank(M, alpha, root):
    result = []
    n = len(M)
    v = np.zeros(n)
    v[node2index[root]] = 1
    while np.sum(abs(v - (alpha * np.matmul(M, v) + (1 - alpha) * v))) > 1e-10:
        v = alpha * np.matmul(M, v) + (1 - alpha) * v
    for ind, prob in enumerate(v):
        result.append([index2node[ind], prob])
        result = sorted(result, key = lambda x:x[1], reverse = True)[:num_candidates]
    return result

def Generate_Transfer_Matrix(G):
    index2node = dict()
    node2index = dict()
    for index,node in enumerate(G.keys()):
        node2index[node] = index
        index2node[index] = node
    # num of nodes
    n = len(node2index)
    # generate Transfer probability matrix M, shape of (n,n)
    M = np.zeros([n,n])
    for node1 in G.keys():
        for node2 in G[node1]:
            # FIXME: some nodes not in the Graphs.keys, may incur some errors
            try:
                M[node2index[node2],node2index[node1]] = 1/len(G[node1])
            except:
                continue
    return M, node2index, index2node

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

if __name__ == '__main__':
    alpha = 0.85
    root = "759491"
    num_candidates = 25000000
    id_list = []
    G = Generate_G()
    #print(len(id_list))
    #print(len(G))
    M, node2index, index2node = Generate_Transfer_Matrix(G)
    result = PageRank(M, alpha, root)
    #print(result)
    #print(len(result))
    
    with open("output_data.csv", "w", encoding="UTF-8") as output:
        writer = csv.writer(output)
        for lines in result:
            writer.writerow(lines)
    