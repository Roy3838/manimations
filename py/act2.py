from manim import *
import numpy as np
COLOR_PRINCIPAL = BLUE
COLOR_1 = RED
COLOR_2 = YELLOW
COLOR_3 = GREEN
class Act2(Scene):
   def construct(self):
       self.cos1()
       self.cos2()
       self.cos3()
       self.cos4()
   # a scene that graphs the function f(x) = 10*sen(3x-0.5t) as time passes     
   def cos1(self):
       time=ValueTracker(0)
       axes = Axes(
           x_range=[-1, 6, 1],
           y_range=[-10, 10, 1],
           axis_config={"color": GREEN},
           tips=True,
       )
       axes_labels = axes.get_axis_labels()
       sin_graph = axes.plot(lambda t: 10*np.sin(3*t-0.5*time.get_value()), color=COLOR_PRINCIPAL)
       sin_graph1=axes.plot(lambda t: 10*np.sin(3*t), color=COLOR_1)
       sin_graph2=axes.plot(lambda t: 10*np.sin(3*t-0.5*4), color=COLOR_2)
       sin_graph3=axes.plot(lambda t: 10*np.sin(3*t-0.5*8), color=COLOR_3)
       sin_graph.add_updater(lambda z: z.become(
           axes.plot(lambda t: 10*np.sin(3*t-0.5*time.get_value()), color=COLOR_PRINCIPAL)
       ))
       self.play(Create(axes))
       self.play(Create(sin_graph))
       self.add(sin_graph1)
       self.play(time.animate.set_value(4))
       self.add(sin_graph2)
       self.play(time.animate.set_value(8))
       self.add(sin_graph3)
       self.play(FadeOut(sin_graph))
       self.play(FadeOut(sin_graph1),FadeOut(sin_graph2),FadeOut(sin_graph3))
       self.play(FadeOut(axes))
   
   # a scene that graphs the function f(x) = 10*cos(3x-0.5t) as time passes  
   def cos2(self):
       time=ValueTracker(0)
       axes = Axes(
           x_range=[-1, 6, 1],
           y_range=[-10, 10, 1],
           axis_config={"color": GREEN},
           tips=True,
       )
       axes_labels = axes.get_axis_labels()
       sin_graph = axes.plot(lambda t: 10*np.cos(3*t-0.5*time.get_value()), color=COLOR_PRINCIPAL)
       sin_graph1=axes.plot(lambda t: 10*np.cos(3*t), color=COLOR_1)
       sin_graph2=axes.plot(lambda t: 10*np.cos(3*t-0.5*4), color=COLOR_2)
       sin_graph3=axes.plot(lambda t: 10*np.cos(3*t-0.5*8), color=COLOR_3)
       sin_graph.add_updater(lambda z: z.become(
           axes.plot(lambda t: 10*np.cos(3*t-0.5*time.get_value()), color=COLOR_PRINCIPAL)
       ))
       self.play(Create(axes))
       self.play(Create(sin_graph))
       self.add(sin_graph1)
       self.play(time.animate.set_value(4))
       self.add(sin_graph2)
       self.play(time.animate.set_value(8))
       self.add(sin_graph3)
       self.play(FadeOut(sin_graph))
       self.play(FadeOut(sin_graph1),FadeOut(sin_graph2),FadeOut(sin_graph3))
       self.play(FadeOut(axes))
      
   # a scene that graphs the function f(x) = 10*sen(-3x-0.5t) as time passes  
   def cos3(self):
       time=ValueTracker(0)
       axes = Axes(
           x_range=[-1, 6, 1],
           y_range=[-10, 10, 1],
           axis_config={"color": GREEN},
           tips=True,
       )
       axes_labels = axes.get_axis_labels()
       sin_graph = axes.plot(lambda t: 10*np.sin(-3*t-0.5*time.get_value()), color=COLOR_PRINCIPAL)
       sin_graph1=axes.plot(lambda t: 10*np.sin(-3*t), color=COLOR_1)
       sin_graph2=axes.plot(lambda t: 10*np.sin(-3*t-0.5*4), color=COLOR_2)
       sin_graph3=axes.plot(lambda t: 10*np.sin(-3*t-0.5*8), color=COLOR_3)
       sin_graph.add_updater(lambda z: z.become(
           axes.plot(lambda t: 10*np.sin(-3*t-0.5*time.get_value()), color=COLOR_PRINCIPAL)
       ))
       self.play(Create(axes))
       self.play(Create(sin_graph))
       self.add(sin_graph1)
       self.play(time.animate.set_value(4))
       self.add(sin_graph2)
       self.play(time.animate.set_value(8))
       self.add(sin_graph3)
       self.play(FadeOut(sin_graph))
       self.play(FadeOut(sin_graph1),FadeOut(sin_graph2),FadeOut(sin_graph3))
       self.play(FadeOut(axes))
      
      
   # a scene that graphs the function f(x) = 10*sen(3x-0.5t) + 10*cos(3x-0.5t) as time passes  
   def cos4(self):
       time=ValueTracker(0)
       axes = Axes(
           x_range=[-1, 6, 1],
           y_range=[-10, 10, 1],
           axis_config={"color": GREEN},
           tips=True,
       )
       axes_labels = axes.get_axis_labels()
       sin_graph = axes.plot(lambda t: 10*np.sin(3*t-0.5*time.get_value())+10*np.cos(3*t-0.5*time.get_value()), color=COLOR_PRINCIPAL)
       sin_graph1 = axes.plot(lambda t: 10*np.sin(3*t)+10*np.cos(3*t), color=COLOR_1)
       sin_graph2 = axes.plot(lambda t: 10*np.sin(3*t-0.5*4)+10*np.cos(3*t-0.5*4), color=COLOR_2)
       sin_graph3 = axes.plot(lambda t: 10*np.sin(3*t-0.5*8)+10*np.cos(3*t-0.5*8), color=COLOR_3)
       sin_graph.add_updater(lambda z: z.become(
           axes.plot(lambda t: 10*np.sin(3*t-0.5*time.get_value())+10*np.cos(3*t-0.5*time.get_value()), color=COLOR_PRINCIPAL)
       ))
       self.play(Create(axes))
       self.play(Create(sin_graph))
       self.add(sin_graph1)
       self.play(time.animate.set_value(4))
       self.add(sin_graph2)
       self.play(time.animate.set_value(8))
       self.add(sin_graph3)
       self.play(FadeOut(sin_graph))
       self.play(FadeOut(sin_graph1),FadeOut(sin_graph2),FadeOut(sin_graph3))
       self.play(FadeOut(axes))
      
