import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
seq_data = pd.read_csv("tumor_data/data.csv")
seq_data.rename(columns={'Unnamed: 0':'sample'}, inplace=True)
#labels = pd.read_csv("tumor_data/labels.csv")
#labels.rename(columns={'Unnamed: 0':'sample'}, inplace=True)
tumor_data = seq_data.set_index('sample').to_numpy()
#print(tumor_data)

#Array1=tumor_data

#cut a x*y martic
Array1=[]
# THE ROW
for i in range(0,10):
    Data=tumor_data[i]
    #HE COLUME
    result=Data[:100]
    Array1.append(result)
print('\n')
print(Array1)

covariance_matrix = np.cov(Array1)

#auto xticklab
count = 0
for j in covariance_matrix[0]:
    count=count+1
print(count)

new_ticks = np.linspace(0, count-1, count)
X=[]
for i in new_ticks:
    i=int(i)
    j = "gene_" + str(i)
    X.append(j)
#print('\n')
#print(X)

#yticklab
new_ticks = np.linspace(0, count-1, count)
Y=[]
for i in new_ticks:
    i=int(i)
    j = "sample_" + str(i)
    Y.append(j)
#print('\n')
#print(Y)

# virtual
print(covariance_matrix)
import matplotlib.pyplot as mp, seaborn

mp.figure(figsize=(15, 10))
seaborn.heatmap(covariance_matrix, annot=False, cmap='YlGnBu',xticklabels=list(X), yticklabels=list(Y))
mp.show()