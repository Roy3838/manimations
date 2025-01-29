from manim import *
import numpy as np

# Set vertical aspect ratio
width = 1080
height = 1920
config.frame_size = [width, height]

class Michelson(MovingCameraScene):
    def construct(self):

        self.camera.background_color = "#E2E2E2"

        self.camera.frame.scale(0.6)

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
        # Pure jenk
        laser2 = Rectangle(height=0.2,width=1,color=BLACK).shift(LEFT*4)
        laser2.set_fill(BLUE,opacity=0.7)

        #splitter de en medio
        splitter=Rectangle(height=0.1,width=0.7,color=GREY).rotate(PI/4)
        #los dos espejos, el a es el de arriba y el b el de abajo
        espejoa=Rectangle(height=0.1,width=0.7,color=GREY_D).shift(3.5*UP)
        espejob=Rectangle(height=0.1,width=0.7,color=GREY_D).shift(3.5*RIGHT).rotate(PI/2)
        #pantalla de observación de abajo
        pantalla=Rectangle(height=0.1,width=5,color=BLACK).move_to(DOWN*3.5)
        #onda antes de splitter
        onda1tracker=ValueTracker(0)
        onda1=onda(laser2.get_right(),splitter.get_left(),BLUE,onda1tracker)

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
        self.add(splitter,espejoa,espejob,pantalla,laser,laser2)
        # self.play(Create_wave(fuente))
        # self.play(Create_wave(fuente))
        # self.play(ReplacementTransform(fuente,laser))
        t=0.5
        self.play(Create(onda1),run_time=t,rate_func=linear)
        self.play(Create(onda2),Create(onda3),onda1tracker.animate.set_value(3.157),run_time=t,rate_func=linear)
        self.remove(onda1)
        self.add(onda5)
        self.play(onda2tracker.animate.set_value(3.1),onda3tracker.animate.set_value(3.1)
                ,Create(onda4),onda5tracker.animate.set_value(0),run_time=t,rate_func=linear)
        self.remove(onda2,onda3,onda5)


        self.play(onda4tracker.animate.set_value(3.1), Uncreate(onda5),Create(onda6),Create(onda7), run_time=t,rate_func=linear)
        self.remove(onda4)

        self.play(onda6tracker.animate.set_value(3.1),onda7tracker.animate.set_value(3.1),run_time=t,rate_func=linear)
        self.remove(onda6,onda7)

        

        self.wait()
        self.play(FadeOut(laser),FadeOut(splitter),FadeOut(espejoa),FadeOut(espejob),FadeOut(pantalla), FadeOut(laser2))
 
