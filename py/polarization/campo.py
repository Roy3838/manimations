"""First we are going to define a class LightVector(Arrow):
    This is the general case where we have a vector that oscilates in a given axis.
    It can be the B or E field. Or any subcomponent of them.

    Axis can be a vector in the xy plane and it propagates in the z plane

"""


from manim import *


class LightVector(Vector):
    def __init__(
        self,
        axis=UP,
        amplitude=2,
        frequency=0.5,
        phase=0,
        propagation_speed=1,
        pathcolor=BLUE,
        opacity=1,
        **kwargs
        ):


        self.axis = axis
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.propagation_speed = propagation_speed
        self.pathcolor = pathcolor
        self.opacity = opacity
        self.time = 0
        # Create Dot that follows the tip of the vector
        self.tip_dot = Dot(self.get_vector().get_end(), color=self.color)

        # Create TracedPath attached to the Dot
        self.path = TracedPath(self.tip_dot.get_center, 
                               stroke_color=self.pathcolor, stroke_width=2, 
                               dissipating_time=5,stroke_opacity = self.opacity)

        super().__init__(**kwargs)
        self.add_updater(self.update)

    def update(self, dt):
        self.time += dt
        self.become(self.get_vector())  # Keep the vector static
        self.tip_dot.move_to(self.get_vector().get_end())  # Move Dot to vector tip
        self.path.shift([-0, 0, -self.propagation_speed * dt])  # Move the TracedPath backwards in the z-direction

    def get_vector(self):
        return Vector(
            self.axis * self.amplitude * np.sin(2 * PI * self.frequency * self.time + self.phase),
            color=self.color,
            buff=0,
        ).set_opacity(self.opacity)

class LightVectorScene(ThreeDScene):
    def construct(self):

        e_field = LightVector(
            pathcolor=BLUE,
            color=BLUE,
        )

        b_field = LightVector(
            axis=RIGHT,
            pathcolor=RED,
            color=RED,
        )
        self.camera.background_color = "#E2E2E2"

        axes = ThreeDAxes(
            x_length=6,
            y_length=6,
            z_length=10,
        ).set_color(BLACK)


        # Now the good stuff
        study_field = LightVector(
            axis=RIGHT+UP,
            pathcolor=BLUE,
            color=BLUE,
        )

        sub_x_field = LightVector(
            axis=RIGHT,
            pathcolor=BLUE,
            color=BLUE,
            opacity = 0.5,
        )

        sub_y_field = LightVector(
            axis=UP,
            pathcolor=BLUE,
            color=BLUE,
            opacity = 0.5,
        )

        self.play(Create(axes))
        self.add(e_field, b_field)
        self.add(e_field.path, b_field.path)  # Add traced paths

        self.move_camera(phi = 45*DEGREES, theta= (-15+90)* DEGREES,gamma = (270-15/2)* DEGREES, distance = 10, run_time = 2)

        
        
        self.wait(2)  # Wait for 10 seconds
        self.remove(e_field, e_field.path, b_field, b_field.path)

        self.add(sub_x_field, sub_y_field)
        self.wait(2)

        self.add(study_field)

        self.wait(2)  # Wait for 10 seconds




