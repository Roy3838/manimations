from manim import * 
import pandas as pd
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt


class fftm(Scene):
    def construct(self):   
        self.camera.background_color = "#E2E2E2"
        #plot1(pd.read_csv('930-data-export.csv', delimiter=',', parse_dates=[1]))
        self.plot2()
        #plot3(pd.read_csv('930-data-export.csv', delimiter=',', parse_dates=[1]))



    def plot3():
        dataset=pd.read_csv('930-data-export.csv', delimiter=',', parse_dates=[1])
        '''
        TERCER PLOT, SE GRAFICA EL FFT PERO EN HORAS
        '''
        

        #calcular los valores que se van a usar en el plot del fft
        X = fft(dataset['Total CAL Demand (MWh)'])
        N = len(X)
        n = np.arange(N)
        #Se tiene frequencia angular y se cambia a Hertz
        sr = 1 / (60*60)
        T = N/sr
        freq = n/T 
        n_oneside = N//2
        f_oneside = freq[:n_oneside]
        #Convertir frequencia a horas
        t_h = 1/f_oneside / (60 * 60)
        
        #Plot con matplotlib
        plt.figure(figsize = (15, 7))
        plt.plot(t_h, np.abs(X[:n_oneside])/n_oneside, color='red')
        plt.xticks([12,24, 84])
        plt.xlim(5, 90)
        plt.xlabel('Periodo (Horas)')
        plt.ylabel('|FFT(x)|')
        plt.show()



#Referencias
#https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html
#https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.04-FFT-in-Python.html
#https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

