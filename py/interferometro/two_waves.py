from manim import *



class TwoWavesDistance(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        # WAVES SECTION

        lambda0=0.785398163397*2*RIGHT

        def init_wave():
            wave = ParametricFunction(lambda t: np.array((t,t,0))).set_color(BLACK)
            wave.amplitud = 0.8
            wave.periodo = 4
            wave.phi = 6
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
        ).move_to(RIGHT*4)

        sum_arrow = Arrow()

        def sum_arrow_updater(mobject):
            # Calculate the magnitudes of the arrows for wave1 and wave2
            magnitude1 = wave1.arrow.get_end() - wave1.arrow.get_start()
            magnitude2 = wave2.arrow.get_end() - wave2.arrow.get_start()

            # Determine the start and end points of the sum arrow
            start_point = ORIGIN + RIGHT*2
            end_point = start_point + magnitude1 + magnitude2 

            # Update the sum arrow
            mobject.become(Arrow(start_point, end_point, buff=0).set_color(BLACK))

        sum_arrow.add_updater(sum_arrow_updater)

        curve = VGroup()
        curve_start = ORIGIN + RIGHT*2
        curve.add(Line(curve_start, curve_start))

        def curve_updater(mobject):
            last_line = mobject[-1]
            new_line = Line(last_line.get_end(), sum_arrow.get_end(), color=GREY)
            mobject.shift(RIGHT*0.01)
            mobject.add(new_line)

        curve.add_updater(curve_updater)

        # Brace Between Origin points section
        brace = BraceBetweenPoints(wave1.origin.get_center(), wave2.origin.get_center(), buff=0)
        brace.text = brace.get_text("d", buff=0.1)
        def brace_updater(mobject):
            point1 = [wave1.origin.get_x(), 0, 0]
            point2 = [wave2.origin.get_x(), 0 ,0]
            mobject.become(BraceBetweenPoints(point2, point1, buff=0).set_color(BLACK))
            mobject.text = mobject.get_text("d", buff=0.1).next_to(mobject, DOWN, buff=0.1).set_color(BLACK)

        brace.add_updater(brace_updater)

        
        self.add(wave1_group, wave2_group)

        self.play(wave1.origin.animate.shift(UP*2), wave2.origin.animate.shift(DOWN*2))

        self.play(wave1.origin.animate.shift(LEFT*3),
                  wave1.target.animate.shift(LEFT*3),
                  wave2.origin.animate.shift(LEFT*3),
                  wave2.target.animate.shift(LEFT*3))

        ogpos1 = wave1.origin.get_center()
        ogpos2 = wave2.origin.get_center()

        self.wait(2)

        self.play(wave1.origin.animate.shift(lambda0/4), wave2.origin.animate.shift(-lambda0/4))
        
        self.wait(2)

        self.play(wave1.origin.animate.shift(lambda0/4), wave2.origin.animate.shift(-lambda0/4))

        self.wait(2)

        self.play(FadeIn(ax), FadeIn(sum_arrow))
        self.add(curve)

        self.wait(2)

        self.play(wave1.origin.animate.shift(lambda0/4), wave2.origin.animate.shift(-lambda0/4))

        self.wait(2)

        wave1.phi = 0
        wave2.phi = 0

        # return to original position
        self.play(wave1.origin.animate.move_to(ogpos1), wave2.origin.animate.move_to(ogpos2))

        # good animation 

        wave1.phi = 12
        wave2.phi = 12

        self.play(
            wave1.origin.animate.shift(lambda0),
            wave2.origin.animate.shift(-lambda0),
            run_time=12,
            rate_func=linear
        )

        


        