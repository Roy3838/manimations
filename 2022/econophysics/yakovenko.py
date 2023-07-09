from manim import *
import numpy as np



class Yakovenko(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        e = 2.718281828459045
        
        def funcexp(x):
            return 100*e**(-0.047*x)

        def funcexpexp(x):
            return 100*e**(-0.047*x)
        
        def funcnor(x):
            # 70*e**(-0.002*(-50)**2)
            return 700*e**(-0.002*(-50)**2)
        
        ax = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 100, 20],
            tips=True,
            axis_config={"include_numbers": True}
            #,y_axis_config={"scaling": LogBase(custom_labels=True)}
        ).set_color(BLACK)
        
        labels = ax.get_axis_labels(x_label=Tex("\$"), y_label=Tex("N personas"))
        labels.set_color(BLACK)
        
        curve_normal = ax.plot(lambda x: funcnor(x), x_range=[0, 100], color=BLUE_C)
        
        curve_exp = ax.plot(lambda x: funcexp(x), x_range=[0, 100], color=BLUE_C)
        
        secondax = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 2, 0.5],
            tips=True,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
            ).set_color(BLACK)


        thirdax = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 2, 0.5],
            tips=True,
            axis_config={"include_numbers": True},
            x_axis_config={"scaling": LogBase(custom_labels=True)},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
            ).set_color(BLACK)

    
        curve_exp_exp=secondax.plot(lambda x: funcexpexp(x), x_range=[0, 100], color=BLUE_C)

        curve_exp_third=thirdax.plot(lambda x: funcexp(x), x_range=[0, 2], color=BLUE_C)

        #plotting values cientific notation
        x=[10**0,10**0.5,10**1,10**1.5,10**1.75,10**2,10**2.25,10**2.5]
        y=[10**2,10**1.8,10**1.65,10**1.5,10**1,10**0.5,10**0.4,10**0.3]
        #plotting values non cientific notation
        x=[1  , 3.16 , 10   , 31.62, 56.23, 63.09 , 100  , 177.82, 316.22 ]
        y=[90 , 80   , 60.66, 25.62, 8    , 3.98  , 3.162, 2.51  , 1.99   ]



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

        self.play(Create(curve_normal))

        self.wait()

        self.play(ReplacementTransform(curve_normal, curve_exp))

        self.play(Create(plot1))

        self.wait(2)


        self.play(ReplacementTransform(ax,secondax), ReplacementTransform(curve_exp, curve_exp_exp), FadeOut(plot1))

        self.wait(2)

        self.play(Create(plot2))

        self.wait(2)


        self.play(ReplacementTransform(secondax,thirdax), ReplacementTransform(curve_exp_exp,curve_exp_third), FadeOut(plot2))

        self.wait(2)

        self.play(Create(plot3))

        self.wait(3)
