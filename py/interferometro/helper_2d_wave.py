from manim import *


class TwoWavesDistance(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        # WAVES SECTION

        lambda0=0.785398163397*2*RIGHT

        def wave_updater(mobject, dt):

            def wave_function(t):
                return np.array((t,
                                 (1/1.54)*np.arctan(4*t)*A*np.sin(P * t - wave1.t_offset),
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


        def init_wave():
            wave = ParametricFunction(lambda t: np.array((t,t,0))).set_color(BLACK)
            wave.amplitud = 0.8
            wave.periodo = 4
            wave.phi = 6
            wave.t_offset = 0
            wave.origin = Dot(color = BLACK).move_to(LEFT*2)
            wave.target = Dot(color = BLUE).move_to(RIGHT*3)
            wave.im_target = Dot(color = BLUE).move_to(RIGHT*3)
            return wave

        wave1 = init_wave()

        
        wave1.add_updater(wave_updater)
        self.add(wave1.origin, wave1.target, wave1.im_target, wave1)

        self.play(wave1.origin.animate.shift(UP))
        self.play(wave1.im_target.animate.shift(DOWN))

        self.wait(4)

        