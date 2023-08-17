from manim import *



class Thumbnail(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        def onda(pos1, pos2, color, difface=0, periodo=8, amplitud=0.2, override=0):
            if override == 0:
                override = pos2
            elif override == 1:
                override = pos1

            length = np.sqrt(np.power(pos1[0] - pos2[0], 2) + np.power(pos1[1] - pos2[1], 2))
            sound2 = ParametricFunction(
                lambda t: np.array((t, amplitud * np.sin(periodo * (t + difface)), 0)),
                t_range=np.array([0, length]), fill_opacity=0
            ).set_color(color)

            sound2.rotate(
                np.arctan((pos1[1] - pos2[1]) / (pos1[0] - pos2[0])), about_point=pos1
            )
            sound2.align_to(override, direction=RIGHT)
            return sound2

        def onda_vert(pos1, pos2, color, difface=0, periodo=8, amplitud=0.2):
            length = np.sqrt(np.power(pos1[0] - pos2[0], 2) + np.power(pos1[1] - pos2[1], 2))
            sound2 = ParametricFunction(
                lambda t: np.array((t, amplitud * np.sin(periodo * (t + difface)), 0)),
                t_range=np.array([0, length]), fill_opacity=0
            ).set_color(color)

            sound2.rotate(
                np.arctan((pos1[1] - pos2[1]) / (pos1[0] - pos2[0])), about_point=pos1
            )
            sound2.move_to([(pos1[0] + pos2[0]) / 2, (pos1[1] + pos2[1]) / 2, 0])
            return sound2

        def onda_vertabajo(pos1, pos2, color, difface=0, periodo=8, amplitud=0.2):
            length = np.sqrt(np.power(pos1[0] - pos2[0], 2) + np.power(pos1[1] - pos2[1], 2))
            sound2 = ParametricFunction(
                lambda t: np.array((t, amplitud * np.sin(periodo * (t + difface)), 0)),
                t_range=np.array([0, length]), fill_opacity=0
            ).set_color(color)

            sound2.rotate(
                np.arctan((pos1[1] - pos2[1]) / (pos1[0] - pos2[0])), about_point=pos1
            )
            sound2.move_to([(pos1[0] + pos2[0]) / 2, (pos1[1] + pos2[1]) / 2, 0])
            return sound2

        def onda_regreso(pos1, pos2, color, difface=0, periodo=8, amplitud=0.2, override=0):
            length = np.sqrt(np.power(pos1[0] - pos2[0], 2) + np.power(pos1[1] - pos2[1], 2))
            sound2 = ParametricFunction(
                lambda t: np.array((t, amplitud * np.sin(periodo * (t + difface)), 0)),
                t_range=np.array([0, length]), fill_opacity=0
            ).set_color(color)

            sound2.rotate(
                np.arctan((pos1[1] - pos2[1]) / (pos1[0] - pos2[0])), about_point=pos1
            )
            sound2.move_to([(pos1[0] + pos2[0]) / 2, (pos1[1] + pos2[1]) / 2, 0])
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
        onda1=onda(laser.get_right(),splitter.get_left(),BLUE,difface=0)
        # ondas despues de splitter (onda pa riba y luego pa derecha)
        onda2 = onda_vert(espejoa.get_bottom(), splitter.get_top(), BLUE, difface=0)
        onda3 = onda(splitter.get_right(), espejob.get_left(), BLUE, difface=0)

        # ondas despues de espejo
        onda4 = onda_vertabajo(splitter.get_top(), espejoa.get_bottom(), BLUE, difface=2)
        onda5 = onda_regreso(espejob.get_left(), splitter.get_right(), BLUE, difface=2 + 3.1)  # Summed the tracker value with difface

        onda6 = onda_vertabajo(pantalla.get_top(), splitter.get_bottom(), BLUE, difface=2)
        onda7 = onda_vertabajo(pantalla.get_top(), splitter.get_bottom(), BLUE, difface=0)



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
        pantallay=Rectangle(height=8,width=0.2,color=BLACK).move_to(RIGHT*6)

        radius = 7
        radiusfinal=9
        wave1=Circle(radius=radius,color=BLUE).move_to(fuente1.get_center()).set_opacity((1-(1/radiusfinal)*radius))

        radiusfinal=8
        radius = 6
        wave2= Arc(radius=radius,start_angle=-90*DEGREES,angle=PI,color=BLUE).align_to(fuente2,direction=LEFT).set_opacity((1-(1/radiusfinal)*radius)).set_y(fuente2.get_y())
        
        radiusfinal=8
        radius = 6
        wave3= Arc(radius=radius,start_angle=-90*DEGREES,angle=PI,color=BLUE).align_to(fuente3,direction=LEFT).set_opacity((1-(1/radiusfinal)*radius)).set_y(fuente3.get_y())
        
        
        young=VGroup(fuente1,fuente2,fuente3,rejilla1,rejilla2,rejilla3,pantallay, wave1, wave2, wave3)
        young.shift(UP*5+ LEFT*10).scale(0.7)

        # Thumbnail arrow
        arrow = Arrow(UP+LEFT, ORIGIN, color=RED, stroke_width=30).move_to(UP*3+ LEFT*5)
        arrow.tip.scale(3)
        arrow.scale(3)

        the_same = Text("The Same!", color=BLACK).move_to(UP*6+ LEFT).scale(3)

        young_michelson=Text("Young = Michelson", color=BLACK).move_to(DOWN*3+LEFT*10).scale(1.5)



        #láser

        self.camera.frame.shift(UP*2+LEFT*6).scale(1.5)

        self.add(# Michelson
                splitter,espejoa,espejob,pantalla,
                 laser,onda1,onda2,onda3,onda4,onda5,onda6,onda7,
                 
                 # Young
                 young,

                 arrow,
                 the_same,
                    young_michelson
                 )
