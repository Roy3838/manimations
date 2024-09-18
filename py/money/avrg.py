from manim import *
width=1080
height=1920
config.frame_size = [width, height]
class CompareCreditCardInterestAnimation(Scene):
    def construct(self):
        spending_data1 = [1, 3, 0, 4, 1, 3, 5, 5, 2, 8, 0, 0, 10, 0, 7]
        spending_data2 = [1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 11, 12, 13, 13]

        animation1 = self.create_animation(spending_data1, "Scenario 1: Gradual Increase")
        animation2 = self.create_animation(spending_data2, "Scenario 2: Consistent Spending")

        animation1.to_edge(UP)
        animation2.next_to(animation1, DOWN, buff=0.5)

        self.play(Create(animation1), Create(animation2))
        self.wait()

        self.animate_interest(animation1)
        self.animate_interest(animation2)

    def create_animation(self, spending_data, title):
        axes = Axes(
            x_range=[0, 16, 5],
            y_range=[0, 15, 5],
            axis_config={"color": BLUE},
            x_length=10,
            y_length=3
        ).add_coordinates()
        
        bars = VGroup(*[
            Rectangle(height=value * 0.1, width=0.3, fill_opacity=0.8, color=BLUE)
            for value in spending_data
        ])
        bars.arrange(RIGHT, buff=0.1, aligned_edge=DOWN)
        bars.next_to(axes.x_axis, UP, buff=0)

        title = Text(title).scale(0.6).next_to(axes, UP)
        x_label = Text("Days").scale(0.4).next_to(axes.x_axis, DOWN)
        y_label = Text("Amount ($)").scale(0.4).next_to(axes.y_axis, LEFT).rotate(90 * DEGREES)

        return VGroup(axes, bars, title, x_label, y_label)

    def animate_interest(self, animation):
        bars = animation[1]
        interest_bars = VGroup(*[
            Rectangle(
                height=bar.height * 0.2,
                width=bar.width,
                fill_opacity=0.8,
                color=RED
            ).next_to(bar, UP, buff=0)
            for bar in bars
        ])

        self.play(LaggedStartMap(GrowFromEdge, interest_bars, edge=DOWN))

        accumulation = VGroup()
        for i, rectangle in enumerate(interest_bars):
            if i == 0:
                accumulation.add(rectangle.copy())
                accumulation[0].next_to(bars, RIGHT, buff=0.5)
                self.play(ReplacementTransform(rectangle, accumulation[0]))
            else:
                accumulation.add(rectangle.copy())
                accumulation[i].move_to(accumulation[i-1].get_top() + [0, interest_bars[i].height / 2, 0])
                self.play(ReplacementTransform(rectangle, accumulation[i]), run_time=0.2)

        total_interest = sum([bar.height for bar in interest_bars])
        total_interest_text = Text(f"Total Interest: ${total_interest*10:.2f}").scale(0.4).next_to(accumulation, RIGHT)
        self.play(Write(total_interest_text))
        self.wait(1)
