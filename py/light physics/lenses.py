from manim import *


class Lenses(Scene):
    def construct(self):
        
        
        def lens_transform(focal_point,impact_point):
            point1=impact_point
            point2=focal_point



            
            light_ray=Line(point1,point2)
            return light_ray


        
        self.add(Text("hello world"))



