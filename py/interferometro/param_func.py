from manim import *
import numpy as np

class ParametricSurface(ThreeDScene):
    

    def construct(self):
        self.camera.background_color = "#E2E2E2"

        def wave_updater(mobject, dt):
            #Create wave
            mobject.radius += 0.01 + 3*dt
            radius = mobject.radius
            radiusfinal=8 
            mobject.become(Circle(radius=radius,color=BLUE)
                                                .move_to(mobject.get_center())
                                                .set_opacity(0.5*(1-(1/radiusfinal)*radius)))

        def begin_flashing(mobject, dt):
            mobject.time += dt
            if mobject.time > 0.5 and mobject.flashing == True:
                flash = Circle(radius=0.01).move_to(mobject.get_center())
                flash.radius = 0.01
                flash.add_updater(wave_updater)
                self.add(flash)
                mobject.time = 0   


        def func(t, theta, h=0, a=1, k=0, b=3):
            x = h + a / np.cos(t)
            y = (k + b * np.tan(t)) * np.cos(theta)
            z = (k + b * np.tan(t)) * np.sin(theta)
            return np.array([x, y, z])
        


        # DEFINICION OF THE TWO SOURCES
        fuente1=Dot(color=BLUE).shift(5*LEFT)
        fuente2=Dot(color=BLUE).shift(5*RIGHT)
        fuente1.time = 0
        fuente1.flashing = False
        fuente1.add_updater(begin_flashing)
        fuente2.time = 0
        fuente2.flashing = False
        fuente2.add_updater(begin_flashing)


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

        self.play(Create(fuente1),Create(fuente2))
        fuente1.flashing = True
        fuente2.flashing = True

        self.play(Create(params),Create(axes.x_axis),Create(axes.y_axis))

        self.wait()
               




        # MAKE IT 3D

        self.move_camera(phi=10 * DEGREES, theta=30 * DEGREES, gamma = 115 * DEGREES)

        self.play(Create(axes.z_axis))

        self.play(Rotate(axes, 2*PI, axis=RIGHT, about_point=ORIGIN),
                  Rotate(params, 2*PI, axis=RIGHT, about_point=ORIGIN),
                   run_time=2)
        
        self.wait()
        
        fuente1.flashing = False
        fuente2.flashing = False 

        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, gamma = 90 * DEGREES)

        self.play(Create(surfaces))

        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(3)
        self.stop_3dillusion_camera_rotation()
