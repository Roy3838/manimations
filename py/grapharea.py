from manim import *


class LineArea(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5], y_range=[0, 3, 1], axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)

        def func(x):
            return 1/2 * x 
        graph = ax.plot(func, color=MAROON)

        curve_2 = ax.plot(
            lambda x: 0.000001*x,
        )

        curve_1 = ax.plot(lambda x: 1/2*x)


        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        area = ax.get_area(curve_1, [0, t.get_value()],bounded_graph=curve_2, color=GREY, opacity=0.5)
        area.add_updater(lambda a: a.become(ax.get_area(curve_1, [0, t.get_value()],bounded_graph=curve_2, color=GREY, opacity=0.5)))

        self.add(ax, labels, graph, dot,area)
        self.play(t.animate.set_value(3))
        self.wait()

class ConstantArea(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5], y_range=[0, 12, 1], axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        

        t = ValueTracker(0)

        #time=Text('t=' + str(t.get_value()), color=BLUE).shift(UP + RIGHT)
        #time.add_updater(lambda time: time.set_text('t=' + str(t.get_value())))

        def text(mobject):
            mobject.set_value(t.get_value())

        label=DecimalNumber().move_to(UP*3 + RIGHT*3)
        label.add_updater(text)
        labeltext=MathTex("\\text{t=}").move_to(label.get_left() + LEFT*0.5)
        textcompleto=VGroup(labeltext,label)

        def func(x):
            return 0.0000001*x + 9.81
        graph = ax.plot(func, color=BLUE)

        curve_2 = ax.plot(
            lambda x: 0.000001*x + 9.81,
        )

        curve_1 = ax.plot(lambda x: 0.0000001*x)


        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        area = ax.get_area(curve_1, [0, t.get_value()],bounded_graph=curve_2, color=GREY, opacity=0.5)
        area.add_updater(lambda a: a.become(ax.get_area(curve_1, [0, t.get_value()],bounded_graph=curve_2, color=GREY, opacity=0.5)))
        
        
        self.play(Create(ax))
        self.play(Write(labels))
        self.play(Create(graph))
        self.play(Create(dot))
        self.play(Write(textcompleto))
        self.play(t.animate.set_value(4),run_time=2)
        self.wait(0.5)
        self.play(t.animate.set_value(1),run_time=2)
        self.wait(0.5)
        self.play(t.animate.set_value(0))
        self.wait()
        self.add(area)
        self.play(t.animate.set_value(3),run_time=2)
        self.wait(0.5)
        self.play(t.animate.set_value(4),run_time=2)
        self.wait()