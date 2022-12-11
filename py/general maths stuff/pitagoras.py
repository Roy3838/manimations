# from tkinter import CENTER
from manim import *

width=1080
height=1920
# config.pixel_width = width
# config.pixel_height = height
config.frame_size = [width, height]
class pitagoras(MovingCameraScene):
    def construct(self):
        #change background color to gray
        self.camera.background_color = "#E2E2E2"
        self.camera.frame.scale(0.5)
        #watermark
        watermark=MathTex(r"\mathbb{R}euler", color=GRAY_D, fill_opacity=0.3).scale(1).move_to(RIGHT*2.5 + DOWN*5)
        self.add(watermark)
        
        #zoom on the camera
        

        #rotation matrix for vector [0,1],[-1,0]
        rotation_matrix=np.array([[0,1],[-1,0]])
        def makesquare(pos1,pos2,fill_color=BLUE,lines_color=BLACK):
            #makes a square with the dimentions points pos1 and pos2, aligns the side with the line pos1-pos2

            #square side 1,2 not element wise

            distance=np.sqrt(np.sum(np.square(pos1-pos2)))
            square = Square(side_length=distance, fill_opacity=0.6, fill_color=fill_color, color=lines_color)

            pos1_2d=np.array([pos1[0],pos1[1]])
            pos2_2d=np.array([pos2[0],pos2[1]])

            #place between the two points
            between=(pos1_2d+pos2_2d)/2
            centerofsquare=between + -np.dot(rotation_matrix,((pos1_2d-pos2_2d)/2))

            square.shift([centerofsquare[0],centerofsquare[1],0])

            #angle of rotation
            angle=np.arctan2(pos1_2d[1]-pos2_2d[1],pos1_2d[0]-pos2_2d[0])

            square.rotate(angle)

            return square


        """ General build struff """
        #be careful with the order of the triangle, start with square angle, go clockwise o idk ahi veo

        pos1=np.array([-1,-1, 0])
        pos2=np.array([ 1,-1, 0])
        pos3=np.array([-1, 0, 0])

        #pos1 is the vecvtor of the cathetus

        #pos2 is the vector of the long cathetus and hypotenuse

        #pos3 is the vector of the short cathetus and hypotenuse

        #make triangle
        triangle = Polygon(pos1,pos2,pos3).set_color(BLACK)



        #make squares of the sides of triangle
        catetogrande=makesquare(pos1,pos2)
        hypothenuse=makesquare(pos2,pos3,RED)
        catetochico=makesquare(pos3,pos1)

        """ Intro Scene"""
        a=MathTex("a",color=BLACK).move_to([-1.3,-0.5,0])
        b=MathTex("b",color=BLACK).move_to([0,-1.3,0])
        c=MathTex("c",color=BLACK).move_to([0,-0.15,0])

        a1=a.copy()
        a2=a.copy()
        a3=a.copy()
        b1=b.copy()
        b2=b.copy()
        b3=b.copy()
        c1=c.copy()
        c2=c.copy()
        c3=c.copy()
        asquared=MathTex("a^2",color=BLACK).move_to(catetochico.get_center())
        bsquared=MathTex("b^2",color=BLACK).move_to(catetogrande.get_center())
        csquared=MathTex("c^2",color=BLACK).move_to(hypothenuse.get_center())


        """ Sum of squares scene """
        squarea=catetochico.copy()
        squareb=catetogrande.copy()
        squarec=hypothenuse.copy()

        squarea.move_to(LEFT*3)
        squareb.move_to(LEFT)
        squarec.move_to(RIGHT*2)

        suma=Tex("+").move_to(LEFT*2.25).set_color(BLACK)
        igual=Tex("=").set_color(BLACK).move_to(RIGHT*0.3)



        pos1_2d=np.array([pos1[0],pos1[1]])
        pos2_2d=np.array([pos2[0],pos2[1]])
        pos3_2d=np.array([pos3[0],pos3[1]])

        """ Trapezoid Area Scene """

        #trapezoid shift 1
        areasquare=Polygon([-1,1,0],[1,1,0],[1,-1,0],[-1,-1,0],color=BLACK,fill_color=BLUE,fill_opacity=0.6)
        areatrapezoind=Polygon([0,1,0],[2,1,0],[1,-1,0],[-1,-1,0],color=BLACK,fill_color=BLUE,fill_opacity=0.6)
        triangleoffset=Polygon([1,1,0],[1,-1,0],[2,1,0],color=BLACK)
        triangleoffset2=Polygon([-1,1,0],[-1,-1,0],[0,1,0],color=BLACK)

        #trapezoid shift 2
        areatrapezoind2=Polygon([1,1,0],[3,1,0],[1,-1,0],[-1,-1,0],color=BLACK,fill_color=BLUE,fill_opacity=0.6)
        triangleoffset3=Polygon([1,1,0],[1,-1,0],[3,1,0],color=BLACK)
        triangleoffset4=Polygon([-1,1,0],[-1,-1,0],[1,1,0],color=BLACK)

        #original square
        ogsquare=Polygon([-1,1,0],[1,1,0],[1,-1,0],[-1,-1,0],color=GOLD)
        ogsquare2=Polygon([-1,1,0],[1,1,0],[1,-1,0],[-1,-1,0],color=GOLD)



        """ Equation Scene """

        # atext=Tex(r"\a^{2}").move_to(catetogrande.get_top()+UP*0.5).set_color(BLACK)
        # btext=Tex(r" b ").move_to(catetochico.get_right()+RIGHT*0.5).set_color(BLACK)
        # ctext=Tex(r"\c^{2}").move_to(hypothenuse.get_bottom()+DOWN*0.5).set_color(BLACK)

        #equation=Tex(r"\a^{2}", r"+", " b ", r"=",r"\c^{2}").move_to(UP*3+RIGHT*3).set_color(BLACK)

        ecuacion=MathTex(r"a^{2}","+",r"b^{2}","=" ,r"c^{2}").set_color(BLACK).move_to(3*UP)

        frameboxa=SurroundingRectangle(ecuacion[0],color=GOLD,buff=0.1)
        frameboxb=SurroundingRectangle(ecuacion[2],color=GOLD,buff=0.1)
        frameboxc=SurroundingRectangle(ecuacion[4],color=GOLD,buff=0.1)

        framebox_cuadro_a=SurroundingRectangle(squarea,color=GOLD,buff=0.2)
        framebox_cuadro_b=SurroundingRectangle(squareb,color=GOLD,buff=0.2)
        framebox_cuadro_c=SurroundingRectangle(squarec,color=GOLD,buff=0.1)

        """ Final Scene """
        #lines that mark the cathetus vector
        vector = pos1_2d + -np.dot(rotation_matrix,(pos1_2d-pos2_2d)) + np.dot(rotation_matrix,(pos1_2d-pos3_2d))
        

        vector = [vector[0],vector[1],0]


        vector1=Line([pos1[0],vector[1],0], vector).set_color(BLACK)
        vector2=Line([vector[0],pos1[1],0], vector).set_color(BLACK)


        #prueba=ValueTracker([0,0,0])
        
        #solving the linear algebra equations to get the values of t and s to know where the point is
        #using cramers rule
        A=np.array([[pos1[0]-vector[0], -(pos3[0]-pos2[0])],[pos1[1]-vector[1], -(pos3[1]-pos2[1])]])
        B=np.array([pos2[0]-vector[0], pos2[1]-vector[1]])
        t,s=np.linalg.solve(A,B)

        #point on the line hypotenuse of the triangle
        point=np.array(vector + t*(pos1-vector))
        extra=np.dot(rotation_matrix,(pos2_2d-pos3_2d))
        extra=[extra[0],extra[1],0]
        pointdivisor=point-extra

        division=Line(vector,pointdivisor).set_color(BLACK)
        
        #poligono
        puntopol1=np.array(vector+(pos3-pos1))
        puntopol2=np.array(vector+(pos2-pos1))

        #esquinas
        puntoesquinaizquierda=pos3-extra
        puntoesquinadercha=pos2-extra

        fill_color=BLUE
        lines_color=BLACK

        pol1=Polygon(puntopol1,vector,pos1,pos3,fill_opacity=0.6, fill_color=fill_color, color=lines_color)
        pol2=Polygon(vector,puntopol2,pos2,pos1,fill_opacity=0.6, fill_color=fill_color, color=lines_color)

        #poligonos finales
        pol1final=Polygon(pos3,point,pointdivisor,puntoesquinaizquierda,fill_opacity=0.6, fill_color=fill_color, color=lines_color)
        pol2final=Polygon(point,pos2,puntoesquinadercha,pointdivisor,fill_opacity=0.6, fill_color=fill_color, color=lines_color)

        #escena final
        catetochicofinal=catetochico.copy()
        catetograndefinal=catetogrande.copy()
        hypothenusefinal=hypothenuse.copy()


        """ GENERALIZING SCENE """

        #generalizing the proof to any triangle

        def make_proof(dim=[np.array([-1,-1, 0]),np.array([ 1,-1, 0]),np.array([-1, 0, 0])], offset=[0,0,0]):
            pos1=dim[0] + offset
            pos2=dim[1] + offset
            pos3=dim[2] + offset
            triangle = Polygon(pos1,pos2,pos3).set_color(BLACK)
            catetogrande=makesquare(pos1,pos2)
            hypothenuse=makesquare(pos2,pos3,RED)
            catetochico=makesquare(pos3,pos1)
            pos1_2d=np.array([pos1[0],pos1[1]])
            pos2_2d=np.array([pos2[0],pos2[1]])
            pos3_2d=np.array([pos3[0],pos3[1]])
            vector = pos1_2d + -np.dot(rotation_matrix,(pos1_2d-pos2_2d)) + np.dot(rotation_matrix,(pos1_2d-pos3_2d))
            

            vector = [vector[0],vector[1],0]


            vector1=Line([pos1[0],vector[1],0], vector).set_color(BLACK)
            vector2=Line([vector[0],pos1[1],0], vector).set_color(BLACK)


            #prueba=ValueTracker([0,0,0])
            
            #solving the linear algebra equations to get the values of t and s to know where the point is
            #using cramers rule
            A=np.array([[pos1[0]-vector[0], -(pos3[0]-pos2[0])],[pos1[1]-vector[1], -(pos3[1]-pos2[1])]])
            B=np.array([pos2[0]-vector[0], pos2[1]-vector[1]])
            t,s=np.linalg.solve(A,B)

            #point on the line hypotenuse of the triangle
            point=np.array(vector + t*(pos1-vector))
            extra=np.dot(rotation_matrix,(pos2_2d-pos3_2d))
            extra=[extra[0],extra[1],0]
            pointdivisor=point-extra

            division=Line(vector,pointdivisor).set_color(BLACK)
            
            #poligono
            puntopol1=np.array(vector+(pos3-pos1))
            puntopol2=np.array(vector+(pos2-pos1))

            #esquinas
            puntoesquinaizquierda=pos3-extra
            puntoesquinadercha=pos2-extra

            fill_color=BLUE
            lines_color=BLACK

            pol1=Polygon(puntopol1,vector,pos1,pos3,fill_opacity=0.6, fill_color=fill_color, color=lines_color)
            pol2=Polygon(vector,puntopol2,pos2,pos1,fill_opacity=0.6, fill_color=fill_color, color=lines_color)

            #poligonos finales
            pol1final=Polygon(pos3,point,pointdivisor,puntoesquinaizquierda,fill_opacity=0.6, fill_color=fill_color, color=lines_color)
            pol2final=Polygon(point,pos2,puntoesquinadercha,pointdivisor,fill_opacity=0.6, fill_color=fill_color, color=lines_color)
            

            return [triangle,catetogrande,hypothenuse,catetochico,vector1,vector2,division,pol1,pol2,pol1final,pol2final]
        


        def debugging(tamanyo=0.3,color=RED):
            #debugging
            d1=Dot().move_to(pos1).scale(tamanyo).set_color(color)
            #pos1dt=Text("1").move_to(pos1 + UP*0.1).scale(0.3).set_color(RED)
            d2=Dot().move_to(pos2).scale(tamanyo).set_color(color)
            #pos2dt=Text("2").move_to(pos2 + UP*0.1).scale(0.3).set_color(RED)
            d3=Dot().move_to(pos3).scale(tamanyo).set_color(color)
            #pos3dt=Text("3").move_to(pos3 + UP*0.1).scale(0.3).set_color(RED)

            dotinterseccion=Dot().move_to(pointdivisor).scale(tamanyo).set_color(color)

            dt=Dot().move_to(vector).scale(tamanyo).set_color(color)
            #dt2=Text("vector").move_to(vector + UP*0.1).scale(0.5).set_color(RED)

            dotpol1=Dot().move_to(puntopol1).scale(tamanyo).set_color(color)
            dotpol2=Dot().move_to(puntopol2).scale(tamanyo).set_color(color)

            dots=VGroup(d1,d2,d3,dt,dotinterseccion,dotpol1,dotpol2)
            return dots

        
        """####################### ANIMATIONS START HERE #######################"""


        def Intro():
            #Introduction
            self.play(Write(triangle))
            self.play(
                Create(a),
                Create(b),
                Create(c)
            )
            self.play(Write(ecuacion.move_to(UP*3)))

            self.wait()
            self.play(
                Write(catetogrande),
                Write(hypothenuse),
                Write(catetochico),
                )
            self.play(
                #move a's
                a1.animate.shift(LEFT*0.2,UP*0.7),
                a2.animate.shift(LEFT),
                a3.animate.shift(DOWN*0.7,LEFT*0.2),
                a.animate.shift(RIGHT*0.5),

                #move b's
                b1.animate.shift(DOWN*2),
                b2.animate.shift(DOWN*0.7,LEFT*1.3),
                b3.animate.shift(DOWN*0.7,RIGHT*1.3),
                b.animate.shift(UP*0.6),

                #move c's
                c1.animate.shift(UP*1.85 + RIGHT*1.2),
                c2.animate.shift(UP*1.4+ LEFT*0.7),
                c3.animate.shift(RIGHT*1.75 + UP*0.2),
                c.animate.shift(DOWN*0.4 + LEFT*0.4),
            )
            self.wait()
            las_as=VGroup(a,a1,a2,a3)
            las_bs=VGroup(b,b1,b2,b3)
            las_cs=VGroup(c,c1,c2,c3)

            self.play(
                ReplacementTransform(las_as,asquared),
                ReplacementTransform(las_bs,bsquared),
                ReplacementTransform(las_cs,csquared),
            )
            self.wait()  

            self.play(
                FadeOut(triangle),
                FadeOut(asquared),
                FadeOut(bsquared),
                FadeOut(csquared)
            )
           
        def Equation():
        
            #Equation and squares scene
            ecuacion.move_to(UP*3)

            self.play(
                ReplacementTransform(catetochico,squarea),
                ReplacementTransform(catetogrande,squareb),
                ReplacementTransform(hypothenuse,squarec)
                )

            self.play(
                Create(suma),
                Create(igual)
            )

            self.wait()

            self.play(
                Create(frameboxa),
                Create(framebox_cuadro_a)
            )

            self.play(
                ReplacementTransform(frameboxa,frameboxb),
                ReplacementTransform(framebox_cuadro_a,framebox_cuadro_b)
            )

            self.play(
                ReplacementTransform(frameboxb,frameboxc),
                ReplacementTransform(framebox_cuadro_b,framebox_cuadro_c)
            )

            #Fade Out of Scene
            self.play(
                FadeOut(frameboxc),
                FadeOut(framebox_cuadro_c))
            self.play(
                FadeOut(squarea),
                FadeOut(squareb),
                FadeOut(squarec),
                FadeOut(suma),
                FadeOut(igual),
                FadeOut(ecuacion))
        
        def SameAreaScene():
            #Same Area Scene
            #make copies before ReplacementTransform to avoid the original object being modified
            areasquareog=areasquare.copy()
            areatrapezoindog=areatrapezoind.copy()

            #same area trapezoids
            self.play(Create(areasquare))
            #shift square
            self.play(ReplacementTransform(areasquare,areatrapezoind))

            self.wait()

            #show the area is the same 1
            self.play(Create(triangleoffset))
            self.play(ReplacementTransform(triangleoffset,triangleoffset2))
            self.play(Create(ogsquare))
            self.play(Uncreate(ogsquare))
            self.play(FadeOut(triangleoffset2))

            #show the area is the same 2
            self.play(ReplacementTransform(areatrapezoind,areatrapezoind2))
            self.play(Create(triangleoffset3))
            self.play(ReplacementTransform(triangleoffset3,triangleoffset4))
            self.play(Create(ogsquare2))
            self.play(Uncreate(ogsquare2))

            self.play(FadeOut(triangleoffset4))

            #equalsigns
            equalsign=MathTex("=").move_to(LEFT*1.1).set_color(BLACK)
            equalsign2=MathTex("=").move_to(RIGHT*1.1).set_color(BLACK)

            #show all Polygons
            self.play(areatrapezoind2.animate.move_to(RIGHT*2.3),run_time=0.5)
            self.play(
                Create(areasquareog.move_to(LEFT*2.3).scale(0.8)),
                Create(areatrapezoindog.move_to([0,0,0]).scale(0.8)),
                areatrapezoind2.animate.scale(0.8),
                Create(equalsign),
                Create(equalsign2)
                )

            self.wait(0.5)
            #Fade Out of Scene
            self.play(
                FadeOut(areasquareog),
                FadeOut(areatrapezoindog),
                FadeOut(areatrapezoind2),
                FadeOut(equalsign),
                FadeOut(equalsign2)
            )
        
        def FinalScene():
            #Show the final animation
            self.play(Write(triangle))
            self.wait()
            self.play(
                Write(catetograndefinal),
                Write(hypothenusefinal),
                Write(catetochicofinal))
            self.wait()
            self.play(Write(vector1),Write(vector2))

            self.play(Write(division))
            self.wait()
            self.play(
                ReplacementTransform(catetochicofinal,pol1),
                ReplacementTransform(catetograndefinal,pol2),
                FadeOut(vector1),
                FadeOut(vector2))
            self.wait()
            self.play(
                ReplacementTransform(pol1,pol1final),
                ReplacementTransform(pol2,pol2final),
                FadeOut(division),
                hypothenusefinal.animate.set_fill(opacity=0))

            self.wait()

            self.play(FadeOut(pol1final),FadeOut(pol2final),
            FadeOut(triangle),FadeOut(hypothenusefinal ))

        def Generalizing():

            
            #LaTeX MORADO
            # \left(4,-1\right),\left(5,-1\right),\left(4,1\right)
            #numpy arrays
            t1= [np.array([4,-1,0]), np.array([5,-1,0]), np.array([4,1,0])]

            #LaTeX VERDE
            # \left(-1,-1\right),\left(1,-1\right),\left(-1,0\right)
            #numpy arrays
            t2= [np.array([-1,-1,0]), np.array([1,-1,0]), np.array([-1,0,0])]

            #LaTeX ROJO
            # \left(-5,-1\right),\left(-4,-1\right),\left(-5,0\right)
            #numpy arrays
            t3 = [np.array([-5,-1,0]), np.array([-4,-1,0]), np.array([-5,0,0])]


            [triangle,catetogrande,hypothenuse,
            catetochico,vector1,vector2,division,
            pol1,pol2,pol1final,pol2final]=make_proof(t1, [-4.5,-4,0])

            [triangle1,catetogrande1,hypothenuse1,
            catetochico1,vector11,vector21,division1,
            pol11,pol21,pol1final1,pol2final1]=make_proof(t2 , [0,4.3,0])

            [triangle2,catetogrande2,hypothenuse2,
            catetochico2,vector12,vector22,division2,
            pol12,pol22,pol1final2,pol2final2]=make_proof(t3, [4.5,0,0])


            self.play(Write(triangle),Write(triangle1),Write(triangle2))
            self.play(
                Write(catetogrande),
                Write(hypothenuse),
                Write(catetochico),

                Write(catetogrande1),
                Write(hypothenuse1),
                Write(catetochico1),

                Write(catetogrande2),
                Write(hypothenuse2),
                Write(catetochico2))
            self.play(Write(vector1),Write(vector2),
                Write(vector11),Write(vector21),
                Write(vector12),Write(vector22))

            self.play(Write(division),Write(division1),Write(division2))
            self.play(
                ReplacementTransform(catetochico,pol1),
                ReplacementTransform(catetogrande,pol2),

                ReplacementTransform(catetochico1,pol11),
                ReplacementTransform(catetogrande1,pol21),

                ReplacementTransform(catetochico2,pol12),
                ReplacementTransform(catetogrande2,pol22),

                FadeOut(vector1),
                FadeOut(vector2),
                
                FadeOut(vector11),
                FadeOut(vector21),

                FadeOut(vector12),
                FadeOut(vector22))
            self.play(
                ReplacementTransform(pol1,pol1final),
                ReplacementTransform(pol2,pol2final),

                ReplacementTransform(pol11,pol1final1),
                ReplacementTransform(pol21,pol2final1),

                ReplacementTransform(pol12,pol1final2),
                ReplacementTransform(pol22,pol2final2),


                FadeOut(division),
                FadeOut(division1),
                FadeOut(division2),
                
                hypothenuse.animate.set_fill(opacity=0),
                hypothenuse1.animate.set_fill(opacity=0),
                hypothenuse2.animate.set_fill(opacity=0))
            self.play(FadeOut(pol1final),
                FadeOut(pol1final1),
                FadeOut(pol1final2),
                FadeOut(hypothenuse),
                FadeOut(hypothenuse1),
                FadeOut(hypothenuse2),
                FadeOut(triangle),
                FadeOut(triangle1),
                FadeOut(triangle2),
                FadeOut(pol2final),
                FadeOut(pol2final1),
                FadeOut(pol2final2))
            
            
        def Logo():
            self.remove(watermark)
            Reuler=MathTex(r"\mathbb{R}euler", color=GRAY_D).scale(3)
            self.play(Write(Reuler), run_time=3)
            self.wait()



        Intro()
        Equation()
        SameAreaScene()
        FinalScene()
        Generalizing()
        Logo()




