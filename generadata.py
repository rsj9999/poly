import numpy as np
import pandas as pd
#Genera datos aleatoriamente
x = np.random.randn(50)
sigma = np.random.randn(len(x))/3
y = x**2-2*x+1 + sigma

#Los guarda en formato csv
data = pd.DataFrame(np.array([x,y]).T, columns=["x", "y"])
data.to_csv("dataPolyDegree2.csv")