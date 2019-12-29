import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


numpy_time={}
normal_time={}

for n in range(10,101):
    A = np.random.randint(1, n, size=(n, n))
    B = np.random.randint(1, n, size=(n, n))

    result = np.zeros((n,n))
    
    start_time = time.time()
    for i in range(len(A)): 
  
        for j in range(len(B[0])): 
  
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j]
    normal_time.update({n:time.time()-start_time})

    start_time_numpy = time.time()
    res =  np.dot(A,B)
    numpy_time.update({n:time.time()-start_time_numpy})



df_list = [normal_time, numpy_time]

df = pd.DataFrame(df_list, index=['Normal Time', 'Numpy Time'])
df = df.transpose()
df.head(10)

ax = df.plot.line(title="Numpy v/s Python for Matrix Multiplication")
ax.set_xlabel("Value of n (no. of rows and columns)")
ax.set_ylabel("Time (in seconds)")
plt.show()
