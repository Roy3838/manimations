# Script para probar hacer cajas alrededor de numeradores y denominadores en manim
# Script to test making boxes around numerators and denominators in manim


# DOESNT WORK
from manim import *

class MovingFrameBox(Scene):
    def construct(self):

        # Create the MathTex object
        expression = MathTex(r"\frac{xd}{~}")
        expression2= MathTex(r"\frac{~}{aa}")
        
        # Play the animation to write the expression
        self.play(Write(expression ))
        self.play(Write(expression2))
        
        # Create the surrounding rectangles
        framebox1 = SurroundingRectangle(expression , buff=0.1)
        framebox2 = SurroundingRectangle(expression2, buff=0.1)
        
        # Play the animation to create the first box
        self.play(Create(framebox1))
        self.wait()
        
        # Play the animation to create the second box
        self.play(Create(framebox2))
        self.wait()









