import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
seq_data = pd.read_csv("tumor_data/data.csv")
seq_data.rename(columns={'Unnamed: 0':'sample'}, inplace=True)
labels = pd.read_csv("tumor_data/labels.csv")
labels.rename(columns={'Unnamed: 0':'sample'}, inplace=True)
tumor_data = seq_data.set_index('sample').to_numpy()


#f = open("./tumor_data/bladder-rsem-fpkm-gtex.txt")
#next(f)
#line = f.readline()   
#list1 = []
#tumor_data=[]
#while line:
#    a = line.split()
#    b = a[1:]  
#    for num in b:
#        tumor_data.append(float(num))
    #tumor_data.append(float(list1)) 
 #   line = f.readline()
#f.close()

print(tumor_data)


array=[]
result=[]
#print(tumor_data)

#i is the number of genes
i=15

for x in range(0,i):
    Data= tumor_data[: x]
    #print(Data)
    values = Data
    SD = Data
    #Mean
    values = np.mean(Data)
    Avg=round(values,4)
    array.append(Avg)
print('\n')


for y in range(0, i):
    Data = tumor_data[: y]
    values = Data
    SD = Data
    #Std
    SD = np.std(Data,ddof=1)
    Std=round(SD,4)
    result.append(Std)
print('\n')

#Avg_float = []
#for i in array:
 #   Avg_float.append(float(i))

#Std_float = []
#for j in result:
#    Std_float.append(float(j))

#print("mean=",Std_float)

index = np.arange(i)
print("mean=",array)
print("std=",result)

new_ticks = np.linspace(0, i-1, i)
Array_float=[]
for i in new_ticks:
    i= int(i)
    j = str(i)
    Array_float.append(j)
print('\n')
print(Array_float)

plt.xlabel('Genes')
plt.ylabel('Mean')
plt.title('one Std of the Mean about UCI Database')
plt.bar(index, array, yerr=result, error_kw={'ecolor': '0.3', 'capsize': 6}, alpha=0.8)
plt.xticks(index + 0.2, Array_float)
plt.legend(loc=2)
plt.show()
