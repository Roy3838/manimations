from manim import *




#Animation of two point emminating spherical waves that interfere with each other
class TwoPointInterference(Scene):
    
    
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        #self.twopoints()
        #self.twodistances()
        #self.mathequations()
        #self.young()
        #self.michelson()
        self.hyperbolic()
        
    def twopoints(self):
        def Create_wave(fuente):
            #Create wave
            radius = ValueTracker(0.01)
            radiusfinal=5
            wave=Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center())
            wave.add_updater(lambda m: m.become(Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center()).set_opacity((1-(1/radiusfinal)*radius.get_value()))))
            self.add(wave)
            return radius.animate.set_value(radiusfinal)

        ''' PART 1 PLANO GENERAL'''

        

        #Create two points
        fuente1=Dot(color=BLUE).shift(3*LEFT)
        fuente2=Dot(color=BLUE).shift(3*RIGHT)

        
            

        analysispoint=Dot(color=BLACK)
        

        distance1=Line(fuente1,analysispoint).set_color(GOLD)
        distance2=Line(fuente2,analysispoint).set_color(GOLD)

        distance1.add_updater(lambda x: x.become(
            Line(fuente1,analysispoint).set_color(GOLD)
        ))
        distance2.add_updater(lambda x: x.become(
            Line(fuente2,analysispoint).set_color(GOLD)
        ))
        
        bracedis1=BraceBetweenPoints(fuente1.get_center(),analysispoint.get_center(),buff=0,color=BLACK)
        bracedis1.add_updater(lambda z: z.become(
            BraceBetweenPoints(fuente1.get_center(),analysispoint.get_center(),buff=0,color=BLACK)
        ))
        dis1label=MathTex(r"d_{1}", color=BLACK).move_to(bracedis1.get_center()+0.5*DOWN)
        dis1label.add_updater(lambda z: z.move_to(bracedis1.get_center()+0.5*DOWN))
        
        bracedis2=BraceBetweenPoints(analysispoint.get_center(),fuente2.get_center(),buff=0,color=BLACK)
        bracedis2.add_updater(lambda z: z.become(
            BraceBetweenPoints(analysispoint.get_center(),fuente2.get_center(),buff=0,color=BLACK)
        ))
        dis2label=MathTex(r"d_{2}", color=BLACK).move_to(bracedis2.get_center()+0.5*DOWN)
        dis2label.add_updater(lambda z: z.move_to(bracedis2.get_center()+0.5*DOWN))
        

        ''' ANIMACIONES 1'''
        self.add(fuente1,fuente2,distance1,distance2,analysispoint)
        self.play(Create_wave(fuente1),Create_wave(fuente2))
        self.play(Create_wave(fuente1),Create_wave(fuente2))
        self.play(Create_wave(fuente1),Create_wave(fuente2))
        self.play(Create_wave(fuente1),Create_wave(fuente2))
        self.wait(0.5)
        self.play(analysispoint.animate.move_to(0.5*RIGHT))
        self.play(Write(bracedis1),Write(dis1label),Write(bracedis2),Write(dis2label))
        self.play(analysispoint.animate.shift(LEFT))
        self.play(analysispoint.animate.shift(1.5*RIGHT),run_time=1.5)
        self.play(FadeOut(distance1),FadeOut(distance2))
        self.play(FadeOut(fuente1),FadeOut(fuente2),FadeOut(analysispoint),
                  FadeOut(bracedis1),FadeOut(dis1label),FadeOut(bracedis2),FadeOut(dis2label))
        self.wait(0.5)
        
        self.twodistances()




        ''' PART 2 PLANO GENERAL'''
        self.add(fuente1,fuente2,distance1,distance2,analysispoint)
        self.play(analysispoint.animate.move_to(0.5*RIGHT+UP))
        self.play(Write(bracedis1),Write(dis1label),Write(bracedis2),Write(dis2label))
        self.play(analysispoint.animate.shift(LEFT+2*DOWN))
        self.play(analysispoint.animate.shift(1.5*RIGHT+2*UP))
        self.play(FadeOut(distance1),FadeOut(distance2))
        self.play(FadeOut(fuente1),FadeOut(fuente2),FadeOut(analysispoint),
                  FadeOut(bracedis1),FadeOut(dis1label),FadeOut(bracedis2),FadeOut(dis2label))
        self.wait(0.5)
            

    def twodistances(self):
        """ PART 2 DOS LINEAS POR SEPARADO"""

        
        



        #puntos de fuentes
        point1=Dot(color=BLUE).shift(3*LEFT+UP)
        point2=Dot(color=BLUE).shift(3*LEFT+DOWN)

        
        #punto en el que se va a analizar el sonido
        target1=Dot(color=BLACK).shift(3*RIGHT+UP)
        target2=Dot(color=BLACK).shift(3*RIGHT+DOWN)
        line1= Line(point1.get_center(), target1.get_center()).set_color(GOLD)
        line2= Line(point2.get_center(), target2.get_center()).set_color(GOLD)
        
        x1=ValueTracker(3)
        x2=ValueTracker(3)

        target1.add_updater(lambda z: z.set_x(x1.get_value()))
        target2.add_updater(lambda z: z.set_x(x2.get_value()))
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
            t_range = np.array([0, np.abs(point1.get_x()-x1.get_value())]), fill_opacity=0)
            .set_color(RED).align_to(point1,LEFT).shift(UP+0.05*RIGHT)
        ))
        
        sound2=ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * t), 0)), t_range = np.array([0, len2.get_value()]), fill_opacity=0).set_color(RED)
        sound2.add_updater(lambda x: x.become(
            ParametricFunction(lambda t: 
            np.array((t, (1/1.54)*np.arctan(4*t)*amplitud*np.sin(periodo * t +phi.get_value()), 0)), 
            t_range = np.array([0, np.abs(point2.get_x()-x2.get_value())]), fill_opacity=0)
            .set_color(RED).align_to(point2,LEFT).shift(DOWN+0.05*RIGHT)
        ))

        #punto que se mueve en la funcion parametrica sound y sound2
        analysispoint1=Dot(color=GOLD).shift(3*RIGHT+UP)
        analysispoint2=Dot(color=GOLD).shift(3*RIGHT+DOWN)
        analysispoint1.add_updater(lambda z: z.move_to(np.array((target1.get_x(), amplitud*np.sin(periodo * target1.get_x() +phi.get_value() -PI/4) + target1.get_y(), 0))))
        analysispoint2.add_updater(lambda z: z.move_to(np.array((target2.get_x(), amplitud*np.sin(periodo * target2.get_x() +phi.get_value() -PI/4) + target2.get_y(), 0))))


        #vectores en el punto
        vector1=Arrow(target1.get_center(),analysispoint1.get_center(),buff=0,color=BLACK).set_x(4.5)
        vector2=Arrow(target2.get_center(),analysispoint2.get_center(),buff=0,color=BLACK).set_x(4.5)
        #update vector
        vector1.add_updater(lambda x: x.become(
            Arrow(target1.get_center(),analysispoint1.get_center(),buff=0,color=BLACK).set_x(4.5)
        ))
        vector2.add_updater(lambda x: x.become(
            Arrow(target2.get_center(),analysispoint2.get_center(),buff=0,color=BLACK).set_x(4.5)
        ))


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
                                
        

        '''ANIMACIONES 2'''
        lambda0=0.785398163397
        
        mobs=VGroup(line1,line2,point1,point2,target1,target2)
        self.play(Write(mobs))
        self.wait()
        self.play(Create(sound1),Create(sound2))
        self.play(FadeIn(analysispoint1),FadeIn(analysispoint2))
        self.play(phi.animate.set_value(30),rate_func=linear, run_time=4)
        
        
        self.play(x1.animate.set_value(3.3),x2.animate.set_value(2.3))
        self.play(phi.animate.set_value(0),rate_func=linear, run_time=4)
        self.play(Create(brace),Create(deltalabel))
        self.play(Create(vector1),Create(vector2))
        self.play(phi.animate.set_value(-30),rate_func=linear, run_time=4)


        self.play(x1.animate.set_value(3+lambda0/4),x2.animate.set_value(3-lambda0/4))
        self.play(phi.animate.set_value(-60),rate_func=linear, run_time=4)
        
        self.play(x1.animate.set_value(3+lambda0/2),x2.animate.set_value(3-lambda0/2))
        self.play(phi.animate.set_value(-90),rate_func=linear, run_time=4)

        self.play(FadeOut(deltalabel))
        self.play(Write(deltalabel2))
        
        self.play(x1.animate.set_value(3+lambda0/4),x2.animate.set_value(3-lambda0/4))
        self.play(phi.animate.set_value(-120),rate_func=linear, run_time=4)
        
        self.play(text_tracker.animate.set_value(2),run_time=0.1)
        self.play(x1.animate.set_value(3+lambda0/2),x2.animate.set_value(3-lambda0/2))
        self.play(phi.animate.set_value(-150),rate_func=linear, run_time=4)

        self.play(text_tracker.animate.set_value(3),run_time=0.1)
        self.play(x1.animate.set_value(3+3*lambda0/4),x2.animate.set_value(3-3*lambda0/4))
        self.play(phi.animate.set_value(-180),rate_func=linear, run_time=4)
        
        self.play(text_tracker.animate.set_value(4),run_time=0.1)
        self.play(x1.animate.set_value(3+lambda0),x2.animate.set_value(3-lambda0))
        self.play(phi.animate.set_value(-210),rate_func=linear, run_time=4)

        self.play(text_tracker.animate.set_value(5),run_time=0.1)
        self.play(x1.animate.set_value(3+5*lambda0/4),x2.animate.set_value(3-5*lambda0/4))
        self.play(phi.animate.set_value(-240),rate_func=linear, run_time=4)
        self.play(phi.animate.set_value(-270),rate_func=linear, run_time=4)

        #self.play(phi.animate.set_value(5))
        self.wait()
        self.play(FadeOut(brace),FadeOut(deltalabel2),FadeOut(vector1),FadeOut(vector2),
                  FadeOut(analysispoint1),FadeOut(analysispoint2),FadeOut(sound1),
                  FadeOut(sound2),FadeOut(target1),FadeOut(target2),FadeOut(line1),
                  FadeOut(line2),FadeOut(point1),FadeOut(point2))
        self.wait()
        

    def mathequations(self):
        deltad=MathTex(r"\Delta d",r"=",r"d_{1}",r"-",r"d_{2}").set_color(BLACK)
        lambdad=MathTex(r"\frac{\lambda}{2}",r"=",r"\sqrt{\left(d+x\right)^{2}+y^{2}}",r"-",r"\sqrt{\left(d-x\right)^{2}+y^{2}}").set_color(BLACK)
        deltadf1=SurroundingRectangle(deltad[0], buff = .1, color=GOLD)
        deltadf2=SurroundingRectangle(deltad[2], buff = .1, color=GOLD)
        deltadf3=SurroundingRectangle(deltad[4], buff = .1, color=GOLD)
        lambdadf1=SurroundingRectangle(lambdad[0], buff = .1, color=GOLD)
        lambdadf2=SurroundingRectangle(lambdad[2], buff = .1, color=GOLD)
        lambdadf3=SurroundingRectangle(lambdad[4], buff = .1, color=GOLD)


        self.play(Write(deltad))
        self.play(Write(deltadf1))
        self.play(ReplacementTransform(deltadf1,deltadf2))
        self.play(ReplacementTransform(deltadf2,deltadf3))
        self.wait()
        self.play(FadeOut(deltadf3))
        self.play(deltad.animate.shift(UP))
        self.play(Write(lambdad))
        self.play(Write(lambdadf1))
        deltadf1=SurroundingRectangle(deltad[0], buff = .1, color=GOLD)
        deltadf2=SurroundingRectangle(deltad[2], buff = .1, color=GOLD)
        deltadf3=SurroundingRectangle(deltad[4], buff = .1, color=GOLD)
        self.play(Write(deltadf1))
        self.wait()
        self.play(ReplacementTransform(lambdadf1,lambdadf2),ReplacementTransform(deltadf1,deltadf2))
        self.wait()
        self.play(ReplacementTransform(lambdadf2,lambdadf3),ReplacementTransform(deltadf2,deltadf3))
        self.wait()
        self.play(FadeOut(lambdadf3),FadeOut(deltadf3))
        self.wait()
        self.play(FadeOut(lambdad),FadeOut(deltad))


    def young(self):
        def Create_semi(fuente):
            #Create semi wave
            radius = ValueTracker(0.01)
            radiusfinal=7
            wave=Arc(radius=radius.get_value(),start_angle=-90*DEGREES,angle=PI,color=BLUE).move_to(fuente.get_center())
            wave.add_updater(lambda m: m.become(
                Arc(radius=radius.get_value(),start_angle=-90*DEGREES,angle=PI,color=BLUE).align_to(fuente,direction=LEFT).set_opacity((1-(1/radiusfinal)*radius.get_value())).set_y(fuente.get_y())
                ))
            
            self.add(wave)
            return radius.animate.set_value(radiusfinal)
        
        def Create_wave(fuente):
            #Create wave with circle
            radius = ValueTracker(0.01)
            radiusfinal=5
            wave=Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center())
            wave.add_updater(lambda m: m.become(Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center()).set_opacity((1-(1/radiusfinal)*radius.get_value()))))
            self.add(wave)
            return radius.animate.set_value(radiusfinal)
        #fuente de la izquierda
        fuente1=Dot(color=BLUE).shift(6*LEFT)
        #fuentes que representan las rendijas
        fuente2=Dot(color=BLUE).shift(UP)
        fuente3=Dot(color=BLUE).shift(DOWN)
        #rejilla entre las dos fuentes
        rejilla1=Rectangle(height=np.abs(fuente2.get_y()-fuente3.get_y()-0.2), width=0.2,color=BLACK).move_to(fuente2.get_x())
        #rejillas arriba y abajo
        rejilla2=Rectangle(height=4, width=0.2,color=BLACK).align_to(fuente2,direction=DOWN).shift(UP*0.2)
        rejilla3=Rectangle(height=4, width=0.2,color=BLACK).align_to(fuente3,direction=UP).shift(DOWN*0.2)
        #pantalla
        pantalla=Rectangle(height=8,width=0.2,color=BLACK).move_to(RIGHT*6)
        
        #distancias
        analysispoint=Dot(color=RED).move_to(pantalla.get_center())
        distance1=Line(fuente2,analysispoint).set_color(GOLD)
        distance2=Line(fuente3,analysispoint).set_color(GOLD)

        distance1.add_updater(lambda x: x.become(
            Line(fuente2,analysispoint).set_color(GOLD)
        ))
        distance2.add_updater(lambda x: x.become(
            Line(fuente3,analysispoint).set_color(GOLD)
        ))
        
        #animaciones
        self.add(fuente1,rejilla1,rejilla2,rejilla3,pantalla)
        self.play(Create_wave(fuente1),run_time=1.5)
        self.play(Create_semi(fuente2),Create_semi(fuente3),run_time=1.5)
        self.play(Create_wave(fuente1),run_time=1.5)
        self.play(Create_semi(fuente2),Create_semi(fuente3),run_time=1.5)
        self.play(FadeIn(fuente2),FadeIn(fuente3))
        self.play(Create_wave(fuente2),Create_wave(fuente3),run_time=1.5)
        self.play(Create_wave(fuente2),Create_wave(fuente3),run_time=1.5)
        self.wait()
        self.play(Create(distance1),Create(distance2),Create(analysispoint),run_time=1.5)
        self.wait()
        self.play(analysispoint.animate.shift(UP))
        self.wait()
        self.play(Create_wave(fuente2),Create_wave(fuente3),run_time=1.5)
        self.play(analysispoint.animate.shift(DOWN*3),run_time=2)
        self.play(Create_wave(fuente2),Create_wave(fuente3),run_time=1.5)
        self.wait()

        self.play(FadeOut(distance1),FadeOut(distance2),FadeOut(analysispoint))
        self.play(FadeOut(fuente1),FadeOut(fuente2),FadeOut(fuente3),FadeOut(rejilla1),FadeOut(rejilla2),FadeOut(rejilla3),FadeOut(pantalla))
        

    def michelson(self):
        def Create_wave(fuente):
            #Create wave with circle
            radius = ValueTracker(0.01)
            radiusfinal=5
            wave=Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center())
            wave.add_updater(lambda m: m.become(Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center()).set_opacity((1-(1/radiusfinal)*radius.get_value()))))
            self.add(wave)
            return radius.animate.set_value(radiusfinal)
        #recibe los parámetros de una onda y te regresa el Mobject
        def onda(pos1,pos2,color,start=ValueTracker(0),difface=0,periodo=8,amplitud=0.2,override=0):
            if override==0:
                override=pos2
            elif override ==1:
                override=pos1
                
                
            length=np.sqrt(np.power(pos1[0]-pos2[0],2)+np.power(pos1[1]-pos2[1],2))
            sound2=ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * (t + difface)), 0)), t_range = np.array([0, length]), fill_opacity=0).set_color(color)
            
            sound2.add_updater(lambda x: x.become(
                ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * (t + difface)), 0)), t_range = np.array([start.get_value(), length]), fill_opacity=0).set_color(color)
                .rotate(np.arctan((pos1[1]-pos2[1])/(pos1[0]-pos2[0])),about_point=pos1)
                .align_to(override, direction=RIGHT)
                ))
            return sound2
        def onda_vert(pos1,pos2,color,start=ValueTracker(0),difface=0,periodo=8,amplitud=0.2):
            length=np.sqrt(np.power(pos1[0]-pos2[0],2)+np.power(pos1[1]-pos2[1],2))
            sound2=ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * (t + difface)), 0)), t_range = np.array([0, length]), fill_opacity=0).set_color(color)
            
            sound2.add_updater(lambda x: x.become(
                ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * (t + difface)), 0)), t_range = np.array([start.get_value(), length]), fill_opacity=0).set_color(color)
                .rotate(np.arctan((pos1[1]-pos2[1])/(pos1[0]-pos2[0])),about_point=pos1)
                .move_to([(pos1[0]+pos2[0])/2,(pos1[1]+pos2[1] + start.get_value())/2,0])
                ))
            return sound2
        
        def onda_vertabajo(pos1,pos2,color,start=ValueTracker(0),difface=0,periodo=8,amplitud=0.2):
            length=np.sqrt(np.power(pos1[0]-pos2[0],2)+np.power(pos1[1]-pos2[1],2))
            sound2=ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * (t + difface)), 0)), t_range = np.array([0, length]), fill_opacity=0).set_color(color)
            
            sound2.add_updater(lambda x: x.become(
                ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * (t + difface)), 0)), t_range = np.array([start.get_value(), length]), fill_opacity=0).set_color(color)
                .rotate(np.arctan((pos1[1]-pos2[1])/(pos1[0]-pos2[0])),about_point=pos1)
                .move_to([(pos1[0]+pos2[0])/2,(pos1[1]+pos2[1] - start.get_value())/2,0])
                ))
            return sound2

        def onda_regreso(pos1,pos2,color,start=ValueTracker(0),difface=0,periodo=8,amplitud=0.2,override=0):
            length=np.sqrt(np.power(pos1[0]-pos2[0],2)+np.power(pos1[1]-pos2[1],2))
            sound2=ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * (t + difface)), 0)), t_range = np.array([0, length]), fill_opacity=0).set_color(color)
            
            sound2.add_updater(lambda x: x.become(
                ParametricFunction(lambda t: np.array((t, amplitud*np.sin(periodo * (t + difface)), 0)), t_range = np.array([start.get_value(), length]), fill_opacity=0).set_color(color)
                .rotate(np.arctan((pos1[1]-pos2[1])/(pos1[0]-pos2[0])),about_point=pos1)
                .move_to([(pos1[0]+pos2[0] + start.get_value())/2,(pos1[1]+pos2[1])/2,0])
                ))
            return sound2
        

        #fuente original que se convierte en laser
        fuente=Dot(color=BLUE).shift(6*LEFT)
        laser=Rectangle(height=0.2,width=1,color=BLUE).shift(LEFT*6)
        #splitter de en medio
        splitter=Rectangle(height=0.1,width=0.7,color=GREY).rotate(PI/4)
        #los dos espejos, el a es el de arriba y el b el de abajo
        espejoa=Rectangle(height=0.1,width=0.7,color=GREY_D).shift(3.5*UP)
        espejob=Rectangle(height=0.1,width=0.7,color=GREY_D).shift(3.5*RIGHT).rotate(PI/2)
        #pantalla de observación de abajo
        pantalla=Rectangle(height=0.1,width=5,color=BLACK).move_to(DOWN*3.5)
        #onda antes de splitter
        onda1tracker=ValueTracker(0)
        onda1=onda(laser.get_right(),splitter.get_left(),BLUE,onda1tracker)

        #ondas despues de splitter (onda pa riba y luego pa derecha)
        onda2tracker=ValueTracker(0)
        onda2=onda_vert(espejoa.get_bottom(),splitter.get_top(),BLUE,onda2tracker)
        onda3tracker=ValueTracker(0)
        onda3=onda(splitter.get_right(),espejob.get_left(),BLUE,onda3tracker)

        #ondas despues de espejo
        onda4tracker=ValueTracker(0)
        onda4=onda_vertabajo(splitter.get_top(),espejoa.get_bottom(),BLUE,onda4tracker,difface=2)
        onda5tracker=ValueTracker(3.1)
        #onda5segundotracker=ValueTracker(1) ,segundotracker=onda5segundotracker
        onda5=onda_regreso(espejob.get_left(),splitter.get_right(),BLUE,onda5tracker,difface=2)

        onda6tracker=ValueTracker(0)
        onda6=onda_vertabajo(pantalla.get_top(),splitter.get_bottom(),BLUE,onda6tracker,difface=2)
        onda7tracker=ValueTracker(0)
        onda7=onda_vertabajo(pantalla.get_top(),splitter.get_bottom(),BLUE,onda7tracker,difface=0)

        #láser
        self.add(fuente,splitter,espejoa,espejob,pantalla)
        self.play(Create_wave(fuente))
        self.play(Create_wave(fuente))
        self.play(ReplacementTransform(fuente,laser))
        self.play(Create(onda1),run_time=1.5,rate_func=linear)
        self.play(Create(onda2),Create(onda3),onda1tracker.animate.set_value(5.157),run_time=1.5,rate_func=linear)
        self.remove(onda1)
        self.add(onda5)
        self.play(onda2tracker.animate.set_value(3.1),onda3tracker.animate.set_value(3.1)
                  ,Create(onda4),onda5tracker.animate.set_value(0),run_time=1.5,rate_func=linear)
        self.remove(onda2,onda3,onda5)


        self.play(onda4tracker.animate.set_value(3.1), Uncreate(onda5),Create(onda6),Create(onda7), run_time=1.5,rate_func=linear)
        self.remove(onda4)

        self.play(onda6tracker.animate.set_value(3.1),onda7tracker.animate.set_value(3.1),run_time=1.5,rate_func=linear)
        self.remove(onda6,onda7)

        self.wait()
        self.play(FadeOut(laser),FadeOut(splitter),FadeOut(espejoa),FadeOut(espejob),FadeOut(pantalla))
        
        
    def hyperbolic(self):
        #modo es el lambda y d es el valuetracker de la distancia
        def hyperbolic_mobject(modo,d, COLOR=RED):
            #d es un value tracker de la distancia entre los dos puntos
            hyperbola=ImplicitFunction(
                lambda x,y: np.sqrt((d.get_value()+x)**2 + y**2) - np.sqrt((d.get_value()-x)**2 + y**2) - modo/2
            ).set_color(COLOR)
            
            hyperbolamirror=ImplicitFunction(
                lambda x,y: np.sqrt((d.get_value()+x)**2 + y**2) - np.sqrt((d.get_value()-x)**2 + y**2) + modo/2
            ).set_color(COLOR)
            
            hyperbola.add_updater(lambda m: m.become(
                ImplicitFunction(
                lambda x,y: np.sqrt((d.get_value()+x)**2 + y**2) - np.sqrt((d.get_value()-x)**2 + y**2) - modo/2
            ).set_color(COLOR)
                
            ))
            hyperbolamirror.add_updater(lambda m: m.become(
                ImplicitFunction(
                lambda x,y: np.sqrt((d.get_value()+x)**2 + y**2) - np.sqrt((d.get_value()-x)**2 + y**2) + modo/2
            ).set_color(COLOR)
            ))
            hyperbolas=VGroup(hyperbola,hyperbolamirror)
            
            return hyperbolas
        
        d=ValueTracker(1.4)
        fuente1=Dot(color=BLUE).shift(1.4*RIGHT)
        fuente2=Dot(color=BLUE).shift(1.4*LEFT)

        self.play(Create(fuente1),Create(fuente2))

        mobjects=VGroup(hyperbolic_mobject(0.5,d),hyperbolic_mobject(1,d),hyperbolic_mobject(1.5,d)
        , hyperbolic_mobject(2,d), hyperbolic_mobject(2.5, d), hyperbolic_mobject(3, d), hyperbolic_mobject(3.5, d),
        hyperbolic_mobject(4, d), hyperbolic_mobject(4.5, d), hyperbolic_mobject(5, d), hyperbolic_mobject(5.5, d))

        self.wait()
        self.play(Create(mobjects))
        
        
        self.play(d.animate.set_value(3),fuente1.animate.move_to(1.5*RIGHT),fuente2.animate.move_to(1.5*LEFT))

        self.wait()

        self.play(d.animate.set_value(4),fuente1.animate.move_to(2*RIGHT), fuente2.animate.move_to(2*LEFT))
        


