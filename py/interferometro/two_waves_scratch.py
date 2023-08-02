from manim import *



class TwoWavesDistance(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        wave1 = ParametricFunction(lambda t: np.array((t,t,0))).set_color(BLACK)
        wave1.amplitud = 0.8
        wave1.periodo = 8
        wave1.phi = 10
        wave1.t_offset = 0
        wave1.origin = Dot(color = BLACK).move_to(LEFT*3)
        wave1.target = Dot(color = BLUE).move_to(RIGHT*3)

        wave2 = ParametricFunction(lambda t: np.array((t,t,0))).set_color(BLACK)
        wave2.amplitud = 0.8
        wave2.periodo = 8
        wave2.phi = 10
        wave2.t_offset = 0
        wave2.origin = Dot(color = BLACK).move_to(LEFT*3)
        wave2.target = Dot(color = BLUE).move_to(RIGHT*3)
        
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
                    .align_to(mobject.origin,LEFT)
                    .set_y(mobject.origin.get_y())
                )
            
            # Move target point to evaluation point of parametric curve
            x = range[1]
            y = wave_function(x)[1] + mobject.origin.get_y()
            mobject.target.move_to([mobject.target.get_x(), y, 0])
            
        wave1.add_updater(wave_updater)
        wave2.add_updater(wave_updater)

        self.add(wave1,wave1.origin,wave1.target,wave2,wave2.origin,wave2.target)
        self.play(wave1.origin.animate.shift(UP*2), wave2.origin.animate.shift(DOWN*2))

        self.play(wave1.origin.animate.shift(LEFT*3),
                  wave1.target.animate.shift(LEFT*3),
                  wave2.origin.animate.shift(LEFT*3),
                  wave2.target.animate.shift(LEFT*3))

        self.wait()

        self.play(wave1.target.animate.shift(RIGHT), wave2.target.animate.shift(LEFT))
        
        self.wait(2)

        