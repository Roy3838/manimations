# Updated EnergyGraph class with more sp# Updated EnergyGraph class with more spaced out E0 and E1 lines and updated arrow positions
from manim import *



class EnergyGraph(ThreeDScene):
    def construct(self):
        # Adjusting the background color and axes

        def func(t, theta, h=0, a=1, k=0, b=0.7):
            x = h + a / np.cos(t)
            y = (k + b * np.tan(t)) * np.cos(theta)
            z = (k + b * np.tan(t)) * np.sin(theta)
            return np.array([x, y, z])

        #2.5sin(t+cos(t)) + 4 + e^(-(t-3)^2), 2cos(t+sin(t)) + 3.5
        def func1(t):
            return np.array([
                2.5*np.sin(t+np.cos(t))+4-np.exp(-(t-3)**2),
                2*np.cos(t+np.sin(t))+2,
                0
            ])
        
        #\left(-2.5\sin\left(t+\cos\left(at\right)\right)\ +\ 3\ +\ e^{-\left(t-3\right)^{2}},-2\cos\left(t+\sin\left(at\right)\right)+4\right)
        def func2(t):
            return np.array([
                -2.5*np.sin(t+np.cos(t))+3+np.exp(-(t-3)**2),
                -2*np.cos(t+np.sin(t))+2.5,
                0
            ])

        self.camera.background_color = "#D4E1E1"
        axes = ThreeDAxes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            z_range=[0, 10, 1],
            axis_config={"color": BLACK}
        )

        axes.scale(0.6)


        # Label for y-axis
        y_label = axes.get_y_axis_label(r"\Delta_{s,i}").set_color(BLACK).rotate(-PI/2)
        x_label = axes.get_x_axis_label("w_p").set_color(BLACK)

        func1p = ParametricFunction(func1, t_range=[-2.8, 3], color=RED)
        func2p = ParametricFunction(func2, t_range=[-2.8, 3], color=RED)
        func1p.shift(LEFT*3+ 2*DOWN + OUT)
        func2p.shift(LEFT*3+ 2*DOWN + OUT)

        # Label the func1p and func2p as DK = 0
        dk1 = MathTex(r"\Delta_{s,i} = 0").set_color(BLACK)
        dk1.next_to(func1p, RIGHT*2)


        func3d = Surface(func, u_range=[0, 1.1], v_range=[-PI, PI], stroke_color=BLACK)
        func3d.set_fill_by_checkerboard(RED_A, RED_A, opacity=0.5)
        func3d.shift(LEFT*2)
        func3d.scale(3)
        z_label = axes.get_z_axis_label(r"\Delta_{r,s,i}").set_color(BLACK).shift(OUT)

        # Label func3d as DK = 0
        dk2 = MathTex(r"\Delta_{r,s,i} = 0").set_color(BLACK).next_to(func3d, OUT*2)




        # Place camera directly above the graph
        self.set_camera_orientation(phi=0, theta=-PI/2)
        # zoom slightly out


        # Add everything to the scene
        self.add(axes.x_axis, axes.y_axis, y_label, x_label)#, arrow_up_2)
        self.wait()
        self.play(Create(func1p))
        self.play(Create(func2p))
        self.wait()
        self.play(Create(dk1))
        self.wait()

        self.move_camera(phi=PI/4, theta=-PI/2)
        self.play(Create(axes.z_axis))
        self.play(ReplacementTransform(y_label, z_label))
        self.wait()

        self.play(Create(func3d), FadeOut(func1p), FadeOut(func2p))
        self.play(ReplacementTransform(dk1, dk2))
        self.begin_3dillusion_camera_rotation(rate=0.1)
        self.wait(3)