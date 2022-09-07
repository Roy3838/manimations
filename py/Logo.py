from manim import *


config.pixel_width = 1920 
config.pixel_height = 1920

class Logo(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        LateX = MathTex("\\text{MC=}", color=GRAY_D)
        LateX2 = MathTex("\\text{E/c}", color=GRAY_D)
        LateX3 = MathTex(r"\frac{E}{c}", color=GRAY_D)

        Reuler=MathTex(r"\mathbb{R}euler", color=GRAY_D).scale(6)
        #self.play(Write(Reuler), run_time=2)\
        self.add(Reuler)


        # LateX.scale(3)
        # LateX2.scale(3)
        # LateX3.scale(3)
        # self.play(Write(LateX),run_time=3)
        # self.play(FadeOut(LateX),run_time=3)
        # self.wait(1)
        # self.play(Write(LateX2),run_time=3)
        # self.play(FadeOut(LateX2),run_time=3)
        # self.wait(1)
        # self.play(Write(LateX3),run_time=3)
        # self.play(FadeOut(LateX3),run_time=3)
        

