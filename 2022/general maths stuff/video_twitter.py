from manim import *
from manim.utils.rate_functions import ease_in_cubic, ease_in_out_quad, ease_in_quad, ease_in_sine, ease_out_back
from numpy import single
#test

#lol 
class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            axis_config={"color": BLACK},
            tips=False,
            x_range=[-5,12,1],
        )
        self.camera.background_color = "#E2E2E2"
        period_tracker=ValueTracker(0.0001)

        def func(x):
            return 3*np.sin(period_tracker.get_value()*x+10*period_tracker.get_value())

        axes_labels = axes.get_axis_labels().set_color(BLACK)
        sin_graph = axes.plot(func, color=BLUE,stroke_width=1,x_range=(-10,12,0.1))
        sin_graph.add_updater(
            lambda m: m.become(axes.plot(func, color=BLUE, stroke_width=1,x_range=(-10,12,0.1)))
        )
        
        # LOLASO

        # def dotongraph1(mobject):
        #     mobject.move_to(axes.c2p(1*spacing,func(1*spacing)))
        # def dotongraph2(mobject):
        #     mobject.move_to(axes.c2p(2*spacing,func(2*spacing)))
        # def dotongraph3(mobject):
        #     mobject.move_to(axes.c2p(3*spacing,func(3*spacing)))
        # def dotongraph4(mobject):
        #     mobject.move_to(axes.c2p(4*spacing,func(4*spacing)))
        # def dotongraph5(mobject):
        #     mobject.move_to(axes.c2p(5*spacing,func(5*spacing)))
        # def dotongraph6(mobject):
        #     mobject.move_to(axes.c2p(6*spacing,func(6*spacing)))
        # def dotongraph7(mobject):
        #     mobject.move_to(axes.c2p(7*spacing,func(7*spacing)))
        # def dotongraph8(mobject):
        #     mobject.move_to(axes.c2p(8*spacing,func(8*spacing)))
        # def dotongraph9(mobject):
        #     mobject.move_to(axes.c2p(9*spacing,func(9*spacing)))
        # def dotongraph10(mobject):
        #     mobject.move_to(axes.c2p(10*spacing,func(10*spacing)))
        # def dotongraph11(mobject):
        #     mobject.move_to(axes.c2p(11*spacing,func(11*spacing)))
        # def dotongraph12(mobject):
        #     mobject.move_to(axes.c2p(12*spacing,func(12*spacing)))
        # def dotongraph13(mobject):
        #     mobject.move_to(axes.c2p(13*spacing,func(13*spacing)))
        # def dotongraph14(mobject):
        #     mobject.move_to(axes.c2p(14*spacing,func(14*spacing)))
        # def dotongraph15(mobject):
        #     mobject.move_to(axes.c2p(15*spacing,func(15*spacing)))
        # def dotongraph16(mobject):
        #     mobject.move_to(axes.c2p(16*spacing,func(16*spacing)))
        # def dotongraph17(mobject):
        #     mobject.move_to(axes.c2p(17*spacing,func(17*spacing)))
        # def dotongraph18(mobject):
        #     mobject.move_to(axes.c2p(18*spacing,func(18*spacing)))
        # def dotongraph19(mobject):
        #     mobject.move_to(axes.c2p(19*spacing,func(19*spacing)))
        # def dotongraph20(mobject):
        #     mobject.move_to(axes.c2p(20*spacing,func(20*spacing)))
        # def dotongraph21(mobject):
        #     mobject.move_to(axes.c2p(21*spacing,func(21*spacing)))
        # def dotongraph22(mobject):
        #     mobject.move_to(axes.c2p(22*spacing,func(22*spacing)))
        # def dotongraph23(mobject):
        #     mobject.move_to(axes.c2p(23*spacing,func(23*spacing)))
        # def dotongraph24(mobject):
        #     mobject.move_to(axes.c2p(24*spacing,func(24*spacing)))
        # def dotongraph25(mobject):
        #     mobject.move_to(axes.c2p(25*spacing,func(25*spacing)))
        # def dotongraph26(mobject):
        #     mobject.move_to(axes.c2p(26*spacing,func(26*spacing)))
        # def dotongraph27(mobject):
        #     mobject.move_to(axes.c2p(27*spacing,func(27*spacing)))
        # def dotongraph28(mobject):
        #     mobject.move_to(axes.c2p(28*spacing,func(28*spacing)))
        # def dotongraph29(mobject):
        #     mobject.move_to(axes.c2p(29*spacing,func(29*spacing)))
        # def dotongraph30(mobject):
        #     mobject.move_to(axes.c2p(30*spacing,func(30*spacing)))

        # LOLASO
        
        # dot1=Dot(color=COLOR1).add_updater(dotongraph1)
        # dot2=Dot(color=COLOR2).add_updater(dotongraph2)
        # dot3=Dot(color=COLOR3).add_updater(dotongraph3)
        # dot4=Dot(color=COLOR4).add_updater(dotongraph4)
        # dot5=Dot(color=COLOR1).add_updater(dotongraph5)
        # dot6=Dot(color=COLOR2).add_updater(dotongraph6)
        # dot7=Dot(color=COLOR3).add_updater(dotongraph7)
        # dot8=Dot(color=COLOR4).add_updater(dotongraph8)
        # dot9=Dot(color=COLOR1).add_updater(dotongraph9)
        # dot10=Dot(color=COLOR2).add_updater(dotongraph10)
        # dot11=Dot(color=COLOR3).add_updater(dotongraph11)
        # dot12=Dot(color=COLOR4).add_updater(dotongraph12)
        # dot13=Dot(color=COLOR1).add_updater(dotongraph13)
        # dot14=Dot(color=COLOR2).add_updater(dotongraph14)
        # dot15=Dot(color=COLOR3).add_updater(dotongraph15)
        # dot16=Dot(color=COLOR4).add_updater(dotongraph16)
        # dot17=Dot(color=COLOR1).add_updater(dotongraph17)
        # dot18=Dot(color=COLOR2).add_updater(dotongraph18)
        # dot19=Dot(color=COLOR3).add_updater(dotongraph19)
        # dot20=Dot(color=COLOR4).add_updater(dotongraph20)
        # dot21=Dot(color=COLOR1).add_updater(dotongraph21)
        # dot22=Dot(color=COLOR2).add_updater(dotongraph22)
        # dot23=Dot(color=COLOR3).add_updater(dotongraph23)
        # dot24=Dot(color=COLOR4).add_updater(dotongraph24)
        # dot25=Dot(color=COLOR1).add_updater(dotongraph25)
        # dot26=Dot(color=COLOR2).add_updater(dotongraph26)
        # dot27=Dot(color=COLOR3).add_updater(dotongraph27)
        # dot28=Dot(color=COLOR4).add_updater(dotongraph28)
        # dot29=Dot(color=COLOR1).add_updater(dotongraph29)
        # dot30=Dot(color=COLOR2).add_updater(dotongraph30)

        # dots=VGroup(dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9,dot10,dot11,dot12,dot13,dot14,dot15,dot16,dot17,dot18,dot19,dot20,dot21,dot22,dot23,dot24,dot25,dot26,dot27,dot28,dot29,dot30)


        def dotongraph(mobject):
            x = mobject.get_x
            spacing = 0.3
            mobject.move_to(axes.c2p(x*spacing,func(x*spacing)))
        
        COLOR1="#87c2a5"
        COLOR2="#525893"
        COLOR3="#343434"
        COLOR4="#e07a5f"

        COLORS = [COLOR1,COLOR2, COLOR3, COLOR4]
        dots = VGroup()
        for i in range(30):
            dot = Dot(color=COLORS[i%4])
            dot.get_x = i
            dot.add_updater(dotongraph)
            dots.add(dot)
        

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, sin_graph), color=YELLOW, line_func=Line
        )

        plot = VGroup(axes, vert_line)
        labels = VGroup(axes_labels)
        

        self.add(plot,sin_graph, labels,dots)
        self.play(period_tracker.animate.set_value(1), run_time=4, rate_func=linear) 
        #self.play(period_tracker.animate.set_value(20), run_time=80, rate_func=linear)
        self.wait()
        



