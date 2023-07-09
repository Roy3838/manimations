from manim import *
from random import uniform
import numpy as np

class Logo(ThreeDScene):
    def construct(self):


        



        self.camera.background_color = "#ece6e2"
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(ThreeDAxes().set_color(BLACK)))

        for i in range(300):
            phi=uniform(0,2*PI)
            theta=uniform(0,2*PI)
            r=3
            coords=[r*np.sin(theta)*np.cos(phi),
                    r*np.sin(theta)*np.sin(phi),
                    r*np.cos(theta)]
            xyz=Vector(coords).set_color(GOLD)
            print(i)
            self.add(xyz)



        self.wait() 
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(PI)
        self.stop_ambient_camera_rotation()
        self.wait()

        
