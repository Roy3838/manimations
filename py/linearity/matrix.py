from manim import *
import numpy as np

class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid", font_size=72)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        transorm_matrix = [[0,1],[1,1]]
        self.play(
            ApplyMatrix(transorm_matrix,grid),
            run_time=3,
        )
        self.play(
            ApplyMatrix(transorm_matrix,grid),
            run_time=3,
        )
        self.play(
            ApplyMatrix(transorm_matrix,grid),
            run_time=3,
        )
        
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        

        eigenmatrix = [[2,2],[1+np.sqrt(5), 1-np.sqrt(5)]]

        inveigenmatrix = np.linalg.inv(np.matrix(eigenmatrix))
            

        identity = np.matrix([[1,0],[0,1]])
        eigengrid = NumberPlane()
        

        
        self.play(FadeOut(grid, grid_transform_title))
        self.play(FadeIn(eigengrid))


        self.play(ApplyMatrix(eigenmatrix,eigengrid),run_time=3)
        self.wait(3)
        

        self.play(ApplyMatrix(2*identity,eigengrid),run_time=2)

        self.play(ApplyMatrix(inveigenmatrix,eigengrid),run_time=3)
        


        #self.remove(grid)
        
        
        
        self.wait()
