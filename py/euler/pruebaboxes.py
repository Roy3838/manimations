from manim import *



class pruebaBoxes(Scene):
    def construct(self):

        self.camera.background_color = "#E2E2E2"


        ec_v_despejada_final = MathTex(r" \vec{p}_{f}" , r"=", r"\vec{v}\cdot \Delta t + \vec{p}_{i}").move_to(DOWN*2).scale(1.3)
        ec_a_despejada_final = MathTex(r" \vec{v}_{f}" , r"=", r"\vec{a}\cdot \Delta t + \vec{v}_{i}").move_to(DOWN*3).scale(1.3)
            
        example_listing = Code(
                "/home/jay/manimations/py/euler/example.py",
                tab_width=4,
                background="window",
                language="python",
                font="Monospace",
                background_stroke_color= WHITE,
            ).move_to(ec_v_despejada_final.get_center()+ UP*2).scale(0.5)
        
        self.play(Write(example_listing))

        pos_boxes = VGroup()
        vel_boxes = VGroup()


        # Code Block lines
        pos_boxes.add(SurroundingRectangle(example_listing[2][2],buff=0).shift(DOWN*0.1+LEFT*0.1))
        vel_boxes.add(SurroundingRectangle(example_listing[2][4],buff=0).shift(DOWN*0.1+LEFT*0.1))

        pos_boxes.add(SurroundingRectangle(ec_v_despejada_final,buff=0.2))
        vel_boxes.add(SurroundingRectangle(ec_a_despejada_final,buff=0.2))

        self.play(Write(pos_boxes))

        self.wait(2)


        # Se tiene que hacer una variable temporal para que funcione
        temppos = pos_boxes.copy()

        #pos to vel
        self.play(ReplacementTransform(pos_boxes[0],vel_boxes[0]),
                    ReplacementTransform(pos_boxes[1],vel_boxes[1]))
        
        #vel to pos
        self.play(ReplacementTransform(vel_boxes[0],temppos[0]),
                    ReplacementTransform(vel_boxes[1],temppos[1]))
        
        