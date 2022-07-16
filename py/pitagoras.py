from manim import *



class pitagoras(Scene):
    def construct(self):
        #change background color to gray
        self.camera.background_color = "#E2E2E2"

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


        """ Sum of squares scene """
        squarea=catetogrande.copy()
        squareb=catetochico.copy()
        squarec=hypothenuse.copy()

        squarea.move_to(LEFT*3.5)
        squareb.move_to(LEFT)
        squarec.move_to(RIGHT*2.5)

        suma=Tex("+").move_to(LEFT*2).set_color(BLACK)
        igual=Tex("=").set_color(BLACK).move_to(RIGHT*0.2)



        pos1_2d=np.array([pos1[0],pos1[1]])
        pos2_2d=np.array([pos2[0],pos2[1]])
        pos3_2d=np.array([pos3[0],pos3[1]])


        """ Equation Scene """

        # atext=Tex(r"\a^{2}").move_to(catetogrande.get_top()+UP*0.5).set_color(BLACK)
        # btext=Tex(r" b ").move_to(catetochico.get_right()+RIGHT*0.5).set_color(BLACK)
        # ctext=Tex(r"\c^{2}").move_to(hypothenuse.get_bottom()+DOWN*0.5).set_color(BLACK)

        #equation=Tex(r"\a^{2}", r"+", " b ", r"=",r"\c^{2}").move_to(UP*3+RIGHT*3).set_color(BLACK)




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
            
        debug=False
        if debug:
            dots=debugging(0.6)
            self.add(dots)

        self.play(Create(squarea),Create(squareb),Create(squarec),Create(suma),Create(igual))

        self.wait()

        #self.play(Write(atext),Write(btext)
        #,Write(ctext),Write(equation)
        #)

        self.play(Write(triangle))
        self.wait()
        self.play(Write(catetogrande),Write(hypothenuse),Write(catetochico))
        self.wait()
        self.play(Write(vector1),Write(vector2))

        self.play(Write(division))
        self.wait()
        self.play(ReplacementTransform(catetochico,pol1),ReplacementTransform(catetogrande,pol2),FadeOut(vector1),FadeOut(vector2))
        self.wait()
        self.play(ReplacementTransform(pol1,pol1final),ReplacementTransform(pol2,pol2final),FadeOut(division))

        self.wait()
