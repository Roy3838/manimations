from manim import *






class helperMatrix(Scene):
    def construct(self):

        self.camera.background_color = "#E2E2E2"

        t0 = MathTable(
            [[r"\Delta d = 0",r"\Delta d = \frac{\lambda}{2}"],
             [r"\Delta d = \lambda",r"\Delta d = \frac{3\lambda}{2}"],
             [r"\Delta d = 2\lambda",r"\Delta d = \frac{5\lambda}{2}"],
             ["...", "..."]
            ],
            col_labels=[Text("+"), Text("-")],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": BLACK})
        t0.scale(0.5).set_color(BLACK)


        self.add(t0[0][0])
        self.wait(1)
        self.play(Write(t0[0][1]))
        self.wait(1)
        self.play(Write(t0[0][2]))
        self.wait(1)
        self.play(Write(t0[0][3]))
        self.wait(1)
        self.play(Write(t0[0][4]))
        self.wait(1)
        self.play(Write(t0[0][5]))
        self.wait(1)
        self.play(Write(t0[0][6]))
        self.wait(1)
        self.play(Write(t0[0][7]))
        self.wait(1)
        self.play(Write(t0[0][8]))
        self.wait(1)
        self.play(Write(t0[0][9]))

