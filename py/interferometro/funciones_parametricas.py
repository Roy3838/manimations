from manim import *
import numpy as np

class InterferometerParametricSurface(ThreeDScene):
    

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

        analysispoint=Dot(color=BLACK)
        
        distance1=Line(fuente1,analysispoint).set_color(GOLD)
        distance2=Line(fuente2,analysispoint).set_color(GOLD)

        distance1.add_updater(lambda x: x.become(
            Line(fuente1,analysispoint).set_color(GOLD)
        ))
        distance2.add_updater(lambda x: x.become(
            Line(fuente2,analysispoint).set_color(GOLD)
        ))
        
        bracedis1=BraceBetweenPoints(fuente1.get_center(),analysispoint.get_center(),buff=0,color=BLACK)
        bracedis1.add_updater(lambda z: z.become(
            BraceBetweenPoints(fuente1.get_center(),analysispoint.get_center(),buff=0,color=BLACK)
        ))
        dis1label=MathTex(r"d_{1}", color=BLACK).move_to(bracedis1.get_center()+0.5*DOWN)
        dis1label.add_updater(lambda z: z.move_to(bracedis1.get_center()+0.5*DOWN))
        
        bracedis2=BraceBetweenPoints(analysispoint.get_center(),fuente2.get_center(),buff=0,color=BLACK)
        bracedis2.add_updater(lambda z: z.become(
            BraceBetweenPoints(analysispoint.get_center(),fuente2.get_center(),buff=0,color=BLACK)
        ))
        dis2label=MathTex(r"d_{2}", color=BLACK).move_to(bracedis2.get_center()+0.5*DOWN)
        dis2label.add_updater(lambda z: z.move_to(bracedis2.get_center()+0.5*DOWN))



        # DEFINICION OF THE WAVES
        wave1 = init_wave(fuente1.get_center(), ORIGIN)        
        wave1.add_updater(wave)
        
        wave2 = init_wave(fuente2.get_center(), ORIGIN)
        wave2.t_offset = PI
        wave2.add_updater(wave)


        formula_final= MathTex(
            r"\Delta d", r"=" ,r"\sqrt{y^{2}+\left(x_{0}-x\right)^{2}}" 
            ,r"-" ,r"\sqrt{y^{2}+\left(x_{0}+x\right)^{2}}", color=BLACK
            ).move_to(UP+LEFT*3).scale(0.5)
        
        el_cero = MathTex(r"0").move_to(formula_final[0].get_center()).set_color(BLACK).scale(0.5)
        l_2 = MathTex(r"\frac{\lambda}{2}").move_to(formula_final[0].get_center()).set_color(BLACK).scale(0.5)
        l = MathTex(r"\lambda").move_to(formula_final[0].get_center()).set_color(BLACK).scale(0.5)
        l3_2 = MathTex(r"\frac{3\lambda}{2}").move_to(formula_final[0].get_center()).set_color(BLACK).scale(0.5)
        l2 = MathTex(r"2\lambda").move_to(formula_final[0].get_center()).set_color(BLACK).scale(0.5)
        l5_2 = MathTex(r"\frac{5\lambda}{2}").move_to(formula_final[0].get_center()).set_color(BLACK).scale(0.5)

        vals = VGroup(el_cero,l_2,l,l3_2,l2,l5_2)

        t0 = MathTable(
            [[r"\Delta d = 0",r"\Delta d = \frac{\lambda}{2}"],
             [r"\Delta d = \lambda",r"\Delta d = \frac{3\lambda}{2}"],
             [r"\Delta d = 2\lambda",r"\Delta d = \frac{5\lambda}{2}"],
             ["...", "..."]
            ],
            col_labels=[Text("+"), Text("-")],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": BLACK})
        t0.scale(0.5).set_color(BLACK).move_to(LEFT*3+UP*3.5)
        

        surfaces = VGroup()
        params = VGroup()

        negative_surfaces = VGroup()
        negative_functions = VGroup()
        positive_surfaces = VGroup()
        positive_functions = VGroup()
        

        
        colors = [BLUE, BLACK]

        for i in range (-4,5):
            t = 1.1

            surface = Surface(
                lambda u, v: axes.c2p(*func(u, v, a = i)),
                u_range=[0, t],
                v_range=[-PI, PI],
                color=colors[i%2],
                resolution=(4, 4)
            ).set_style(fill_opacity=0.2).set_fill_by_value(axes=axes, colorscale=[(colors[i%2], -0.5), (colors[i%2], 0), (colors[i%2], 0.5)], axis=2)

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


        self.play(Create(fuente1),Create(fuente2))
        
        fuente1.flashing = True
        fuente2.flashing = True
        self.wait()

        self.move_camera(frame_center=UP*1.5)

        fuente1.flashing = False
        fuente2.flashing = False

        self.play(Create(t0))

        self.play(Write(formula_final))

        self.wait()

        self.play(Create(axes.x_axis),Create(axes.y_axis))

        self.wait(2)


        
        self.play(
            ReplacementTransform(t0[0][2],el_cero),
            ReplacementTransform(formula_final[0],el_cero),
            Create(params[0][2]),)
        

        self.wait(4)

        self.play(Write(analysispoint), Write(distance1), 
                  Write(distance2), Write(bracedis1), 
                  Write(dis1label), Write(bracedis2), 
                  Write(dis2label))


        self.play(analysispoint.animate.shift(DOWN*6), run_time=1)
        self.play(MoveAlongPath(analysispoint, params[0][2]), run_time=3)

        self.play(Unwrite(analysispoint), Unwrite(distance1), 
                  Unwrite(distance2), Unwrite(bracedis1), 
                  Unwrite(dis1label), Unwrite(bracedis2), 
                  Unwrite(dis2label))

        self.remove(formula_final[0])
        self.play(
            ReplacementTransform(t0[0][3],l_2),
            ReplacementTransform(el_cero,l_2),
            Create(params[1][2],))
        self.remove(el_cero)
        
        self.play(
            ReplacementTransform(t0[0][4],l),
            ReplacementTransform(l_2,l),
            Create(params[0][3]),)
        self.remove(l_2)
        
        self.play(
            ReplacementTransform(t0[0][5],l3_2),
            ReplacementTransform(l,l3_2),
            Create(params[1][3]),)
        self.remove(l)


        self.wait()

        self.play(
            Unwrite(t0),
            Unwrite(formula_final[1:]),
            Unwrite(l3_2),

            Create(params[0][0]),
            Create(params[0][1]),
            Create(params[0][4]),
            Create(params[1][0]),
            Create(params[1][1]),

        )

        # PLANES
        #xy plane for young
        xy_plane = Rectangle(width = 6, height = 4, fill_opacity = 0.2).set_color(GREY_C)


        self.move_camera(frame_center=ORIGIN)

        self.play(Create(xy_plane))

        self.wait()

        self.play(FadeOut(xy_plane))

        yz_plane = Rectangle(width = 8, height = 8, fill_opacity=0.2).set_color(GREY_C).rotate(PI/2, axis = UP).move_to(RIGHT*2)
            

       
               

        




        # MAKE IT 3D

        self.move_camera(phi=10 * DEGREES, theta=30 * DEGREES, gamma = 115 * DEGREES)

        self.play(Create(axes.z_axis))

        self.play(Rotate(axes, 2*PI, axis=RIGHT, about_point=ORIGIN),
                  Rotate(params, 2*PI, axis=RIGHT, about_point=ORIGIN),
                   run_time=2)
        
        self.wait()

        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, gamma = 90 * DEGREES)

        self.play(Create(surfaces))

        self.move_camera(phi=30 * DEGREES, theta=10 * DEGREES, gamma = 90 * DEGREES,rate_func=linear, run_time=2)
        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, gamma = 90 * DEGREES,rate_func=linear)

        
        self.move_camera(phi=90 * DEGREES, zoom=0.5)

        self.play(Create(yz_plane))

        self.wait(3)

        self.play(Create(xy_plane))

        self.move_camera(phi=30 * DEGREES, theta=10 * DEGREES, gamma = 90 * DEGREES,run_time=4)

        self.wait()

        self.play(FadeOut(yz_plane),FadeOut(xy_plane),FadeOut(surfaces),FadeOut(params),FadeOut(axes.z_axis),FadeOut(axes.y_axis),FadeOut(axes.x_axis),FadeOut(fuente1),FadeOut(fuente2))
