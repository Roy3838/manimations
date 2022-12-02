from manim import *
from pathlib import Path
from manim_ml.neural_network.layers import Convolutional3DLayer
from manim_ml.neural_network.layers.feed_forward import FeedForwardLayer
from manim_ml.neural_network.layers.image import ImageLayer
from manim_ml.neural_network.neural_network import NeuralNetwork
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT_DIR = Path(__file__).parents[2]


class SIR(Scene):
    def construct(self):



        dataSIR = pd.read_csv(ROOT_DIR / "SIR.csv")
        dataSIR = dataSIR.to_numpy()
        #print(dataSIR)
        # data from 0 to 100
        S_data = dataSIR[0:100,0]
        I_data = dataSIR[100:200,0]
        R_data = dataSIR[200:300,0]
        #flip data around
        S_data = np.flip(S_data)
        I_data = np.flip(I_data)
        R_data = np.flip(R_data)
        x_axis= np.linspace(0,100,100)

        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 500, 50],
            
        )
        # plot the data
        S_plot = axes.plot_line_graph(x_axis,S_data, 
        add_vertex_dots=False)
        I_plot = axes.plot_line_graph(x_axis,I_data,
        add_vertex_dots=False)
        R_plot = axes.plot_line_graph(x_axis,R_data,
        add_vertex_dots=False)


        self.play(Create(axes),Create(S_plot),Create(I_plot),Create(R_plot))
        self.wait(2)

        #print(S_data.shape, I_data.shape, R_data.shape)
