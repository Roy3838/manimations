from manim import *





class EulerFinal(MovingCameraScene):
    def construct(self):

        
        frac = MathTex(r"\frac{dx}{dt}" , r"  \Delta ").shift(UP*2)

        frac1 = MathTex(r"dx", r"\rule{5mm}{0.3mm} ", r"dt").shift(DOWN)

        #frac1[1].move_to(frac1[0].get_center())

        self.add(NumberPlane())
        self.play(Write(frac))
        self.play(Write(frac1))

        self.play(frac1[0].animate.shift(DOWN), frac1[1].animate.shift(RIGHT))
        self.wait(4)



