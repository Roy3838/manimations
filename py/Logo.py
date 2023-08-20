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

        Slogan = MathTex(r"\vec{S}implif\hat{y} \mathbf{C}omplexit\hat{y}", color=GRAY_D).scale(2)
        Slogan2 = MathTex(r"Using your \mathbf{Im}agination", color=GRAY_D).scale(2).move_to(Slogan, DOWN)
        Slogan3 = MathTex(r"Make the \mathbf{R}eal World Better", color=GRAY_D).scale(2).move_to(Slogan2, DOWN)
        
        # not using MathTex
        Slogan = Tex(r"$\mathbb{R}\{\vec{S}\} = $ $\vec{S}$implify $\mathbb{C}$omplexit$\hat{y}$", color=GRAY_D).scale(2)
        Slogan2 = Tex(r"Using your $\mathbb{I}$maginatio$\bar{n}$", color=GRAY_D).scale(2)
        Slogan3 = Tex(r"Make your $\mathbb{R}$eality Bette$\vec{r}$", color=GRAY_D).scale(2)


        slogan = VGroup(Slogan, Slogan2, Slogan3).arrange(DOWN, buff=0.5)
        Slogan.shift(LEFT*1.3)
        Slogan3.shift(LEFT*0.5)

        slogan.shift(RIGHT*1.3)

        # not using MathTex
        Slogan = Tex(r"$\mathbb{R}\{\vec{S}\} = $ $\vec{\mathbf{S}}$implify $\mathbb{C}$omplexit$\hat{y}$", color=GRAY_D).scale(2)
        Slogan2 = Tex(r"$\mathbf{U}$sing your $\mathbb{I}$maginatio$\bar{n}$", color=GRAY_D).scale(2)
        Slogan3 = Tex(r"$\mathbf{M}$ake the $\mathbb{R}$eal World Bette$\vec{r}$", color=GRAY_D).scale(2)

        # COMBINING SUM AND CIR \sum of Curiosity Inspiration and Reflection
        summ = MathTex(r"\sum ",r"\mathbb{C}uriosity", r" \mathbb{I}nspiration",r" \mathbb{R}eflection", color=GRAY_D)
        summ.arrange(DOWN, buff=0.1)
        # Align left part
        summ[1].align_to(summ[0], LEFT)
        summ[2].align_to(summ[0], LEFT)
        summ[3].align_to(summ[0], LEFT)
        summ[0].move_to(summ[2]).shift(LEFT*2)
        summ[0].scale([1.5,2,1])
        summ.shift(RIGHT*3+DOWN*4)



        slogan = VGroup(Slogan, Slogan2, Slogan3).arrange(DOWN, buff=0.5)
        slogan.add(summ)
        Slogan.shift(LEFT*1.3)
        Slogan3.shift(LEFT*1.1)

        slogan.shift(RIGHT*1.3)

        #self.play(Write(Reuler), run_time=2)\
        #self.add(espacioReuler)
        self.add(slogan)