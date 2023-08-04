from manim import *
import numpy as np

class ParametricSurface(ThreeDScene):
    

    def construct(self):
        self.camera.background_color = "#E2E2E2"

        def func(t, theta, h=0, a=1, k=0, b=3):
            x = h + a / np.cos(t)
            y = (k + b * np.tan(t)) * np.cos(theta)
            z = (k + b * np.tan(t)) * np.sin(theta)
            return np.array([x, y, z])
        
        axes = ThreeDAxes(
            x_range=[-4,4],
            x_length=8,
            y_range=[-4,4],
            y_length=8,
            z_range=[-4,4],
            z_length=8,
            x_axis_config={"include_tip": False},
            y_axis_config={"include_tip": False},
            z_axis_config={"include_tip": False},
            ).set_color(BLACK)


        surfaces = VGroup()
        params = VGroup()
        for i in range (-3,4):
            t = 1.1

            surface = Surface(
                lambda u, v: axes.c2p(*func(u, v, a = i)),
                u_range=[0, t],
                v_range=[-PI, PI],
                color=RED,
                resolution=(4, 4)
            ).set_style(fill_opacity=0.2).set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (RED, 0), (RED, 0.5)], axis=2)

            # Make a 2d version of the surface
            param = ParametricFunction(
                lambda t: axes.c2p(*func(t, 0, a=i)),
                t_range=[-t, t],
                color=RED
            )
            surfaces.add(surface)
            params.add(param)

        self.play(Create(params),Create(axes))

        self.wait()

        

        self.wait(PI)

        self.stop_3dillusion_camera_rotation()

        self.play(Create(surfaces))

        self.move_camera(phi=180 * DEGREES, run_time =2)
        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(3)
        self.stop_3dillusion_camera_rotation()
