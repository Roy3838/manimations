from manim import *
import numpy as np
import random
from colour import Color




class polarization(Scene):


    def construct(self):
        A1=ValueTracker(2)
        A2=ValueTracker(2.7)
        w1=ValueTracker(5.2)
        w2=ValueTracker(2.0)
        phi1=ValueTracker(1.56)
        phi2=ValueTracker(0.0)
        def func(t):
            return np.array((A1.get_value()*np.sin(w1.get_value()*t+phi1.get_value()),A2.get_value()*np.sin(w2.get_value()*t+phi2.get_value()),0))
        def dotsfunc(t,pos):
            return np.array((A1*np.sin(w1*t.get_value()+phi1),A2*np.sin(w2*t.get_value()+phi2),0))+pos

        def func_tracker(t):
            return np.array((A1*np.sin(w1*t.get_value()+phi1),A2*np.sin(w2*t.get_value()+phi2),0))
        self.camera.background_color = "#E2E2E2"
        #sliders to change values of polarization of light
        #arange in matrix
        mobs=VGroup()
        dots=VGroup()
        # x=[-3,3]
        # y=[-2,2]
        # red=Color("cyan")
        # colors=list(red.range_to(Color("pink"),14))
        # t_val=ValueTracker(0)
        # for i in range(x[0],x[1]+1):
        #     for j in range(y[0],y[1]+1):
        #         COLOR = colors[(i-x[0])+(j-y[0])].hex
        #         POSITION= np.array((2*i,1.5*j,0))
        #         dot=Dot(POSITION).set_color(BLACK).scale(0.5)
        #         dots.add(dot)
        #         mobs.add(ParametricFunction(func, t_range = np.array([0, TAU]), fill_opacity=0).set_color(COLOR).scale(1.3).move_to(POSITION))
        
        coso=ParametricFunction(func, t_range = np.array([0, TAU]), fill_opacity=0).set_color(BLACK)
        coso.add_updater(lambda m: m.become(ParametricFunction(func, t_range = np.array([0, TAU]), fill_opacity=0)).set_color(BLACK)) 
        texto=Text("Polarization of light").scale(0.7).set_color(BLACK).to_edge(UP)
        
        A1_text=MathTex(r"A_{1}").to_edge(UL).set_color(BLACK).scale(0.7)
        A2_text=MathTex(r"A_{2}").move_to(A1_text.get_center()+DOWN).set_color(BLACK).scale(0.7)
        w1_text=MathTex(r"w_{1}").move_to(A2_text.get_center()+DOWN).set_color(BLACK).scale(0.7)
        w2_text=MathTex(r"w_{2}").move_to(w1_text.get_center()+DOWN).set_color(BLACK).scale(0.7)
        phi1_text=MathTex(r"\phi_{1}").move_to(w2_text.get_center()+DOWN).set_color(BLACK).scale(0.7)
        phi2_text=MathTex(r"\phi_{2}").move_to(phi1_text.get_center()+DOWN).set_color(BLACK).scale(0.7)

        # number updaters
        A1_value=DecimalNumber(A1.get_value(),num_decimal_places=2).next_to(A1_text,RIGHT).set_color(BLACK).scale(0.7)
        A2_value=DecimalNumber(A2.get_value(),num_decimal_places=2).next_to(A2_text,RIGHT).set_color(BLACK).scale(0.7)
        w1_value=DecimalNumber(w1.get_value(),num_decimal_places=2).next_to(w1_text,RIGHT).set_color(BLACK).scale(0.7)
        w2_value=DecimalNumber(w2.get_value(),num_decimal_places=2).next_to(w2_text,RIGHT).set_color(BLACK).scale(0.7)
        phi1_value=DecimalNumber(phi1.get_value(),num_decimal_places=2).next_to(phi1_text,RIGHT).set_color(BLACK).scale(0.7)
        phi2_value=DecimalNumber(phi2.get_value(),num_decimal_places=2).next_to(phi2_text,RIGHT).set_color(BLACK).scale(0.7)
        # updaters
        A1_value.add_updater(lambda m: m.set_value(A1.get_value()))
        A2_value.add_updater(lambda m: m.set_value(A2.get_value()))
        w1_value.add_updater(lambda m: m.set_value(w1.get_value()))
        w2_value.add_updater(lambda m: m.set_value(w2.get_value()))
        phi1_value.add_updater(lambda m: m.set_value(phi1.get_value()))
        phi2_value.add_updater(lambda m: m.set_value(phi2.get_value()))

        texts=VGroup(A1_text,A2_text,w1_text,w2_text,phi1_text,phi2_text,A1_value,A2_value,w1_value,w2_value,phi1_value,phi2_value)
        


        if(True):
            
            A1.set_value(2)
            A2.set_value(3)
            self.add(coso,texto,texts)

        else:
            self.play(Create(coso))
            self.play(Create(texts))
            inter_time=0.3
            self.wait()
            self.play(A1.animate.set_value(2.3),A2.animate.set_value(1.5),w1.animate.set_value(2.0),w2.animate.set_value(2.0),phi1.animate.set_value(0.0),phi2.animate.set_value(0.0),run_time=2)
            self.wait(inter_time)
            self.play(phi1.animate.set_value(5),run_time=3)
            self.wait(inter_time)
            self.play(phi2.animate.set_value(5),run_time=3)
            self.wait(inter_time)
            self.play(phi1.animate.set_value(0),phi2.animate.set_value(PI/2),run_time=3)
            self.wait(inter_time)
            self.play(w1.animate.set_value(1.0), run_time=3)
            self.wait(inter_time)
            self.play(w2.animate.set_value(1.0), run_time=3)
            self.wait(inter_time)
            self.play(w1.animate.set_value(3*PI/2),w2.animate.set_value(-PI),run_time=3)
            self.wait(inter_time)
            self.play(A1.animate.set_value(3),A2.animate.set_value(3),run_time=3)
            self.wait(inter_time)
            self.play(w1.animate.set_value(-PI/10),w2.animate.set_value(PI/8), run_time=3)
            self.wait(inter_time)
            self.play(phi1.animate.set_value(1.56),phi2.animate.set_value(0.0),run_time=3)
            self.wait(inter_time)
            self.play(phi1.animate.set_value(0.0),run_time=3)
            self.wait(inter_time)
            self.play(w1.animate.set_value(5.2),w2.animate.set_value(-PI),run_time=3)
            self.wait(inter_time)
            self.play(w1.animate.set_value(-PI),w2.animate.set_value(5.2),run_time=3)
            self.wait(inter_time)
            self.play(w1.animate.set_value(-PI),w2.animate.set_value(PI/12),run_time=3)
            self.wait(inter_time)
            self.play(w1.animate.set_value(PI/3),w2.animate.set_value(-2*PI/3),run_time=3)
            self.wait(inter_time)
            self.play(w1.animate.set_value(-PI/8),w2.animate.set_value(PI/2),run_time=3)
            self.wait(inter_time)
            self.play(w1.animate.set_value(-PI/5),w2.animate.set_value(PI),run_time=3)
            self.wait(inter_time)
            self.play(A1.animate.set_value(2.3),A2.animate.set_value(1.5),w1.animate.set_value(2.0),w2.animate.set_value(2.0),phi1.animate.set_value(0.0),phi2.animate.set_value(0.0),run_time=2)

            

            self.wait()
        
        #self.add(dots)
        #self.play(MoveAlongPath(dots[0],mobs[0]),
        #run_time=5,rate_func=linear)
        #self.wait()