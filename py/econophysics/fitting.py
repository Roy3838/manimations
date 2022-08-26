import numpy as np
import pandas as pd



print("reading csv")
matclass= np.genfromtxt('matclasses.csv', delimiter=',')
print("mat loaded")


#get last row
lastrow=matclass[-1]



dataset=pd.DataFrame(lastrow)
#save dataset to csv
dataset.to_csv('expo.csv', index=False)