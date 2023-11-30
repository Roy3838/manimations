# Updated EnergyGraph class with more sp# Updated EnergyGraph class with more spaced out E0 and E1 lines and updated arrow positions
from manim import *



class EnergyGraph(Scene):
    def construct(self):
        # Adjusting the background color and axes
        self.camera.background_color = "#D4E1E1"
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 10, 1],
            x_length=7,
            y_length=5,
            axis_config={"color": BLACK}
        )

        # Label for y-axis
        y_label = axes.get_y_axis_label("Energy").set_color(BLACK)

        # Adjusted positions for Energy lines E0 and E1
        e0_y_value = 2  # Position of E0 line on the y-axis, adjust as needed
        e1_y_value = 8  # Position of E1 line on the y-axis, adjust as needed
        e0_line = Line(start=axes.c2p(0, e0_y_value), end=axes.c2p(5, e0_y_value), color=GREY_C)
        e1_line = Line(start=axes.c2p(0, e1_y_value), end=axes.c2p(5, e1_y_value), color=GREY_C)

        # Arrows with adjusted positions based on E0 and E1 values
        stroke = 8  # Arrow stroke width
        arrow_up = Arrow(start=axes.c2p(1, e0_y_value), end=axes.c2p(1, (e0_y_value + e1_y_value)/2), stroke_width=stroke, buff=0).set_color(RED)
        arrow_up = Arrow(start=axes.c2p(1, e0_y_value), end=axes.c2p(1, (e1_y_value)), stroke_width=stroke, buff=0).set_color(RED)
        #arrow_up_2 = Arrow(start=axes.c2p(1, (e0_y_value + e1_y_value) / 2), end=axes.c2p(1, e1_y_value), stroke_width=stroke, buff=0).set_color(RED)

        # Updated for loop for creating a sequence of three arrows with varying lengths, changing from big-medium-small to small-medium-big

        N = 6  # Number of sets, adjust as needed
        arrow_spacing = 0.5  # Spacing between each set of arrows
        start_x = 2  # Starting x position for the first set, adjust as needed
        stroke = 8  # Arrow stroke width

        total_length = e1_y_value - e0_y_value

        for i in range(-2,N-2):
            x_position = start_x + i * arrow_spacing

            # Gradually adjust the lengths of the arrows
            arrow_down_1_length = total_length / 3 + (i / (N - 1)) * (total_length / 3)
            arrow_down_3_length = total_length / 3 - (i / (N - 1)) * (total_length / 3)
            arrow_down_2_length = total_length - arrow_down_1_length - arrow_down_3_length

            # Create the arrows
            arrow_down_1 = Arrow(start=axes.c2p(x_position, e1_y_value), end=axes.c2p(x_position, e1_y_value - arrow_down_1_length), stroke_width=stroke, buff=0).set_color(GOLD)
            arrow_down_2 = Arrow(start=axes.c2p(x_position, e1_y_value - arrow_down_1_length), end=axes.c2p(x_position, e1_y_value - arrow_down_1_length - arrow_down_2_length), stroke_width=stroke, buff=0).set_color(GOLD)
            arrow_down_3 = Arrow(start=axes.c2p(x_position, e1_y_value - arrow_down_1_length - arrow_down_2_length), end=axes.c2p(x_position, e0_y_value), stroke_width=stroke, buff=0).set_color(GOLD)

            # Shift the three arrows right
            arrow_down_1.shift(RIGHT)
            arrow_down_2.shift(RIGHT)
            arrow_down_3.shift(RIGHT)


            # Add arrows to the scene
            self.add(arrow_down_1, arrow_down_2, arrow_down_3)





        # Add everything to the scene
        self.add(axes, y_label, e0_line, e1_line, arrow_up)#, arrow_up_2)
