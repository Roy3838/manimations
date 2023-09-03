from manim import *


width=1080
height=1920
config.frame_size = [width, height]

class Logo(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        
        
        
        
        def horizontal():
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

        def vertical():
            Reuler=MathTex(r"\mathbb{R}euler" , r"\vec{S}",r"pac",r"\hat{e}", color=GRAY_D).scale(7)
            es_Reuler = MathTex(r"\vec{E}spac \hat{\i} o", r" \mathbb{R}euler", color=GRAY_D).scale(7)


            Reuler[0].shift(RIGHT*4.8)
            Reuler[1:].shift(DOWN*4 + LEFT*6)
            Reuler.shift(UP*4)

            es_Reuler[0].shift(RIGHT*5)
            es_Reuler[1:].shift(DOWN*4 + LEFT*6)
            es_Reuler.shift(UP*4)
            
            #self.play(Write(Reuler), run_time=2)\
            self.play(Write(Reuler),run_time=2)

            self.wait()

            self.play(Unwrite(Reuler))

        vertical()

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
        

