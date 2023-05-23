from manim import *
import numpy as np



class Yakovenko(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        def BoltzManng(x):
            c = 4.63
            b = 0
            a = 0.0295
            return np.exp(-a*x+c)+b
        
        ax = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 100, 20],
            tips=True,
            axis_config={"include_numbers": True}
            #,y_axis_config={"scaling": LogBase(custom_labels=True)}
        ).set_color(BLACK)
        
        labels = ax.get_axis_labels(x_label=Tex("\$"), y_label=Tex(r"\% de personas"))
        labels.set_color(BLACK)
                
        secondax = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 2, 0.5],
            tips=True,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
            ).set_color(BLACK)

        thirdax = Axes(
            x_range=[0, 3.5, 0.5],
            y_range=[-1, 2.2, 0.5],
            tips=True,
            axis_config={"include_numbers": True},
            x_axis_config={"scaling": LogBase(custom_labels=True)},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
            ).set_color(BLACK)

        curve_exp = ax.plot(lambda x: BoltzManng(x), x_range=[0, 100], color=BLUE_C)

        curve_exp2=secondax.plot(lambda x: BoltzManng(x), x_range=[0, 100], color=BLUE_C)

        curve_exp3=thirdax.plot(lambda x: BoltzManng(x), x_range=[0, 2.3], color=BLUE_C)

        # Boltzmann Gibbs Part
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        y = [100.0, 97.0, 94.0, 91.0, 88.0, 86.0, 83.0, 81.0, 79.0, 76.0, 74.0, 72.0, 70.0, 
        68.0, 66.0, 64.0, 62.0, 60.0, 59.0, 57.0, 42.0, 32.0, 23.0, 17.0, 13.0, 10.0, 7.0, 5.0]
        # Pareto Part, last 3 datapoints
        px=[190, 500, 1000]
        py=[1.5, 0.26, 0.1]
        # Concat the two lists
        x = x + px
        y = y + py

        print(x)
        print(y)

        plot1=ax.plot_line_graph(
            x_values=x,
            y_values=y,
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,
        )
        plot2=secondax.plot_line_graph(
            x_values=x,
            y_values=y,
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,
        )
        plot3=thirdax.plot_line_graph(
            x_values=x,
            y_values=y,
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,
        )

        
        

        self.play(Create(ax))
        self.play(Create(labels))

        self.wait()

        self.play(Create(curve_exp))
        self.wait()
        self.play(Create(plot1))

        self.wait(2)

        self.play(ReplacementTransform(ax, secondax),
        ReplacementTransform(curve_exp, curve_exp2),
        ReplacementTransform(plot1, plot2),)

        self.wait()

        self.play(ReplacementTransform(secondax, thirdax),
        ReplacementTransform(curve_exp2, curve_exp3),
        ReplacementTransform(plot2, plot3),)

        self.wait(3)


    










