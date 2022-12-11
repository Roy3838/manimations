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

class SIR_neural_Net(ZoomedScene):

    def construct(self):
        
        self.camera.background_color = "#E2E2E2"
        """ SETUP """   
        neural_network = NeuralNetwork([
            FeedForwardLayer(20),
            FeedForwardLayer(4),
            FeedForwardLayer(4),
            FeedForwardLayer(5),
        ], layer_spacing=0.5).move_to(RIGHT*4).scale(0.9)

        dataSIR = pd.read_csv(ROOT_DIR / "py/estocasticos/SIR.csv")
        dataSIR = dataSIR.to_numpy()
        #print(dataSIR)
        # data from 0 to 100
        # CHECAR PORQUE FLIPEE EL VECTOR
        R_data = dataSIR[0:100,0]
        I_data = dataSIR[100:200,0]
        S_data = dataSIR[200:300,0]
        #print(S_data.shape, I_data.shape, R_data.shape)
        #flip data around
        S_data = np.flip(S_data)
        I_data = np.flip(I_data)
        R_data = np.flip(R_data)
        x_axis= np.linspace(0,100,100)

        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 500, 50],
            
        ).scale(0.5).move_to(LEFT*5).rotate(PI/2).set_color(BLACK)
        # plot the data
        S_plot = axes.plot_line_graph(x_axis,S_data, 
        add_vertex_dots=False).set_color(BLUE)
        I_plot = axes.plot_line_graph(x_axis,I_data,
        add_vertex_dots=False).set_color(RED)
        R_plot = axes.plot_line_graph(x_axis,R_data,
        add_vertex_dots=False).set_color(GREEN)



        puntosS = VGroup()
        puntosI = VGroup()
        puntosR = VGroup()
        puntos = 50
        for i in range(puntos):
            x = i*2
            
            pointS = axes.coords_to_point(x_axis[x],S_data[x])
            pointI = axes.coords_to_point(x_axis[x],I_data[x])
            pointR = axes.coords_to_point(x_axis[x],R_data[x])
            puntosS.add(Dot(pointS, color=BLUE))
            puntosI.add(Dot(pointI, color=RED))
            puntosR.add(Dot(pointR, color=GREEN))

        vectorS = Matrix([[S_data[90]],[S_data[88]],  [ S_data[85]], [ S_data[55]],
        [" ... "], 
        [S_data[15]],[S_data[13]],[S_data[10]],  [S_data[1]], [S_data[0]]
        ]).scale(0.5).set_color(BLACK)

        vectorI = Matrix([[I_data[89]],[I_data[88]],  [ I_data[85]], [ I_data[55]],
        [" ... "],
        [I_data[15]],[I_data[13]],[I_data[10]],  [I_data[1]], [I_data[0]]
        ]).scale(0.5).set_color(BLACK)

        vectorR = Matrix([[R_data[90]],[R_data[89]],  [ R_data[75]], [ R_data[55]],
        [" ... "],
        [R_data[15]],[R_data[13]],[R_data[10]],  [R_data[1]], [R_data[0]]
        ]).scale(0.5).set_color(BLACK)

        label_vectS = Tex("S =").scale(0.5).next_to(vectorS, LEFT).set_color(BLACK)
        label_vectI = Tex("I =").scale(0.5).next_to(vectorI, LEFT).set_color(BLACK)
        label_vectR = Tex("R =").scale(0.5).next_to(vectorR, LEFT).set_color(BLACK)

        vectorS_v= VGroup(label_vectS, vectorS)
        vectorI_v= VGroup(label_vectI, vectorI)
        vectorR_v= VGroup(label_vectR, vectorR)

        input_red = Matrix([["S"], ["I"], ["R"]]).set_color(BLACK)
        input_red_label = Tex("In =").next_to(input_red, LEFT).set_color(BLACK)

        entrada_bigchungus = Matrix([
            [S_data[89]],[S_data[88]],  [ S_data[85]], [ S_data[55]],
        [" ... "], 
        [S_data[15]],[S_data[13]],[S_data[10]],  [S_data[1]], [S_data[0]],
        [I_data[89]],[I_data[88]],  [ I_data[85]], [ I_data[55]],
        [" ... "],
        [I_data[15]],[I_data[13]],[I_data[10]],  [I_data[1]], [I_data[0]],
        [R_data[90]],[R_data[89]],  [ R_data[75]], [ R_data[55]],
        [" ... "],
        [R_data[15]],[R_data[13]],[R_data[10]],  [R_data[1]], [R_data[0]]
        ]).scale(0.3).set_color(BLACK)


        salida_real = Matrix([["0.08"] ,["0.82"], ["0.07"], ["0.02"], ["0.01"]]).scale(0.3).move_to(neural_network.get_right()+RIGHT*0.5).set_color(BLACK)

        salida_binaria = Matrix([["0"] ,["1"], ["0"], ["0"], ["0"]]).scale(0.3).move_to(neural_network.get_right()+RIGHT*2).set_color(BLACK)

        salida_matrix = Matrix([["1<r0<2"],["2<r0<5"],["5<r0<7"],
        ["7<r0<12"],["12<r0<20"]]).move_to(neural_network.get_right()+RIGHT*3).scale(0.3).set_color(BLACK)



        graphcompleta = VGroup(axes,S_plot,I_plot,R_plot)
        graphcompleta.move_to([0,0,0]).rotate(-PI/2)

        self.play(Create(graphcompleta[0]),Create(graphcompleta[1]),Create(graphcompleta[2]),Create(graphcompleta[3]))
        self.wait()
        self.play(graphcompleta.animate.rotate(PI/2))
        self.play(graphcompleta.animate.move_to(LEFT*5))
        

        self.play(Create(neural_network),run_time=2)

        self.play(Create(puntosS),Create(puntosI),Create(puntosR))

        self.wait()
        
        self.play(puntosS.animate.shift(RIGHT*4))
        self.play(ReplacementTransform(puntosS, vectorS))
        self.play(Write(label_vectS))
        self.play(vectorS_v.animate.scale(0.5))
        self.play(vectorS_v.animate.shift(RIGHT*1.5 + UP*2))

        self.play(puntosI.animate.shift(RIGHT*4))
        self.play(ReplacementTransform(puntosI, vectorI))
        self.play(Write(label_vectI))
        self.play(vectorI_v.animate.scale(0.5))
        self.play(vectorI_v.animate.shift(RIGHT*1.5))

        self.play(puntosR.animate.shift(RIGHT*4))
        self.play(ReplacementTransform(puntosR, vectorR))
        self.play(Write(label_vectR))
        self.play(vectorR_v.animate.scale(0.5))
        self.play(vectorR_v.animate.shift(RIGHT*1.5 + DOWN*2))

        self.wait()

        
        self.play(Write(input_red),Write(input_red_label))
        self.wait(2)
        self.play(ReplacementTransform(vectorI_v, entrada_bigchungus),
        ReplacementTransform(vectorS_v, entrada_bigchungus),
        ReplacementTransform(vectorR_v, entrada_bigchungus),
        ReplacementTransform(input_red, entrada_bigchungus))
        self.wait(3)
        self.play(
            entrada_bigchungus.animate.move_to(neural_network.get_left())
        )
        self.play(FadeOut(entrada_bigchungus),run_time=0.4)
        self.play(neural_network.make_forward_pass_animation(run_time=3))



        
        self.play(self.camera.frame.animate.scale(0.5).move_to(neural_network.get_right() + RIGHT))

        self.play(Write(salida_real))
        self.wait()
        self.play(Write(salida_matrix))
        self.wait()
        self.play(Write(salida_binaria))
        self.wait()
        self.play(salida_binaria.animate.move_to(salida_real.get_center()), FadeOut(salida_real))
        self.play(neural_network.make_backward_pass_animation(run_time=3))
        self.wait()
        
        


        """ DOING ANIMATIONS    """

        

        #arrow pointing to bottom axis of the graph at i
        

        
        # self.play(
        #     ReplacementTransform(SIR ),
        # )



