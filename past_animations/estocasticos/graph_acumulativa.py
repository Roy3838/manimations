from manim import *
import numpy as np




class Accumulativa(ThreeDScene):
    def construct(self):

        # Background
        self.camera.background_color = "#E2E2E2"

        def f(x,y):
            return -(1+np.cos(12*np.sqrt(x**2+y**2)))/(0.5*(x**2+y**2)+2)

        cosoplano= Surface(
            lambda u, v: np.array([u,v,f(u,v)]),
            resolution=(10, 10),
            v_range=[-4, 4],
            u_range=[-4, 4]
        ).set_fill_by_checkerboard(PURPLE, RED, opacity=0.5)


        # angle camera

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, distance=10)


        # self.play(Create(ThreeDAxes().set_color(BLACK)))
        # rotate camera
        self.renderer.camera.light_source.move_to(3*IN + 3*LEFT + 3*UP)
        self.play(Create(cosoplano))

        self.play(Rotate(cosoplano, PI/2, axis=IN),run_time=2)
        self.wait()
        self.play(Rotate(cosoplano, PI/2, axis=OUT),run_time=2)
        self.wait()
        self.play(Rotate(cosoplano, PI/4, axis=IN))
        self.wait()
        self.play(Rotate(cosoplano, PI/4, axis=LEFT+DOWN))
        

        self.wait()