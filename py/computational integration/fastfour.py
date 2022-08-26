import numpy as np
import pandas as pd
import matplotlib

dataset=pd.read_csv('930-data-export.csv')
X = np.fft.fft(dataset['Total CAL Demand (MWh)'])
matplotlib.pyplot.plot(dataset['Timestamp (Hour Ending)'], dataset['Total CAL Demand (MWh)'])
matplotlib.pyplot.show()

matplotlib.pyplot.plot(dataset['Timestamp (Hour Ending)'], X)
matplotlib.pyplot.show()

frecuencia = (np.arange(len(X)))/len(X)/1/(60*60)


