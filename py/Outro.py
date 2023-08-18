from manim import *


class Logo(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        LateX = MathTex("\\text{MC=}", color=GRAY_D)
        LateX2 = MathTex("\\text{E/c}", color=GRAY_D)
        LateX3 = MathTex(r"\frac{E}{c}", color=GRAY_D)

        Reuler=MathTex(r"\mathbb{R}euler" , r"\vec{S}",r"pac",r"\hat{e}", color=GRAY_D).scale(4)
        es_Reuler = MathTex(r"\vec{E}spac \hat{\i} o", r" \mathbb{R}euler", color=GRAY_D).scale(4)

        Reuler[0].shift(LEFT*0.2)
        Reuler[1:].shift(RIGHT*0.2)

        es_Reuler[0].shift(LEFT*0.2)
        es_Reuler[1:].shift(RIGHT*0.2)
        
        #self.play(Write(Reuler), run_time=2)\
        self.play(Write(es_Reuler),run_time=2)

        self.wait()

        self.play(Unwrite(es_Reuler))


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
        

