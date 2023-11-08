from manim import *

class BlochSphere(ThreeDScene):
    def construct(self): 
        # Background color
        self.camera.background_color = "#2D2D4D"

        # Create the axes
        axes = ThreeDAxes()  

        # Circle on XZ plane
        circle_xz = Circle(radius=2, color=WHITE, stroke_width=1).set_opacity(0.4)
        circle_xz.rotate(PI/2, axis=RIGHT)

        # Circle on YZ plane
        circle_yz = Circle(radius=2, color=WHITE, stroke_width=1).set_opacity(0.4)
        circle_yz.rotate(PI/2, axis=UP)

        # Circle on XY plane
        circle_xy = Circle(radius=2, color=WHITE, stroke_width=1.5)

        # Dashed circles
        dash_circle_xy = DashedVMobject(circle_xy, num_dashes=64)
        dash_circle_xz = DashedVMobject(circle_xz, num_dashes=64).set_opacity(0.4)
        dash_circle_yz = DashedVMobject(circle_yz, num_dashes=64).set_opacity(0.4)

        # Quantum State |ψ⟩ vector
        quantum_vector = Arrow3D(ORIGIN, [1,1.5,2], color=WHITE)
        
        # Labels
        label_psi = MathTex("|\\psi\\rangle").next_to(quantum_vector.get_end(), RIGHT)
        label_0 = Text("|0⟩").scale(0.8).next_to(axes.z_axis.get_end(), UP)
        label_1 = Text("|1⟩").scale(0.8).next_to(axes.z_axis.get_start(), DOWN)
        label_x = Text("X").scale(0.8).next_to(axes.x_axis.get_end(), DOWN)
        label_y = Text("Y").scale(0.8).next_to(axes.y_axis.get_end(), LEFT)
        label_theta = MathTex("\\theta").scale(0.8).move_to([1, 1.3, 1.5])
        label_phi = MathTex("\\phi").scale(0.8).move_to([1.2, 0.8, 0])

        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)  # Set a good camera view

        self.add(axes, dash_circle_xz, dash_circle_yz, dash_circle_xy, quantum_vector, label_psi, label_0, label_1, label_x, label_y, label_theta, label_phi)

        self.wait(5)  # Show the scene for 5 seconds

