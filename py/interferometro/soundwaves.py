from manim import *



class Waves(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        #puntos de fuentes
        point1=Dot(color=BLUE).shift(3*LEFT+UP)
        point2=Dot(color=BLUE).shift(3*LEFT+DOWN)

        
        #punto en el que se va a analizar el sonido
        target1=Dot(color=BLACK).shift(3*RIGHT+UP)
        target2=Dot(color=BLACK).shift(3*RIGHT+DOWN)
        line1= Line(point1.get_center(), target1.get_center()).set_color(GOLD)
        line2= Line(point2.get_center(), target2.get_center()).set_color(GOLD)
        
        x1=ValueTracker(-3)
        x2=ValueTracker(-3)

        point1.add_updater(lambda z: z.set_x(x1.get_value()))
        point2.add_updater(lambda z: z.set_x(x2.get_value()))
        line1.add_updater(lambda z: z.become(Line(point1.get_center(),target1.get_center()).set_color(GOLD)))
        line2.add_updater(lambda z: z.become(Line(point2.get_center(),target2.get_center()).set_color(GOLD)))


        #valores que afectan a la funcion parametrica
        phi=ValueTracker(60)
        len1=ValueTracker(6)
        len2=ValueTracker(6)
        amplitud=0.8
        periodo=8
        
        #funcion parametrica que representa el sonido de la fuente
        sound1=ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * t), 0)), t_range = np.array([0, len1.get_value()]), fill_opacity=0).set_color(RED)
        sound1.add_updater(lambda x: x.become(
            ParametricFunction(lambda t: 
            np.array((t, (1/1.54)*np.arctan(4*t)*amplitud*np.sin(periodo * t +phi.get_value()), 0)), 
            t_range = np.array([0, np.abs(target1.get_x()-x1.get_value())]), fill_opacity=0)
            .set_color(RED).align_to(point1,LEFT).shift(UP+0.05*RIGHT)
        ))
        
        sound2=ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * t), 0)), t_range = np.array([0, len2.get_value()]), fill_opacity=0).set_color(RED)
        sound2.add_updater(lambda x: x.become(
            ParametricFunction(lambda t: 
            np.array((t, (1/1.54)*np.arctan(4*t)*amplitud*np.sin(periodo * t +phi.get_value()), 0)), 
            t_range = np.array([0, np.abs(target2.get_x()-x2.get_value())]), fill_opacity=0)
            .set_color(RED).align_to(point2,LEFT).shift(DOWN+0.05*RIGHT)
        ))

        #punto que se mueve en la funcion parametrica sound y sound2
        analysispoint1=Dot(color=GOLD).shift(3*RIGHT+UP)
        analysispoint2=Dot(color=GOLD).shift(3*RIGHT+DOWN)
        analysispoint1.add_updater(lambda z: z.move_to(
            np.array((target1.get_x(), 
                      amplitud*np.sin(phi.get_value() + periodo * 2 * (target1.get_x() - x1.get_value())) + target2.get_y(), 0))))
        analysispoint2.add_updater(lambda z: z.move_to(
            np.array((target2.get_x(), 
                      amplitud*np.sin(phi.get_value() + periodo * 2 *(target1.get_x() - x1.get_value())) + target2.get_y(), 0))))


        # #vectores en el punto
        # vector1=Arrow(target1.get_center(),analysispoint1.get_center(),buff=0,color=BLACK).set_x(4.5)
        # vector2=Arrow(target2.get_center(),analysispoint2.get_center(),buff=0,color=BLACK).set_x(4.5)
        # #update vector
        # vector1.add_updater(lambda x: x.become(
        #     Arrow(target1.get_center(),analysispoint1.get_center(),buff=0,color=BLACK).set_x(4.5)
        # ))
        # vector2.add_updater(lambda x: x.become(
        #     Arrow(target2.get_center(),analysispoint2.get_center(),buff=0,color=BLACK).set_x(4.5)
        # ))



        #Brace de delta d
        brace=BraceBetweenPoints([analysispoint2.get_x(),-2,0],[analysispoint1.get_x(),-2,0]).set_color(BLACK)
        brace.add_updater(lambda z: z.become(
            BraceBetweenPoints([analysispoint2.get_x(),-2,0],[analysispoint1.get_x(),-2,0]).set_color(BLACK)
        ))

        #label del brace de delta d
        text_tracker=ValueTracker(1)
        deltalabel=MathTex("\\Delta d", color=BLACK).move_to(brace.get_center()+0.5*DOWN)
        deltalabel.add_updater(lambda z: z.move_to(brace.get_center()+0.5*DOWN))
        deltalabel2=MathTex("\\frac{" + str(int(np.floor(text_tracker.get_value()))) + "\\lambda}{2}", color=BLACK).move_to(brace.get_center()+0.7*DOWN)
        deltalabel2.add_updater(lambda z: z.become(
            MathTex("\\frac{" + str(int(np.floor(text_tracker.get_value()))) + "\\lambda}{2}", color=BLACK).move_to(brace.get_center()+0.7*DOWN)
            ))

        # """ MATH EQUATIONS """                   
        # deltad=MathTex(r"\Delta d",r"=",r"d_{1}",r"-",r"d_{2}").set_color(BLACK)
        # lambdad=MathTex(r"\frac{\lambda}{2}",r"=",r"\sqrt{\left(d+x\right)^{2}+y^{2}}",r"-",r"\sqrt{\left(d-x\right)^{2}+y^{2}}").set_color(BLACK)
        # deltadf1=SurroundingRectangle(deltad[0], buff = .1, color=GOLD)
        # deltadf2=SurroundingRectangle(deltad[2], buff = .1, color=GOLD)
        # deltadf3=SurroundingRectangle(deltad[4], buff = .1, color=GOLD)
        # lambdadf1=SurroundingRectangle(lambdad[0], buff = .1, color=GOLD)
        # lambdadf2=SurroundingRectangle(lambdad[2], buff = .1, color=GOLD)
        # lambdadf3=SurroundingRectangle(lambdad[4], buff = .1, color=GOLD)



        """ PART 2 DOS LINEAS POR SEPARADO"""


        '''ANIMACIONES 2'''
        lambda0=0.785398163397
        
        mobs=VGroup(line1,line2,point1,point2,target1,target2)
        self.play(Write(mobs))
        self.wait()
        self.play(Create(sound1),Create(sound2))
        self.play(FadeIn(analysispoint1),FadeIn(analysispoint2))
        self.play(phi.animate.set_value(30),rate_func=linear, run_time=4)
        
        
        self.play(x1.animate.set_value(-3.3),x2.animate.set_value(-2.3))
        self.play(phi.animate.set_value(0),rate_func=linear, run_time=4)
        #self.play(Create(brace),Create(deltalabel))
        #self.play(Create(vector1),Create(vector2))
        self.play(phi.animate.set_value(-30),rate_func=linear, run_time=4)
        self.play(Write(deltalabel2))


        self.play(x1.animate.set_value(-3+lambda0/4),x2.animate.set_value(-3-lambda0/4))
        self.play(phi.animate.set_value(-60),rate_func=linear, run_time=4)
        
        self.play(x1.animate.set_value(-3+lambda0/2),x2.animate.set_value(-3-lambda0/2))
        self.play(phi.animate.set_value(-90),rate_func=linear, run_time=4)

        
        self.play(x1.animate.set_value(-3+lambda0/4),x2.animate.set_value(-3-lambda0/4))
        self.play(phi.animate.set_value(-120),rate_func=linear, run_time=4)
        
        self.play(text_tracker.animate.set_value(2),run_time=0.1)
        self.play(x1.animate.set_value(-3+lambda0/2),x2.animate.set_value(-3-lambda0/2))
        self.play(phi.animate.set_value(-150),rate_func=linear, run_time=4)

        # self.play(text_tracker.animate.set_value(3),run_time=0.1)
        # self.play(x1.animate.set_value(3+3*lambda0/4),x2.animate.set_value(3-3*lambda0/4))
        # self.play(phi.animate.set_value(-180),rate_func=linear, run_time=4)
        
        # self.play(text_tracker.animate.set_value(4),run_time=0.1)
        # self.play(x1.animate.set_value(3+lambda0),x2.animate.set_value(3-lambda0))
        # self.play(phi.animate.set_value(-210),rate_func=linear, run_time=4)

        # self.play(text_tracker.animate.set_value(5),run_time=0.1)
        # self.play(x1.animate.set_value(3+5*lambda0/4),x2.animate.set_value(3-5*lambda0/4))
        # self.play(phi.animate.set_value(-240),rate_func=linear, run_time=4)
        # self.play(phi.animate.set_value(-270),rate_func=linear, run_time=4)

        #self.play(phi.animate.set_value(5))
        # self.wait()
        # self.play(FadeOut(brace),FadeOut(deltalabel2),FadeOut(vector1),FadeOut(vector2),
        #         FadeOut(analysispoint1),FadeOut(analysispoint2),FadeOut(sound1),
        #         FadeOut(sound2),FadeOut(target1),FadeOut(target2),FadeOut(line1),
        #         FadeOut(line2),FadeOut(point1),FadeOut(point2))
        # self.wait()
