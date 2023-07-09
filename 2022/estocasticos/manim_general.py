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

class VariationalAutoencoderScene(Scene):

    def construct(self):



        self.camera.background_color = "#E2E2E2"
        """ SETUP """   
        neural_network = NeuralNetwork([
            FeedForwardLayer(1),
            FeedForwardLayer(4),
            FeedForwardLayer(4),
            FeedForwardLayer(3),
        ], layer_spacing=0.5).move_to(UP*2).scale(2)

        dataSIR = pd.read_csv(ROOT_DIR / "SIR.csv")
        dataSIR = dataSIR.to_numpy()
        #print(dataSIR)
        # data from 0 to 100
        S_data = dataSIR[0:100,0]
        I_data = dataSIR[100:200,0]
        R_data = dataSIR[200:300,0]
        #print(S_data.shape, I_data.shape, R_data.shape)
        #flip data around
        S_data = np.flip(S_data)
        I_data = np.flip(I_data)
        R_data = np.flip(R_data)
        x_axis= np.linspace(0,100,100)

        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 500, 50],
            
        ).scale(0.5).move_to(DOWN*1.5).set_color(BLACK)
        # plot the data
        S_plot = axes.plot_line_graph(x_axis,S_data, 
        add_vertex_dots=False).set_color(BLUE)
        I_plot = axes.plot_line_graph(x_axis,I_data,
        add_vertex_dots=False).set_color(RED)
        R_plot = axes.plot_line_graph(x_axis,R_data,
        add_vertex_dots=False).set_color(GREEN)

        """ DOING ANIMATIONS    """
        Tex.set_default(color=BLACK)
        Text.set_default(color=BLACK)
        # change neural_network color
        label_inputs = Text("i").move_to(neural_network.get_left() + LEFT).scale(0.8)
        S = Text("S[i]").move_to(UP).scale(0.8)
        I = Text("I[i]") .scale(0.8)
        R = Text("R[i]").move_to(DOWN).scale(0.8)
        SIR = VGroup(S, I, R).move_to(neural_network.get_right() + RIGHT)
        labelcopia = label_inputs.copy()
        SIRcopia = SIR.copy()

        self.play(Create(axes),Create(S_plot),Create(I_plot),Create(R_plot))

        self.play(Create(neural_network),run_time=2)

        def animi(i1):
            self.play(Create(labelcopia), Create(SIRcopia), run_time=0.7)
            i1_tex = Tex(str(i1)).move_to(neural_network.get_left() + LEFT)
            S1 = Tex(str(S_data[i1])).move_to(UP)
            I1 = Tex(str(I_data[i1]))
            R1 = Tex(str(R_data[i1])).move_to(DOWN)
            SIR1 = VGroup(S1, I1, R1).move_to(neural_network.get_right() + RIGHT)
            graph_pos= axes.coords_to_point(x_axis[i1],0)
            i1_tex_graph=Tex(str(i1)).move_to(graph_pos+DOWN*0.5)

            pointS = axes.coords_to_point(x_axis[i1],S_data[i1])
            pointI = axes.coords_to_point(x_axis[i1],I_data[i1])
            pointR = axes.coords_to_point(x_axis[i1],R_data[i1])
            
            dotS = Dot(pointS, color=BLUE)
            dotI = Dot(pointI, color=RED)
            dotR = Dot(pointR, color=GREEN)

            label_graphS = S1.copy().move_to(axes.coords_to_point(0,S_data[i1])+LEFT*0.5)
            label_graphI = I1.copy().move_to(axes.coords_to_point(0,I_data[i1])+LEFT*0.5)
            label_graphR = R1.copy().move_to(axes.coords_to_point(0,R_data[i1])+LEFT*0.5)


            lineS = Line(pointS,axes.coords_to_point(0,S_data[i1]), color=BLUE, stroke_width=2)
            lineI = Line(pointI,axes.coords_to_point(0,I_data[i1]), color=RED, stroke_width=2)
            lineR = Line(pointR,axes.coords_to_point(0,R_data[i1]), color=GREEN, stroke_width=2)
            

            self.play(Create(i1_tex_graph), Create(dotS), Create(dotI), Create(dotR), run_time=0.6)
            self.play(ReplacementTransform(label_inputs, i1_tex),FadeOut(labelcopia),ReplacementTransform(i1_tex_graph, i1_tex),run_time=0.3)
            self.play(
                neural_network.make_forward_pass_animation(run_time=1,passing_flash=True)
                )
            self.play(ReplacementTransform(SIR, SIR1),FadeOut(SIRcopia), run_time=0.6)
            self.play(ReplacementTransform(S1, dotS), ReplacementTransform(I1, dotI), ReplacementTransform(R1, dotR),
            Create(lineS), Create(lineI), Create(lineR), run_time=0.9)
            self.play(ReplacementTransform(S1, label_graphS), ReplacementTransform(I1, label_graphI), 
            ReplacementTransform(R1, label_graphR), run_time=0.9)
            # fade out only loop variables
            self.play(FadeOut(i1_tex), FadeOut(SIR1), 
            FadeOut(dotS), FadeOut(dotI), FadeOut(dotR), 
            FadeOut(lineS), FadeOut(lineI), FadeOut(lineR), 
            FadeOut(label_graphS), FadeOut(label_graphI), FadeOut(label_graphR),run_time=0.5)
        
        animi(40)
        animi(25)
        animi(35)
        animi(60)
        animi(75)


