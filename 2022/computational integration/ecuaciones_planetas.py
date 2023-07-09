from manim import *
import numpy as np
import time
width=1080
height=1920
config.frame_size = [width, height]

class Ecuaciones(MovingCameraScene):
    def construct(self):

        self.camera.frame.scale(1)    
        # ecuaciones en desmos https://www.desmos.com/calculator/rfsgckt7ub
        
        def ecuaciones_generales():
            # ponemos gravitacion F\left(\vec{r}\right)=G\frac{mM}{\vec{r}^{2}} en forma de vector
            ecuacionFr = MathTex(r"F\left(\vec{r}\right)",r"=",r"G\frac{mM}{\vec{r}^{2}}").move_to(UP*2).set_color(BLACK)
            # ponemos ley de newton "F\left(\vec{r}\right)=m\vec{a} en forma de vector
            ecuacionma = MathTex(r"F\left(\vec{r}\right)", r"=", r"m",r"\vec{a}").move_to(UP*2).set_color(BLACK)
            # ponemos despeje de la aceleracion \frac{F\left(r\right)}{m}=a en forma de vector
            ecuaciona = MathTex(r"\frac{F\left(\vec{r}\right)}{m}", r"=", r"\vec{a}").move_to(UP*2).set_color(BLACK)
            # integral simple a \int_{ }^{ }a=v
            ecuacionv = MathTex(r"\int_{ }^{ }",r"\vec{a}", r"=", r"\vec{v}").move_to(UP*2).set_color(BLACK)
            # integral simple v \int_{ }^{ }v=r
            ecuacionr = MathTex(r"\int_{ }^{ }",r"\vec{v}", r"=", r"\vec{r}").move_to(UP*2).set_color(BLACK)
            # definicion r r=<x,y,z>
            ecuacionr2 = MathTex(r"\vec{r}", r"=", r"<x,y,z>").move_to(UP*2).set_color(BLACK)

            # ecuaciona pero rara para separar la division de latex
            ecuaciona2 = MathTex(r"\frac{F\left(\vec{r}\right)}{}", r"=", r"\vec{a}").move_to(UP*2).set_color(BLACK)
            ecuaciona2_m= MathTex("m").move_to(UP*2 + LEFT*0.5 + DOWN*0.5).set_color(BLACK)

            pregunta = MathTex(r"\vec{r}=<x,y,z>=?").set_color(BLACK)


            
            #self.add(NumberPlane())
            

            self.wait()
            self.play(Write(ecuacionFr))
            self.play(Write(pregunta))
            # de Fr a ma
            self.wait()
            self.play(
                ReplacementTransform(ecuacionFr[0],ecuacionma[0]),
                ReplacementTransform(ecuacionFr[1],ecuacionma[1]),
                ReplacementTransform(ecuacionFr[2],ecuacionma[2:]),
                )
            self.wait()

            # de ma a a
            self.play(
                #F(r) a F(r)/m
                ReplacementTransform(ecuacionma[0],ecuaciona2[0]),
                #= a =
                ReplacementTransform(ecuacionma[1],ecuaciona2[1]),
                # a a a
                ReplacementTransform(ecuacionma[3],ecuaciona2[2]),
                # m a m
                ReplacementTransform(ecuacionma[2],ecuaciona2_m),

            )
            self.wait()

            # de a a v
            self.play(
                FadeOut(ecuaciona2), FadeOut(ecuaciona2_m),
                # a a a
                ReplacementTransform(ecuaciona2[2],ecuacionv[1]),
                # = a =
                ReplacementTransform(ecuaciona2[1],ecuacionv[2]),

                FadeIn(ecuacionv[0]), FadeIn(ecuacionv[3])
            )
            self.wait()


            # de v a r
            self.play(
                FadeOut(ecuacionv),
                # integral a integral
                ReplacementTransform(ecuacionv[0],ecuacionr[0]),
                # v a v
                ReplacementTransform(ecuacionv[3],ecuacionr[1]),
                # = a =
                ReplacementTransform(ecuacionv[2],ecuacionr[2]),

                FadeIn(ecuacionr)
            )
            self.wait()

            # de r a r<>
            self.play(
                FadeOut(ecuacionr),

                # r a r
                ReplacementTransform(ecuacionr[1],ecuacionr2[0]),
                # = a =
                ReplacementTransform(ecuacionr[2],ecuacionr2[1]),
                

                FadeIn(ecuacionr2)
            )
            self.play(ReplacementTransform(pregunta,ecuacionr2))


            self.wait()


        def Ecuaciones_CasoParabolico():
            self.wait()


        ecuaciones_generales()

