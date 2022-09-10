from manim import *
import numpy as np

width=1080
height=1920
config.frame_size = [width, height]
class Euler(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)



        def F(r,m0,m1):
            G=3
            return G*m0*m1/(r**2)
        
        t=10
        dt=0.1
        m1=10
        m2=1
        [x1,y1]=[0,1]
        [x2,y2]=[1,0]

        [vx1,vy1]=[0,1]
        [vx2,vy2]=[0,-1]
        # Define Bodies
        r1=[np.arange(0,t,dt),np.arange(0,t,dt)]
        r2=[np.arange(0,t,dt),np.arange(0,t,dt)]

        dr1=[np.arange(0,t,dt),np.arange(0,t,dt)]
        dr2=[np.arange(0,t,dt),np.arange(0,t,dt)]
        # Iterate time
        self.add(Axes())
        for i in range(0,len(r1[0])-1):
            distance=np.abs(r1[i]-r2[i])
            dr1[0][i+1] = dr1[0][i] + F(distance,m1,m2)*dt
            r1[0][i+1] = r1[0][i] + dr1[0][i]
            
            dr1[1][i+1] = dr1[1][i] + F(distance,m1,m2)*dt
            r1[1][i+1] = r1[1][i] + dr1[1][i]

            dr2[0][i+1] = dr2[0][i] + F(distance,m1,m2)*dt
            r2[0][i+1] = r2[0][i] + dr2[0][i]

            dr2[1][i+1] = dr2[1][i] + F(distance,m1,m2)*dt
            r2[1][i+1] = r2[1][i] + dr2[1][i]
            

            planet1=Sphere(radius=0.1,fill_opacity=1,fill_color=BLUE,stroke_width=0).move_to([r1[0][i+1],r1[1][i+1],0])
            planet2=Sphere(radius=0.1,fill_opacity=1,fill_color=RED,stroke_width=0).move_to([r2[0][i+1],r2[1][i+1],0])
            self.add(planet1,planet2)
            self.wait(1/60)
            self.remove(planet1,planet2)
        
        self.add(Text("hi"))
        
