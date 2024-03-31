from manim import *
import numpy as np

class LLM(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        text = Text('').scale(0.6).set_color(BLACK)

        self.add(text)

        for letter in text:
            letter_box = SurroundingRectangle(letter).set_color(BLACK)
            self.play(Create(letter_box), run_time=0.2)


        
        self.wait(10)

