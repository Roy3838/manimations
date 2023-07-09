from manim import *

class Lens(VMobject):
    def __init__(self, radius=2, curvature=0.8, fill_opacity=0.5, fill_color=BLUE, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.curvature = curvature
        self.fill_opacity = fill_opacity
        self.fill_color = fill_color

        self.create_lens()

    def create_lens(self):
        lens_left = Circle(radius=self.radius, arc_center=(-self.curvature*self.radius, 0, 0))
        lens_right = Circle(radius=self.radius, arc_center=(self.curvature*self.radius, 0, 0))

        lens = Intersection(lens_left, lens_right, color=self.fill_color, fill_opacity=self.fill_opacity)
        self.add(lens)

    def get_intersection_points(self, circle_1, circle_2):
        distance_between_centers = np.linalg.norm(circle_2.get_center() - circle_1.get_center())

        d = distance_between_centers
        r1, r2 = circle_1.radius, circle_2.radius
        a = (r1**2 - r2**2 + d**2) / (2 * d)

        h = np.sqrt(r1**2 - a**2)
        c1, c2 = circle_1.get_center(), circle_2.get_center()
        
        x2, y2 = c2[0], c2[1]
        x3 = c1[0] + a * (x2 - c1[0]) / d
        y3 = c1[1] + a * (y2 - c1[1]) / d

        x4_1 = x3 + h * (y2 - c1[1]) / d
        y4_1 = y3 - h * (x2 - c1[0]) / d

        x4_2 = x3 - h * (y2 - c1[1]) / d
        y4_2 = y3 + h * (x2 - c1[0]) / d

        return np.array([[x4_1, y4_1, 0], [x4_2, y4_2, 0]])

class DivergingLens(VMobject):
    def __init__(self, radius=1.8, curvature=1.3, fill_opacity=0.5, fill_color=BLUE, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.curvature = curvature
        self.fill_opacity = fill_opacity
        self.fill_color = fill_color

        self.create_lens()

    def create_lens(self):
        lens_left = Circle(radius=self.radius, arc_center=(-self.radius/1.2*self.curvature, 0, 0))
        lens_right = Circle(radius=self.radius, arc_center=(self.radius/1.2*self.curvature, 0, 0))
        square = Square().scale(self.radius*2/3)

        circulos = Union(lens_left, lens_right, color=self.fill_color, fill_opacity=self.fill_opacity)
        lens = Difference(square, circulos, fill_opacity=self.fill_opacity, color=self.fill_color)

        self.add(lens)
  
class LensAnimation(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        
        
        lens = Lens()
        line1 = Line(LEFT * 3 + UP/2, UP/2 + LEFT * 0.1).set_color(GOLD)
        line2 = Line(LEFT * 3 + DOWN/2, DOWN/2 + LEFT * 0.1).set_color(GOLD)

        refracted_line1 = self.calculate_refracted_ray(line1.get_end(), lens)
        refracted_line2 = self.calculate_refracted_ray(line2.get_end(), lens)
        
        self.play(Create(lens), Create(line1.shift(LEFT*0.3)), Create(line2.shift(LEFT*0.3)))
        
        self.wait()
                
        diverging_lens = DivergingLens().shift(RIGHT * 2.85)
        
        self.play(Create(diverging_lens))
        
        self.wait()
        
        self.play(Transform(line1, refracted_line1), Transform(line2, refracted_line2))
        
        self.wait()
        
        refracted_line1_diverging = self.calculate_refracted_ray(line1.get_end(), diverging_lens).shift(RIGHT*0.6)
        refracted_line2_diverging = self.calculate_refracted_ray(line2.get_end(), diverging_lens).shift(RIGHT*0.6)

        self.play(Transform(line1, refracted_line1_diverging), Transform(line2, refracted_line2_diverging))

        self.wait()

    def calculate_refracted_ray(self, point, lens):
        buff = 0.4  # Buffer distance to avoid lines going inside the lenses
        start_point = point + buff * RIGHT
        end_point = point + (2 * buff) * LEFT
        
        n1, n2 = 1, 4  # Refractive indices (air and lens material)

        # Find the normal vector to the lens surface at the intersection point
        curvature_center = np.array([lens.curvature * lens.radius, 0, 0])
        normal = point - curvature_center
        normal = normal / np.linalg.norm(normal)

        # Calculate the incident ray direction
        incident_ray = point - LEFT * 3
        incident_ray = incident_ray / np.linalg.norm(incident_ray)

        # Calculate the angle of incidence using the dot product
        cos_incidence_angle = np.dot(normal, incident_ray)
        incidence_angle = np.arccos(cos_incidence_angle)

        # Calculate the angle of refraction using Snell's Law
        refraction_angle = np.arcsin(n1 * np.sin(incidence_angle) / n2)

        # Calculate the refracted ray direction
        refracted_ray = np.dot(incident_ray, np.cos(refraction_angle)) - np.dot(normal, np.sin(refraction_angle))

        # Create the refracted ray as a Line object
        refracted_line = Line(start_point, end_point + refracted_ray * 3, color=GOLD)

        return refracted_line
    

if __name__ == "__main__":
    from manim import *
    scene = LensAnimation()
    scene.render()