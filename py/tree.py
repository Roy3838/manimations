from manim import *

class Tree(Scene):
    def construct(self):
        #info blocks
        block1=Rectangle(width=2.0,height=1.0).shift(2*DOWN,5.5*LEFT)
        block2=Rectangle(width=2.0,height=1.0).shift(2*DOWN,2*LEFT)
        block3=Rectangle(width=2.0,height=1.0).shift(2*DOWN,2*RIGHT)
        block4=Rectangle(width=2.0,height=1.0).shift(2*DOWN,5.5*RIGHT)
        block1text=Text("Block 1").move_to(block1).scale(0.6)
        block2text=Text("Block 2").move_to(block2).scale(0.6)
        block3text=Text("Block 3").move_to(block3).scale(0.6)
        block4text=Text("Block 4").move_to(block4).scale(0.6)
        #hashes
        hash1=Text("Hash(Block 1)").move_to(block1).scale(0.6).shift(1.5*UP)
        hash2=Text("Hash(Block 2)").move_to(block2).scale(0.6).shift(1.5*UP)
        hash3=Text("Hash(Block 3)").move_to(block3).scale(0.6).shift(1.5*UP)
        hash4=Text("Hash(Block 4)").move_to(block4).scale(0.6).shift(1.5*UP)
        #arrows
        arrow1=Arrow(block1.get_top(),hash1.get_bottom())
        arrow2=Arrow(block2.get_top(),hash2.get_bottom())
        arrow3=Arrow(block3.get_top(),hash3.get_bottom())
        arrow4=Arrow(block4.get_top(),hash4.get_bottom())



        self.play(Create(block1),Create(block2),Create(block3),Create(block4))
        self.play(Write(block1text),Write(block2text),Write(block3text),Write(block4text))
        self.wait()
        self.play(Create(arrow1),Create(arrow2),Create(arrow3),Create(arrow4))
        self.play(Write(hash1),Write(hash2),Write(hash3),Write(hash4))
        self.wait()