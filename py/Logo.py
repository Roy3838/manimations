from manim import *

config.pixel_width = 1920 
config.pixel_height = 1920


class Logo(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        LateX = MathTex("\\text{MC=}", color=GRAY_D)
        LateX2 = MathTex("\\text{E/c}", color=GRAY_D)
        LateX3 = MathTex(r"\frac{E}{c}", color=GRAY_D)

        Reuler=MathTex(r"\mathbb{R} \{\vec{S}\}", color=GRAY_D).scale(10)

        espacioReuler = MathTex(r"\vec{E} \mathbb{R}", color=GRAY_D).scale(10)
        
        
        #self.play(Write(Reuler), run_time=2)\
        self.add(espacioReuler)