from manim import *

width=1080
height=1920
config.frame_size = [width, height]

class BlochSphere(ThreeDScene):
    def construct(self): 

        # Background color
        self.camera.background_color ="#E2E2E2" 

        # Lines as Axes
        xLine = Line([0,0,0], [1.6,0,0], color=GREY_B, stroke_width=1.5).set_opacity(0.6)
        yLine = Line([0,0,0], [0,1.6,0], color=GREY_B, stroke_width=1.5).set_opacity(0.6)
        zLine = Line([0,0,-2], [0,0,2], color=GREY_B, stroke_width=1.5).set_opacity(0.6)
        axes = VGroup(xLine, yLine, zLine)


        # Circle on XZ plane
        circle_xz = Circle(radius=2, color=GREY_C, stroke_width=1).set_opacity(0.4)
        circle_xz.rotate(PI/2, axis=RIGHT)

        # Circle on YZ plane
        circle_yz = Circle(radius=2, color=GREY_C, stroke_width=1).set_opacity(0.4)
        circle_yz.rotate(PI/2, axis=UP)

        # Circle on XY plane
        circle_xy = Circle(radius=2, color=GREY_C, stroke_width=1.5)

        # Dashed circles
        dash_circle_xy = DashedVMobject(circle_xy, num_dashes=64)
        dash_circle_xz = DashedVMobject(circle_xz, num_dashes=64).set_opacity(0.4)
        dash_circle_yz = DashedVMobject(circle_yz, num_dashes=64).set_opacity(0.4)

        # Quantum State |ψ⟩ vector
        vector = [1.1,1.4,1]
        quantum_vector = Arrow3D(ORIGIN, vector, color=GREY_A,thickness=0.005).set_opacity(0.2)
        quantum_vector.cone.scale(0.5).set_opacity(0.2)

        # Dotted projection to z=0 plane
        projection_end = [vector[0], vector[1], 0]

        projection_line = DashedLine((quantum_vector.get_end()*1.125), projection_end, color=GREY_C, stroke_width=0.5)

        # Dotted projection onto XY plane
        projection_on_xy = DashedLine(projection_end, ORIGIN, color=GREY_C, stroke_width=0.5)
        
        # # Labels write \ket{Roy} and move to point of vector
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{physics}")
        label_roy = Tex(r"$\ket{Roy}$",tex_template=myTemplate, color=GREY_B).scale(0.75)
        # Label \ket{Quantum} to the top of the sphere
        label_quantum = Tex(r"$\ket{Quantum}$",tex_template=myTemplate, color=GREY_B).scale(0.5)
        # Label \ket{Computing}
        label_computing = Tex(r"$\ket{Computing}$",tex_template=myTemplate, color=GREY_B).scale(0.5)

        # Add label_roy to fixed_in_frame_mobjects
        self.add_fixed_in_frame_mobjects(label_roy, label_quantum, label_computing)
        label_roy.shift(RIGHT*2.5+DOWN*1.55)
        label_quantum.shift(UP*0.5+RIGHT*1.8)
        label_computing.shift(DOWN*3.5+RIGHT*1.8)



        # Adjust the camera's position
        #self.move_camera(frame_center=[0.5, 0.5, 0])


        self.set_camera_orientation(phi=80 * DEGREES, theta=15 * DEGREES)  # Set a good camera view
        # Move camera up and to the left




        group = VGroup(axes, dash_circle_xz, dash_circle_yz, dash_circle_xy, quantum_vector, 
                 #label_psi, label_0, label_1, label_x, label_y, label_theta, label_phi,
                 projection_line, projection_on_xy,
                 label_roy, label_quantum, label_computing)
        
        group.shift(4*IN+LEFT).scale(3).set_opacity(0.6)
        self.add(group)
        # self.begin_3dillusion_camera_rotation(rate=2)
        # self.wait(PI/2)
        # self.stop_3dillusion_camera_rotation()
