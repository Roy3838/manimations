from manim import *

class EyeLogoScene(MovingCameraScene):
    def construct(self):

        self.camera.background_color ="#111827" 

        # Create the eye outline mobject
        eye_outline = Circle(radius=2.6, color=WHITE, stroke_width=40)
        
        # Create the pupil mobject
        pupil = Circle(radius=0.8, color=WHITE, fill_opacity=1)
        
        # Position both at the center
        eye_outline.move_to(ORIGIN)
        pupil.move_to(ORIGIN)
        
        # Group them for the complete eye
        eye_logo = VGroup(eye_outline, pupil)

        self.add(eye_logo)

        self.play(
                pupil.animate.shift(DOWN+RIGHT),
                run_time=0.5
                )
        self.play(
                pupil.animate.shift(LEFT*1.5),
                run_time=0.5
                )

        self.play(
                pupil.animate.move_to(ORIGIN),
                run_time=0.6
                )
        
        self.play(
            self.camera.frame.animate.scale(2).shift(9.5*RIGHT),
            run_time=0.5
        )

        with register_font("/home/jay/Downloads/static/GolosText-Medium.ttf"):
            bserver = Text("bserver", font="Golos Text")
            bserver.scale(8)
            bserver.shift(RIGHT*12.5 + 0.3*DOWN)
            bserver.set_color(WHITE)

            self.play(Write(bserver))

        
        # Hold the final state
        self.wait(2)

