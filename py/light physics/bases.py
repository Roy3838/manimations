from manim import *


class Bases(ThreeDScene):
    def construct(self):

        self.camera.background_color = "#E2E2E2"
        """
        A Scene that explains how from orthogonal linear bases you can get the resulting elipse, and when using 
        orthogonal circular bases you can get the elipse too.
        
        """

        # Axes

        axes = ThreeDAxes()
        axes.set_color(BLACK)
        z = 0.05
        plane1 = Polyhedron(vertex_coords=[axes.c2p(0, 0, z),
                                    axes.c2p(0, 3, z),
                                    axes.c2p(3, 3, z),
                                    axes.c2p(3, 0, z)],
                                    faces_list=[[0, 1, 2, 3]],
                                    )

        # Plane 2 at oposite end of the x axis
        plane2 = Polyhedron(vertex_coords=[axes.c2p(0, 0, z),
                                    axes.c2p(0, -3, z),
                                    axes.c2p(-3, -3, z),
                                    axes.c2p(-3, 0, z)],
                                    faces_list=[[0, 1, 2, 3]],)

        plane1.faces.set_fill(opacity=0.2)
        plane2.faces.set_fill(opacity=0.2)


        # Dot that oscilates as a line on the plane
        param1= ValueTracker(0)
        param2= ValueTracker(0)
        phase_shift1 = ValueTracker(0)
        phase_shift2 = ValueTracker(0)

        Dot1 = Dot(radius=0.08, color=BLACK)
        Dot2 = Dot(radius=0.08, color=BLACK)

        Dot_suma = Dot(radius=0.08, color=BLACK)

        Line1 = Line(axes.c2p(0, 0, 0), axes.c2p(0, 0, 0), color=GREY,stroke_width=1)
        Line2 = Line(axes.c2p(0, 0, 0), axes.c2p(0, 0, 0), color=GREY,stroke_width=1)

        # Dot1.move_to(axes.c2p(1.5, 1.5, 0))
        # Dot2.move_to(axes.c2p(-1.5, -1.5, 0))

        # Linear bases combination updaters
        Dot1.add_updater(lambda m: m.move_to(axes.c2p(np.cos(param1.get_value() + phase_shift1.get_value()) + 1.5, 1.5, 0)))
        Dot2.add_updater(lambda m: m.move_to(axes.c2p(-1.5, np.cos(param2.get_value() + phase_shift2.get_value()) - 1.5, 0)))
        Dot_suma.add_updater(lambda m: m.move_to(axes.c2p(np.cos(param1.get_value() + phase_shift1.get_value()) + 1.5, np.cos(param2.get_value() + phase_shift2.get_value()) - 1.5, 0)))
                
        # Universal Line Updaters
        Line1.add_updater(lambda m: m.put_start_and_end_on(Dot1.get_center(),Dot_suma.get_center()) )
        Line2.add_updater(lambda m: m.put_start_and_end_on(Dot2.get_center(),Dot_suma.get_center()) )

        self.curve1 = VGroup()
        self.curve2 = VGroup()

        self.path1 = TracedPath(Dot1.get_center, stroke_color=RED, stroke_width=2,dissipating_time=1.8)
        self.path2 = TracedPath(Dot2.get_center, stroke_color=BLUE, stroke_width=2,dissipating_time=1.8)
        self.path_suma = TracedPath(Dot_suma.get_center, stroke_color=GREEN, stroke_width=2,dissipating_time=1.8)

        
        self.set_camera_orientation(phi=40 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes))
        self.play(Create(plane1.faces))
        self.play(Create(plane2.faces))
        self.play(Create(Dot1))
        self.play(Create(Dot2))
        self.play(Create(Dot_suma))
        self.play(Create(Line1))
        self.play(Create(Line2))
        self.play(Create(self.path1), Create(self.path2), Create(self.path_suma))
        self.play(param1.animate.set_value(4*PI), param2.animate.set_value(4*PI), rate_func=linear, run_time=5)
        self.play(phase_shift1.animate.set_value(PI/2), rate_func=linear, run_time=1)
        self.play(param1.animate.set_value(8*PI), param2.animate.set_value(8*PI), rate_func=linear, run_time=5)

        self.wait()

        # Remove updaters
        phase_shift1.set_value(0)
        Dot1.clear_updaters()
        Dot2.clear_updaters()
        Dot_suma.clear_updaters()

        # Circular bases combination updaters
        Dot1.add_updater(lambda m: m.move_to(axes.c2p(np.cos(param1.get_value() + phase_shift1.get_value()) + 1.5, np.sin(param1.get_value() + phase_shift1.get_value()) + 1.5, 0)))
        Dot2.add_updater(lambda m: m.move_to(axes.c2p(np.cos(-param2.get_value() + phase_shift2.get_value()) - 1.5, np.sin(-param2.get_value() + phase_shift2.get_value()) - 1.5, 0)))

        # 
        Dot_suma.add_updater(lambda m: m.move_to(axes.c2p(np.cos(param1.get_value() + phase_shift1.get_value()) 
                                                          + 1.5, np.sin(-param2.get_value() + phase_shift2.get_value()) - 1.5,0)))


        self.play(param1.animate.set_value(12*PI), param2.animate.set_value(12*PI), rate_func=linear, run_time=5)
        self.play(phase_shift1.animate.set_value(PI/2), rate_func=linear, run_time=1)
        self.play(param1.animate.set_value(16*PI), param2.animate.set_value(16*PI), rate_func=linear, run_time=5)

        self.play(param1.animate.set_value(12*PI), param2.animate.set_value(12*PI), rate_func=linear, run_time=5)
        self.play(phase_shift1.animate.set_value(PI/4), rate_func=linear, run_time=1)
        self.play(param1.animate.set_value(16*PI), param2.animate.set_value(16*PI), rate_func=linear, run_time=5)


        self.wait(3)



        # Set camera position
        

