from manim import *
import numpy as np

class ParametricSurface(ThreeDScene):
    

    def construct(self):
        self.camera.background_color = "#E2E2E2"


        """ BEGINING OF DECLARING FUNCTIONS AND UPDATERS """

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
                flash = Circle(radius=0.01).move_to(mobject.get_center()).set_color(BLUE)
                flash.radius = 0.01
                flash.add_updater(wave_updater)
                self.add(flash)
                mobject.time = 0   

        def func(t, theta, h=0, a=1, k=0, b=3):
            x = h + a / np.cos(t)
            y = (k + b * np.tan(t)) * np.cos(theta)
            z = (k + b * np.tan(t)) * np.sin(theta)
            return np.array([x, y, z])
        
        def wave(mobject, dt):

            def wave_function(t):
                return np.array((t,
                                 (1/1.54)*np.arctan(4*t)*A*np.sin(P * t - mobject.t_offset),
                                 0))
            
            mobject.t_offset += dt * mobject.phi

            A = mobject.amplitud
            P = mobject.periodo

            origin_coordinate = mobject.origin.get_center()
            target_coordinate = mobject.im_target.get_center()


            # Norm of the difference of the two points

            cartesian_distance = np.linalg.norm(target_coordinate - origin_coordinate)

            range = np.array([0, cartesian_distance])   

            # Get angle of rotation
            angle = np.arctan2(target_coordinate[1] - origin_coordinate[1],
                                 target_coordinate[0] - origin_coordinate[0])


            mobject.become(
                ParametricFunction(
                    wave_function,
                    t_range=range,
                    fill_opacity = 0)
                    .set_color(mobject.get_color())
                    .align_to(mobject.origin,LEFT)
                    .shift(RIGHT*0.1)
                    .set_y(mobject.origin.get_y())
                    .rotate(angle, about_point = mobject.origin.get_center())
            )

        def init_wave(from_origin, to_target):
            wave = ParametricFunction(lambda t: np.array((t,t,0))).set_color(BLACK)
            wave.amplitud = 0.8
            # Spacial frequency
            wave.periodo = 4
            # Temporal frequency
            wave.phi = 6
            # Phase offset
            wave.t_offset = 0
            wave.origin = Dot(color = BLACK).move_to(from_origin)
            wave.target = Dot(color = BLUE).move_to(to_target)
            wave.im_target = Dot(color = BLUE).move_to(to_target)
            return wave


        """ BEGINING OF DECLARING MOBJECTS """

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


        # DEFINICION OF THE TWO SOURCES
        fuente1=Dot(color=BLUE).shift(5*LEFT)
        fuente2=Dot(color=BLUE).shift(5*RIGHT)
        fuente1.time = 0
        fuente1.flashing = False
        fuente1.add_updater(begin_flashing)
        fuente2.time = 0
        fuente2.flashing = False
        fuente2.add_updater(begin_flashing)


        # DEFINICION OF THE WAVES
        wave1 = init_wave(fuente1.get_center(), ORIGIN)        
        wave1.add_updater(wave)
        
        wave2 = init_wave(fuente2.get_center(), ORIGIN)
        wave2.t_offset = PI
        wave2.add_updater(wave)


        

        surfaces = VGroup()
        params = VGroup()

        negative_surfaces = VGroup()
        negative_functions = VGroup()
        positive_surfaces = VGroup()
        positive_functions = VGroup()
        

        
        colors = [RED, BLACK]

        for i in range (-3,4):
            t = 1.1

            surface = Surface(
                lambda u, v: axes.c2p(*func(u, v, a = i)),
                u_range=[0, t],
                v_range=[-PI, PI],
                color=colors[i%2],
                resolution=(4, 4)
            ).set_style(fill_opacity=0.2).set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (RED, 0), (RED, 0.5)], axis=2)

            # Make a 2d version of the surface
            param = ParametricFunction(
                lambda t: axes.c2p(*func(t, 0, a=i)),
                t_range=[-t, t],
                color=colors[i%2]
            )
            if i%2 == 0:
                positive_surfaces.add(surface)
                positive_functions.add(param)
            else:
                negative_surfaces.add(surface)
                negative_functions.add(param)
                
            
        surfaces.add(positive_surfaces,negative_surfaces)
        params.add(positive_functions,negative_functions)



        self.add(axes)


        self.play(Create(fuente1),Create(fuente2))
        fuente1.flashing = True
        fuente2.flashing = True


        self.play(Create(params),Create(axes.x_axis),Create(axes.y_axis))

        self.wait()

        fuente1.flashing = False
        fuente2.flashing = False

        self.wait()

        self.play(Create(wave1),
                  Create(wave1.origin),
                  Create(wave1.im_target),
                  Create(wave2),
                  Create(wave2.origin),
                  Create(wave2.im_target),)

        self.play(wave1.im_target.animate.move_to(params[1].get_bottom()),
                  wave2.im_target.animate.move_to(params[1].get_bottom()),
        )
        wave1.phi = 0
        wave2.phi = 0

        self.play(MoveAlongPath(wave1.im_target, params[1][1], interpolate_mobject=0.3),
                  MoveAlongPath(wave2.im_target, params[1][1]),
                   run_time = 5)

        self.play(wave1.im_target.animate.move_to(ORIGIN),
                  wave2.im_target.animate.move_to(ORIGIN),
        )

        self.wait(3)
               




        # MAKE IT 3D

        # self.move_camera(phi=10 * DEGREES, theta=30 * DEGREES, gamma = 115 * DEGREES)

        # self.play(Create(axes.z_axis))

        # self.play(Rotate(axes, 2*PI, axis=RIGHT, about_point=ORIGIN),
        #           Rotate(params, 2*PI, axis=RIGHT, about_point=ORIGIN),
        #            run_time=2)
        
        # self.wait()
        
        # fuente1.flashing = False
        # fuente2.flashing = False 

        # self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, gamma = 90 * DEGREES)

        # self.play(Create(surfaces))

        # self.begin_3dillusion_camera_rotation(rate=2)
        # self.wait(3)
        # self.stop_3dillusion_camera_rotation()
