# from turtle import fillcolor, width
from manim import *
import numpy as np



class sphere(ThreeDScene):
    def construct(self):
        
        #from phase space to elipse dimensions
        def getelipse(S0,S1,S2,S3):
            p=np.sqrt(S1**2 + S2 ** 2 + S3**2)/S0
            chi=np.arcsin(S3/(p*S0))/2
            phi=np.arctan(S2/S1)/2
            a=np.sqrt(S0/(np.tan(chi)**2 + 1)   )
            b=a*np.tan(chi)
            return [a,b,phi]

        '''
        numberp = NumberPlane(
            x_range=(-6, 6, 1),
            y_range=(-6, 6, 1),
            background_line_style={
                "stroke_width": 4,
                "stroke_color": TEAL,
                "stroke_opacity": 0.5,
            })
        '''
        #S Space
        radius=2
        axes = ThreeDAxes(x_range=(-2, 2), y_range=(-2, 2), z_range=(-2, 2)).set_color(GREY)
        sphere = Surface(
            lambda u, v: np.array([
                radius * np.cos(u) * np.cos(v),
                radius * np.cos(u) * np.sin(v),
                radius * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],resolution=(30, 64),
            checkerboard_colors=[BLUE_D, BLUE_E]
        )
        '''
        x0=ValueTracker(0)
        y0=ValueTracker(0)
        z0=ValueTracker(0)
        vector=Arrow(ORIGIN,ORIGIN,buff=0)
        vector.add_updater(lambda v: v.become(Arrow(
            ORIGIN,UP,buff=0).rotate(z0.get_value(),OUT,about_point=ORIGIN
                                     ).rotate(y0.get_value(),RIGHT,about_point=ORIGIN
                                              ).rotate(x0.get_value(),UP,about_point=ORIGIN)
                                              ))
        '''
        
        
        z=0.001  
        S0=1
        S1=z
        S2=1
        S3=z
        a=ValueTracker(getelipse(S0,S1,S2,S3)[0])
        b=ValueTracker(getelipse(S0,S1,S2,S3)[1])
        phi=ValueTracker(getelipse(S0,S1,S2,S3)[2])
        
        pointx=ValueTracker(0)
        pointy=ValueTracker(1)
        pointz=ValueTracker(0)
        vector=Arrow(ORIGIN,ORIGIN,buff=0)
        vector.add_updater(lambda v: v.become(
            Arrow(ORIGIN,[pointx.get_value() * radius,pointy.get_value() * radius,pointz.get_value() * radius],buff=0,color=BLACK)
            ))
        

        #Matrix describing the S space
        S0_val=ValueTracker(S0)
        S1_val=ValueTracker(S1)
        S2_val=ValueTracker(S2)
        S3_val=ValueTracker(S3)
        S_space_matrix=IntegerMatrix([[S0],[S1],[S2],[S3]]).to_corner(DR).scale(0.6).set_color(BLACK)

        S_space_matrix.add_updater(lambda m: m.become(IntegerMatrix(
            [
            [np.round(S0_val.get_value(),2)],
            [np.round(S1_val.get_value(),2)],
            [np.round(S2_val.get_value(),2)],
            [np.round(S3_val.get_value(),2)]
            ]
        ).to_corner(DR).scale(0.6).set_color(BLACK)
        ))

        
        #GRAPH LIGHT
        graph = ImplicitFunction(
            lambda x, y: x**2/a.get_value()**2 + y**2/b.get_value()**2 - 1,
            color=GOLD
        ).move_to(UP*3 + RIGHT*6)
        graph.add_updater(lambda m: m.become(ImplicitFunction(
            lambda x, y: x**2/a.get_value()**2 + y**2/b.get_value()**2 - 1,
            color=GOLD
        ).rotate(phi.get_value()).move_to(UP*3 + RIGHT*6)
        ))

        #light
        dot=Dot(color=RED).scale(0.3).move_to(graph.get_center())
        arrow=Arrow(graph.get_center(),dot.get_center(), buff=0)
        arrow.add_updater(lambda a: a.become(Arrow(graph.get_center(),dot.get_center(), buff=0).set_color(GREY)))
        light=VGroup(dot,arrow)







        # ANIMATIONS
        def animatelight(S0,S1,S2,S3,self,n):
            self.play(a.animate.set_value(getelipse(S0,S1,S2,S3)[0]),
            b.animate.set_value(getelipse(S0,S1,S2,S3)[1]),
            phi.animate.set_value(getelipse(S0,S1,S2,S3)[2],

                                  ),
            #animación al mismo tiempo de la transformación de la elipse
                                pointx.animate.set_value(S1),
                                pointy.animate.set_value(S2),
                                pointz.animate.set_value(S3),

            #animacion de la matriz
                                S0_val.animate.set_value(S0),
                                S1_val.animate.set_value(S1),
                                S2_val.animate.set_value(S2),
                                S3_val.animate.set_value(S3),
            
            )
            self.add_fixed_in_frame_mobjects(light)
            for i in range(n):
                self.play(MoveAlongPath(dot, graph), run_time=2, rate_func=linear)
            self.remove(light)
                
            
            
        
        self.camera.background_color = "#ece6e2"
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.move_camera(frame_center=RIGHT*3)
        self.add_fixed_in_frame_mobjects(graph)
        self.add_fixed_in_frame_mobjects(S_space_matrix)
        self.add(axes,sphere,vector)
        
        #horizontal
        animatelight(S0,S1,S2,S3,self,2)
        
        #de lado
        animatelight(1,0.7,0.3,0.648,self,2)
        
        #circulo
        animatelight(1,z,z,1,self,2)

        #de lado
        animatelight(1,-0.7,-0.3,0.648,self,2)

        #vertical
        animatelight(1,1,z,z,self,2)
        

        

        
    

