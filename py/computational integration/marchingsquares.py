
from manim import *
import itertools as it



class MarchingSquares(ThreeDScene):
    def construct(self):


        # Makes a manim marching square algorithm
        # Takes an implicit function that is equal to 0 
        def marching_square_algorithm(function, x_range, y_range, z_range, resolution):
            xs=(x_range[1]-x_range[0])/resolution
            ys=(y_range[1]-y_range[0])/resolution
            zs=(z_range[1]-z_range[0])/resolution
            fig=VGroup()
            for i in np.arange(x_range[0],x_range[1],xs):
                print(i)
                for j in np.arange(y_range[0],y_range[1],ys):
                    for k in np.arange(z_range[0],z_range[1],zs):
                        #points of the square
                        #scan=Cube(side_length=xs,fill_opacity=0.8,fill_color=YELLOW).move_to([i,j,k])
                        #self.play(Create(scan),run_time=0.07)
                        #self.wait(0.08)
                        if function(i,j,k)*function(i+xs,j+ys,k+zs) < 0:
                            cubo=Cube(side_length=xs,fill_opacity=0.5,fill_color=BLUE_C)
                            cubo.shift(i*RIGHT+j*UP+k*OUT)
                            #self.play(Write(cubo),run_time=0.01)

                            fig.add(cubo)
                        
            return fig         
                            


        
        self.camera.background_color = "#E2E2E2"
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(ThreeDAxes().set_color(BLACK))
        figura = marching_square_algorithm(lambda x,y,z: x**2+y**2+z**2 - 5,[-2.5,2.5],[-2.5,2.5],[-2.5,2.5],30)
        #self.play(Write(fig))
        self.play(Create(figura))
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(PI)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait(2)
        






            
        



