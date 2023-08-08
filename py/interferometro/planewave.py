from manim import *


class TwoWavesDistance(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        # WAVES SECTION

        lambda0=0.785398163397*2*RIGHT

        def wave_updater(mobject, dt):

            def wave_function(t):
                x, y = t
                return np.array((x,
                                y + (1/1.54)*np.arctan(4*x)*A*np.sin(P * x - mobject.t_offset),
                                0))
                    
            mobject.t_offset += dt * mobject.phi
            A = mobject.amplitud
            P = mobject.periodo
            range_x = np.array([ np.abs(mobject.origin.get_x() - mobject.target.get_x())])
            range_y = np.array([mobject.origin.get_y()- mobject.target.get_y()])
            t_range = np.array()

            mobject.become(
                ParametricFunction(
                    wave_function,
                    t_range=t_range,
                    fill_opacity=0)
                    .set_color(mobject.get_color())
                    .align_to(mobject.target, RIGHT)
                    .shift(LEFT*0.1)
                )

            # Move target point Dot()
            x, y = range_x[1], range_y[1]
            target_y = wave_function([x, y])[1]
            mobject.target.move_to([mobject.target.get_x(), target_y, 0])

            # Move superposition Arrow()
            arrow_base = [mobject.target.get_x(), mobject.origin.get_y(), 0]
            mobject.arrow.become(
                Arrow(arrow_base, mobject.target.get_center(), buff=0)
                .set_color(BLACK)
                .shift(RIGHT))


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

        wave1.arrow = Arrow(wave1.origin.get_center(), wave1.target.get_center(), buff=0, color=BLACK)

        self.add(wave1.origin, wave1.target, wave1.arrow, wave1)
        wave1.add_updater(wave_updater)

        self.wait(4)

        