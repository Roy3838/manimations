from manim import *

width = 1080
height = 1920
config.frame_size = [width, height]

class CompareCreditCardInterestAnimation(Scene):
    def construct(self):
        spending_data1 = [1, 13, 0, 4, 1, 3, 4, 1, 2, 9, 1, 3, 0, 1, 14, 4]

        animation1 = self.create_animation(spending_data1, "Random Spending")

        animation1.to_edge(UP)

        self.play(Create(animation1))
        self.wait()

        self.animate_interest(animation1)

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

        title = Text(title).scale(0.6).next_to(axes, UP*3)
        x_label = Text("Days").scale(0.4).next_to(axes.x_axis, DOWN)
        y_label = Text("Daily Expenses ($)").scale(0.4).next_to(axes.y_axis, LEFT).rotate(90 * DEGREES)

        return VGroup(axes, bars, x_label, y_label)

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
            self.play(rectangle.animate.move_to(UP*(0.2*i + 3) + [rectangle.get_center()[0], 0, 0]), run_time=0.5)
            
            right_shifted_rectangles = VGroup()
            for j in range(len(interest_bars) - i):
                new_rect = rectangle.copy()
                new_rect.move_to(rectangle.get_center() + RIGHT * 0.4 * j)
                right_shifted_rectangles.add(new_rect)
            
            self.play(Create(right_shifted_rectangles), run_time=0.5)
            accumulation.add(right_shifted_rectangles)

        # # Sum up all red rectangles
        # total_interest = VGroup(*[rect.copy() for rect in accumulation])
        # target_height = sum(rect.height for rect in total_interest)
        # target_width = bars.width
        #
        # summed_rectangle = Rectangle(
        #     height=target_height,
        #     width=target_width,
        #     fill_opacity=0.8,
        #     color=RED
        # ).next_to(bars, RIGHT, buff=1)
        #
        # self.play(
        #     total_interest.animate.arrange(DOWN, buff=0).move_to(summed_rectangle),
        #     run_time=1.5
        # )
        # self.play(ReplacementTransform(total_interest, summed_rectangle), run_time=1)
        #
        # total_interest_text = Text("Total Interest").scale(0.4).next_to(summed_rectangle, UP)
        # self.play(Write(total_interest_text))

        self.wait(2)
