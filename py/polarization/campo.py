"""First we are going to define a class LightVector(Arrow):
    This is the general case where we have a vector that oscilates in a given axis.
    It can be the B or E field. Or any subcomponent of them.

    Axis can be a vector in the xy plane and it propagates in the z plane

"""

from manim import *

DISSIPATING_TIME = 5
DEFAULT_VECTOR_COLOR = BLUE
DEFAULT_PATH_COLOR = BLUE
DEFAULT_OPACITY = 1

DISSIPATING_TIME = 5
DEFAULT_VECTOR_COLOR = BLUE
DEFAULT_PATH_COLOR = BLUE
DEFAULT_OPACITY = 1

"""Final Class Merging together LightBase and Light Vector, when given a base, it oscilates
in that base, when given two vectors, it gives the resulting vector"""

class OscillatingVector(Vector):
    def __init__(self, vectors=None,
        amplitude=2,
        frequency=0.5,
        phase=0,
        propagation_speed=1,
        pathcolor=BLUE,
        opacity=1, **kwargs):
        super().__init__(**kwargs)

        self.vectors = vectors if vectors else []
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.propagation_speed = propagation_speed
        self.pathcolor = pathcolor
        self.opacity = opacity

        self.create_tip_and_path()
        self.add_updater(self.update)

    def create_tip_and_path(self):
        self.tip_dot = Dot(color=DEFAULT_VECTOR_COLOR).set_opacity(DEFAULT_OPACITY)
        self.path = TracedPath(self.tip_dot.get_center, 
                               stroke_color=DEFAULT_PATH_COLOR, 
                               stroke_width=2, 
                               dissipating_time=DISSIPATING_TIME, 
                               stroke_opacity=DEFAULT_OPACITY)

    def update(self, dt, **kwargs):
        resultant_vector = self.get_vector()
        self.become(resultant_vector)
        self.tip_dot.move_to(resultant_vector.get_end())
        if len(self.vectors) > 0:
            self.path.shift([0, 0, -self.vectors[0].propagation_speed * dt])  # Using the first vector's speed as the reference.

    def get_vector(self):
        resultant = np.array([0.0, 0.0, 0.0])

        for vector in self.vectors:
            resultant += vector.get_vector().get_end()

        return Vector(resultant).set_color(self.color).set_opacity(self.opacity)

class LightBase(Vector):
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

    def update(self, dt, **kwargs):
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


class Combination(Vector):
    def __init__(
        self,
        vectors,
        pathcolor=BLUE,
        opacity=1,
        propagation_speed=1,
        phases = None,
        **kwargs
    ):
        super().__init__(**kwargs)


        self.pathcolor = pathcolor
        self.opacity = opacity
        self.propagation_speed = propagation_speed

        self.vectors = vectors if vectors else []
        
        # Initialize the phase trackers for each vector
        if phases is None:
            phases = [0] * len(self.vectors)
        
        self.phase_trackers = [ValueTracker(phase) for phase in phases]

        self.create_tip_and_path()
        self.add_updater(self.update)

    def create_tip_and_path(self):
        # Assuming the first vector is representative for settings like color
        first_vector = self.vectors[0] if self.vectors else None

        if not first_vector:
            raise ValueError("No vectors provided for creating tip and path.")

        # Create Dot that will be at the tip of the resultant vector
        self.tip_dot = Dot(color=first_vector.color).set_opacity(self.opacity)

        # Create TracedPath attached to the Dot
        self.path = TracedPath(
            self.tip_dot.get_center,
            stroke_color=self.pathcolor, 
            stroke_width=2,
            dissipating_time=5,
            stroke_opacity=self.opacity
        )
        
    def get_vector(self):
        resultant = np.array([0.0, 0.0, 0.0])

        for idx, vector in enumerate(self.vectors):
            # Update the phase of each vector using its phase tracker
            if hasattr(vector, 'phase'):
                vector.phase = self.phase_trackers[idx].get_value()
            resultant += vector.get_end()  # Use get_end directly since vector is of type Vector.

        return Vector(resultant).set_color(self.color).set_opacity(self.opacity)

    def update(self, dt, **kwargs):
        resultant_vector = self.get_vector()
        self.become(resultant_vector)  # Keep the vector static
        self.tip_dot.move_to(resultant_vector.get_end())  # Move Dot to the end of the resultant vector
        # Assuming a propagation speed; you can modify this as needed
        self.path.shift([0, 0, -self.propagation_speed * dt])  # Use propagation_speed from Combination directly.




class LightVectorScene(ThreeDScene):
    def construct(self):

        self.camera.background_color = "#E2E2E2"

        axes = ThreeDAxes(
            x_length=6,
            y_length=6,
            z_length=10,
        ).set_color(BLACK)

        x_field = LightBase(
            axis=UP,
            pathcolor=BLUE,
            color=BLUE,
        )

        y_field = LightBase(
            axis=RIGHT,
            pathcolor=RED,
            color=RED,
        )

        # Now we make a vector that has PI/2 phase
        y_field_shift = LightBase(
            axis=RIGHT,
            pathcolor=BLUE,
            color=BLUE,
            phase=PI,
        )


        self.play(Create(axes))
        self.add(x_field, y_field)
        self.add(x_field.path, y_field.path)  # Add traced paths

        self.move_camera(phi = 45*DEGREES, theta= (-15+90)* DEGREES,gamma = (270-15/2)* DEGREES, distance = 10, run_time = 2)

        self.wait(2)
        self.remove(y_field, y_field.path, x_field.path)

        self.wait()

        y_field.set_color(BLUE)
        x_field.opacity = 0.5
        y_field.opacity = 0.5

        self.play(Create(y_field))

        self.wait(2)

        diagonal_vector = OscillatingVector(vectors=[x_field, y_field], color=BLUE) 

        self.play(FadeIn(diagonal_vector), FadeIn(diagonal_vector.path))

        circular_vector = OscillatingVector(vectors=[x_field, y_field_shift], color=BLUE)

        self.wait(3)

        # Now we make a vector that has PI/2 phase
        y_field_shift = LightBase(
            axis=RIGHT,
            pathcolor=BLUE,
            color=BLUE,
            phase=PI,
        )

        

        self.move_camera(phi = 0*DEGREES, theta= (0)* DEGREES,gamma = (0)* DEGREES, distance = 10, run_time = 2)


        self.play(Transform(y_field, y_field_shift))

        self.add(circular_vector, circular_vector.path)
        

        self.wait(4)


        
        
        # self.wait(2) 
        # self.remove(x_field, x_field.path, y_field, y_field.path)

        # self.add(sub_x_field, sub_y_field)
        # self.wait(4)

        # self.add(diagonal_vector, diagonal_vector.path)

        # self.wait(4) 

        # self.remove(diagonal_vector, diagonal_vector.path, sub_x_field, sub_y_field)

        # self.add(sub_x_fieldshifted, y_field_shift)

        # self.wait(4)

        # self.add(omg_sumshifted, omg_sumshifted.path)

        # self.wait(4) 