class Squish(Scene):
    def construct(self):
        amplitude_tracker=ValueTracker(10)
        axes = Axes(
            axis_config={"color": GREEN},
            tips=False,
            x_range=[-amplitude_tracker.get_value(),amplitude_tracker.get_value(),1]
        )
        axes.add_updater(lambda a: a.become(Axes(
            axis_config={"color": GREEN},
            tips=False,
            x_range=[-amplitude_tracker.get_value(),amplitude_tracker.get_value(),1]
        )))
        period_tracker=ValueTracker(0.01)
        

        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(np.abs(period_tracker.get_value()*x)), color=BLUE,stroke_width=1)
        sin_graph.add_updater(
            lambda m: m.become(axes.plot(lambda x: np.sin(np.abs(period_tracker.get_value()*x)), color=BLUE, stroke_width=1))
        )
        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, sin_graph), color=YELLOW, line_func=Line
        )

        plot = VGroup(axes, vert_line)
        labels = VGroup(axes_labels)
        
        self.add(plot, labels, sin_graph)
        self.play(period_tracker.animate.set_value(2), run_time=1) # exponential decay otra opcion
        self.wait()
        self.play(amplitude_tracker.animate.set_value(20))
        self.wait()
        self.play(period_tracker.animate.set_value(4), run_time=1)



class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))