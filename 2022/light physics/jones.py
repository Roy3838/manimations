from manim import *

class SineWaveX(ParametricFunction):
    def __init__(self, t_value, **kwargs):
        self.t_value = t_value
        super().__init__(self.sine_wave_function, **kwargs)

    def sine_wave_function(self, z):
        y = np.sin(z - self.t_value.get_value())
        return np.array([0, y, z])
    
class SineWaveY(ParametricFunction):
    def __init__(self, t_value, **kwargs):
        self.t_value = t_value
        super().__init__(self.sine_wave_function, **kwargs)

    def sine_wave_function(self, z):
        x = np.sin(z - self.t_value.get_value())
        return np.array([x, 0, z])


class Jones(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        # Create the axes
        axes = ThreeDAxes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            z_range=(-5, 5, 1),
            x_length=4,
            y_length=4,
            z_length=8,
            axis_config={"color": BLACK},
        )
        
        # Add labels to the axes
        x_label = Tex("x").next_to(axes, RIGHT).set_color(BLACK).scale(0.6)
        y_label = Tex("y").next_to(axes, UP).set_color(BLACK).scale(0.6)
        z_label = Tex("z").next_to(axes, OUT).set_color(BLACK).scale(0.6)

        self.play(Create(axes), Write(x_label), Write(y_label))
        #self.move_camera(phi=80 * DEGREES, theta=70 * DEGREES) # phi polar theta azimuthal
        self.move_camera(phi=80 * DEGREES, theta=70 * DEGREES, gamma=270 * DEGREES)

        self.play(Write(z_label))
        self.wait()
        
        t_value = ValueTracker(0)

        # Create the sine wave
        sine_wave = SineWaveX(t_value, t_range=[-5,5], color="#411C06")
        second_sin_wave = SineWaveY(t_value, t_range=[-5,5], color=GOLD)

        self.play(Create(sine_wave),Create(second_sin_wave))
        self.wait()
        
        def update_sine_wave(sine_wave, dt):
            t_value.increment_value(0.1)
            sine_wave.become(SineWaveX(t_value, t_range=[-5,5], color="#411C06"))
            second_sin_wave.become(SineWaveY(t_value, t_range=[-5,5], color=GOLD))
            

        sine_wave.add_updater(update_sine_wave)
        self.add(sine_wave)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(6)

        #self.wait()
        