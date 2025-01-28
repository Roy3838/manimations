from manim import *

width=int(1080)
height=int(1920)
config.frame_size = [width, height]

class InterferometerDistance(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        self.camera.frame.scale(0.6)

        # WAVES SECTION

        lambda0=0.785398163397*2*RIGHT

        def init_wave():
            wave = ParametricFunction(lambda t: np.array((t,t,0))).set_color(BLACK)
            wave.amplitud = 0.8
            wave.periodo = 4
            wave.phi = 8
            wave.t_offset = 0
            wave.origin = Dot(color = BLACK).move_to(LEFT*2)
            wave.target = Dot(color = BLUE).move_to(RIGHT*3)
            wave.arrow = Arrow()
            return wave

        wave1 = init_wave()
        wave2 = init_wave()
        
        def wave_updater(mobject, dt):

            def wave_function(t):
                return np.array((t,
                                 (1/1.54)*np.arctan(4*t)*A*np.sin(P * t - wave1.t_offset),
                                 0))
            
            mobject.t_offset += dt * mobject.phi
            A = mobject.amplitud
            P = mobject.periodo
            range = np.array([0, np.abs(mobject.origin.get_x()-mobject.target.get_x())])            
            mobject.become(
                ParametricFunction(
                    wave_function,
                    t_range=range,
                    fill_opacity = 0)
                    .set_color(mobject.get_color())
                    .align_to(mobject.target,RIGHT)
                    .shift(LEFT*0.1)
                    .set_y(mobject.origin.get_y())
                )
            
            # Move target point Dot()
            x = range[1]
            y = wave_function(x)[1] + mobject.origin.get_y()
            mobject.target.move_to([mobject.target.get_x(), y, 0])

            # Move superposition Arrow()
            arrow_base = [mobject.target.get_x(), mobject.origin.get_y(), 0]
            mobject.arrow.become(
                Arrow(arrow_base, mobject.target.get_center(),buff=0)
                .set_color(BLACK)
                .shift(RIGHT))
            

        wave1.add_updater(wave_updater)
        wave2.add_updater(wave_updater)
        wave1_group = VGroup(wave1,wave1.origin,wave1.target,wave1.arrow)
        wave2_group = VGroup(wave2,wave2.origin,wave2.target,wave2.arrow)  
        
        # GRAPH SECTION
        ax= Axes(
            x_range=[0,4,1],
            y_range=[-2,2,1],
            x_length=4,
            y_length=4,
            axis_config={
                "color": BLACK,
                "stroke_width": 2,
                "include_tip": False,
            },
            tips=False,
        ).move_to(DOWN*7)

        def sum_arrow_updater(mobject):
            # Calculate the magnitudes of the arrows for wave1 and wave2
            magnitude1 = wave1.arrow.get_end() - wave1.arrow.get_start()
            magnitude2 = wave2.arrow.get_end() - wave2.arrow.get_start()

            # Determine the start and end points of the sum arrow
            start_point = mobject.start
            end_point = start_point + magnitude1 + magnitude2 

            # Update the sum arrow
            mobject.become(Arrow(start_point, end_point, buff=0).set_color(BLACK))


        sum_arrow = Arrow()
        sum_arrow.start = LEFT*2 + ax.get_center()
        sum_arrow.add_updater(sum_arrow_updater)

        curve = VGroup()
        curve.add(Line(sum_arrow.start, sum_arrow.start))

        def curve_updater(mobject):
            last_line = mobject[-1]
            new_line = Line(last_line.get_end(), sum_arrow.get_end(), color=GREY)
            mobject.shift(RIGHT*0.02)
            mobject.add(new_line)

        curve.add_updater(curve_updater)


        # Brace Between Origin points section
        brace = BraceBetweenPoints(wave1.origin.get_center(), wave2.origin.get_center(), buff=0).set_color(BLACK)
        brace.text = Tex("$\lambda/2$").set_color(BLACK).move_to(brace.get_bottom() +  DOWN, )

        def brace_updater(mobject):
            point1 = [wave1.origin.get_x(), -1, 0]
            point2 = [wave2.origin.get_x(), -1 ,0]
            mobject.become(BraceBetweenPoints(point2, point1, buff=0).set_color(BLACK))

        def text_updater(mobject):
            mobject.become(
                MathTex(mobject.text).set_color(BLACK).move_to(brace.get_bottom() +  DOWN, )
            )


        brace.add_updater(brace_updater)
        brace.text.add_updater(text_updater)

        
        self.add(wave1_group, wave2_group)

        self.play(wave1.origin.animate.shift(UP*2), wave2.origin.animate.shift(DOWN*2))

        # self.play(wave1.origin.animate.shift(LEFT*3),
        #           wave1.target.animate.shift(LEFT*3),
        #           wave2.origin.animate.shift(LEFT*3),
        #           wave2.target.animate.shift(LEFT*3))

        ogpos1 = wave1.origin.get_center()
        ogpos2 = wave2.origin.get_center()

        self.wait(5)

        self.play(wave1.origin.animate.shift(lambda0/4), 
                  wave2.origin.animate.shift(-lambda0/4),
                  )
        
        
        self.wait(4)

        wave1.phi = 16
        wave2.phi = 16

        self.play(self.camera.frame.animate.move_to(DOWN*4),)

        self.play(FadeIn(ax), FadeIn(sum_arrow))
        self.add(curve)

        # return to original position
        self.play(wave1.origin.animate.move_to(ogpos1), wave2.origin.animate.move_to(ogpos2))

        self.play(
            wave1.origin.animate.shift(lambda0),
            wave2.origin.animate.shift(-lambda0),
            run_time=3,
            rate_func=linear
        )
        self.play(
            wave1.origin.animate.shift(-lambda0),
            wave2.origin.animate.shift(lambda0),
            run_time=3,
            rate_func=linear
        )

        t0 = MathTable(
            [[r"\Delta d = 0",r"\Delta d = \frac{\lambda}{2}"],
             [r"\Delta d = \lambda",r"\Delta d = \frac{3\lambda}{2}"],
             [r"\Delta d = 2\lambda",r"\Delta d = \frac{5\lambda}{2}"],
             ["...", "..."]
            ],
            col_labels=[Text("+"), Text("-")],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": BLACK})
        t0.scale(0.5).set_color(BLACK).move_to(UP*5)

        self.play(Create(t0[0][0]), Create(t0[0][1]), Create(t0.get_vertical_lines()), Create(t0.get_horizontal_lines()))


        brace.text.text = r"\Delta d = 0"
        self.play(self.camera.frame.animate.move_to(LEFT*4),
                    wave2.origin.animate.shift(UP*2),
            Create(brace), Write(brace.text), FadeOut(curve), FadeOut(sum_arrow),FadeOut(ax))

        self.play(Write(t0[0][2]))
        self.wait()

        for i in range(1, 6):
            brace.text.text = rf"\Delta d = \frac{{{i}\lambda}}{{2}}"
            self.play(wave1.origin.animate.shift(lambda0/4), wave2.origin.animate.shift(-lambda0/4), run_time=0.5)
            self.play(Write(t0[0][i+2]),run_time=0.3)
            self.wait(0.8)
        self.play(Write(t0[0][8]), Write(t0[0][9]),run_time=0.3)


        


