from manim import *
import numpy as np
import random
from colour import Color




class polarization(Scene):


    def construct(self):
        A1=0.23
        A2=0.50
        w1=5.2
        w2=2.0
        phi1=1.56
        phi2=0.0
        def func(t):
            return np.array((A1*np.sin(w1*t+phi1),A2*np.sin(w2*t+phi2),0))
        def dotsfunc(t,pos):
            return np.array((A1*np.sin(w1*t.get_value()+phi1),A2*np.sin(w2*t.get_value()+phi2),0))+pos

        def func_tracker(t):
            return np.array((A1*np.sin(w1*t.get_value()+phi1),A2*np.sin(w2*t.get_value()+phi2),0))
        self.camera.background_color = "#E2E2E2"
        #sliders to change values of polarization of light
        #arange in matrix
        mobs=VGroup()
        dots=VGroup()
        x=[-3,3]
        y=[-2,2]
        red=Color("cyan")
        colors=list(red.range_to(Color("pink"),14))
        t_val=ValueTracker(0)
        for i in range(x[0],x[1]+1):
            for j in range(y[0],y[1]+1):
                COLOR = colors[(i-x[0])+(j-y[0])].hex
                POSITION= np.array((2*i,1.5*j,0))
                dot=Dot(POSITION).set_color(BLACK).scale(0.5)
                dots.add(dot)
                mobs.add(ParametricFunction(func, t_range = np.array([0, TAU]), fill_opacity=0).set_color(COLOR).scale(1.3).move_to(POSITION))
                
                
        self.add(mobs)
        self.add(dots)
        self.play(MoveAlongPath(dots[0],mobs[0]),
            MoveAlongPath(dots[1],mobs[1]),
            MoveAlongPath(dots[2],mobs[2]),
            MoveAlongPath(dots[3],mobs[3]),
            MoveAlongPath(dots[4],mobs[4]),
            MoveAlongPath(dots[5],mobs[5]),
            MoveAlongPath(dots[6],mobs[6]),
            MoveAlongPath(dots[7],mobs[7]),
            MoveAlongPath(dots[8],mobs[8]),
            MoveAlongPath(dots[9],mobs[9]),
            MoveAlongPath(dots[10],mobs[10]),
            MoveAlongPath(dots[11],mobs[11]),
            MoveAlongPath(dots[12],mobs[12]),
            MoveAlongPath(dots[13],mobs[13]),
            MoveAlongPath(dots[14],mobs[14]),
            MoveAlongPath(dots[15],mobs[15]),
            MoveAlongPath(dots[16],mobs[16]),
            MoveAlongPath(dots[17],mobs[17]),
            MoveAlongPath(dots[18],mobs[18]),
            MoveAlongPath(dots[19],mobs[19]),
            MoveAlongPath(dots[20],mobs[20]),
            MoveAlongPath(dots[21],mobs[21]),
            MoveAlongPath(dots[22],mobs[22]),
            MoveAlongPath(dots[23],mobs[23]),
            MoveAlongPath(dots[24],mobs[24]),
            MoveAlongPath(dots[25],mobs[25]),
            MoveAlongPath(dots[26],mobs[26]),
            MoveAlongPath(dots[27],mobs[27]),
            MoveAlongPath(dots[28],mobs[28]),
            MoveAlongPath(dots[29],mobs[29]),
            MoveAlongPath(dots[30],mobs[30]),
            MoveAlongPath(dots[31],mobs[31]),
            MoveAlongPath(dots[32],mobs[32]),
            MoveAlongPath(dots[33],mobs[33]),
            MoveAlongPath(dots[34],mobs[34]),
        run_time=5,rate_func=linear)
        self.wait()