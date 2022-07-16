from manim import *
import numpy as np



class Brag(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        
        dotx=5
        doty=3
        dots=VGroup()
        #brag matrix of atoms
        for i in range(dotx):
            for j in range(doty):
                dot = Dot(color=PURPLE)
                dot.move_to(np.array([i,j,0]))
                dots.add(dot)
        xray=Dot().move_to(np.array([-4,3,0]))
        
        #parametric function that describes light beam
        A=0.2
        phi=ValueTracker(0)
        p=2*PI
        d1=ValueTracker(10)
        d2=ValueTracker(10)
        c=ValueTracker(0.1)
        ray1=ParametricFunction(lambda t: np.array
        ([t-(A*c.get_value()*
             np.sin(p*np.abs(t + phi.get_value()) 
                                    * (np.sqrt(4 + 2 * np.power(c.get_value(),2)) ))/(c.get_value()+1)) , 
        A*np.sin(p*(t+phi.get_value()) * (np.sqrt(4 + 2* (c.get_value()**2)))   )+c.get_value()*np.abs(t) ,
         0])
        ,color=RED,t_range=[-10,10])
        
        ray1.add_updater(lambda x: x.become(
            ParametricFunction(lambda t: np.array
        ([t-(A*c.get_value()*
             np.sin(p*np.abs(t + phi.get_value()) 
                                    * (np.sqrt(4 + 2 * np.power(c.get_value(),2)) ))/(c.get_value()+1)) , 
        A*np.sin(p*(t+phi.get_value()) * (np.sqrt(4 + 2* (c.get_value()**2)))   )+c.get_value()*np.abs(t) ,
         0])
        ,color=RED,t_range=[-10,10])
        ))

        ray2=ray1.copy()
        ray2.add_updater(lambda x: x.become(
            ParametricFunction(lambda t: np.array
        ([t-(A*c.get_value()*
             np.sin(p*np.abs(t + phi.get_value()) 
                                    * (np.sqrt(4 + 2 * np.power(c.get_value(),2)) ))/(c.get_value()+1)) , 
        A*np.sin(p*(t+phi.get_value()) * (np.sqrt(4 + 2* (c.get_value()**2)))   )+c.get_value()*np.abs(t) ,
         0])
        ,color=RED,t_range=[-10,10]).shift(DOWN) 
        ))

        ray3=ray1.copy()
        ray3.add_updater(lambda x: x.become(
            ParametricFunction(lambda t: np.array
        ([t-(A*c.get_value()*
             np.sin(p*np.abs(t + phi.get_value()) 
                                    * (np.sqrt(4 + 2 * np.power(c.get_value(),2)) ))/(c.get_value()+1)) , 
        A*np.sin(p*(t+phi.get_value()) * (np.sqrt(4 + 2* (c.get_value()**2)))   )+c.get_value()*np.abs(t) ,
         0])
        ,color=RED,t_range=[-10,10]).shift(DOWN*2) 
        ))
        
        

        
        dots.move_to(np.array([0,-1,0]))
        self.play(Create(dots))
        self.play(Create(ray1),Create(ray2),Create(ray3))
        self.play(c.animate.set_value(0.2))
        self.play(c.animate.set_value(0.3))
        self.play(c.animate.set_value(0.5))
        self.play(c.animate.set_value(1))
        self.play(c.animate.set_value(2))
        self.play(c.animate.set_value(3))