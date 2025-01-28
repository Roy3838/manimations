from manim import *
import numpy as np
from itertools import combinations_with_replacement
from manim import *
import numpy as np
from itertools import combinations_with_replacement


# Set vertical aspect ratio
width = 1080
height = 1920
config.frame_size = [width, height]


class SmoothWiggle(Animation):
    def __init__(self, mobject, amplitude=0.05, angular_frequency=0.1, **kwargs):
        self.amplitude = amplitude
        self.angular_frequency = angular_frequency
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        time = alpha * self.run_time
        for particle, center in zip(self.mobject, self.mobject.site_centers):
            offset = self.amplitude * np.array([
                np.sin(self.angular_frequency * time + np.random.random() * 2 * np.pi),
                np.cos(self.angular_frequency * time + np.random.random() * 2 * np.pi),
                0
            ])

            particle.move_to(center + UP*0.2 + offset + particle.last_offset)
            particle.last_offset = offset

class BoseHubbardModel(MovingCameraScene):

    def construct(self):
        self.camera.background_color = "#E2E2E2"

        self.camera.frame.scale(0.5)
        self.boxes_animation()

    def generate_combinations(self, M, N):
        sites = range(M)
        return [self.count_occurrences(combo, M) for combo in combinations_with_replacement(sites, N)]

    def count_occurrences(self, combo, M):
        return [combo.count(i) for i in range(M)]

    def combination_to_dirac(self, combination):
        return r"$|" + ",".join(map(str, combination)) + r"\rangle$"

    def boxes_animation(self):
        M = 4  # Number of sites
        N = 3  # Number of particles

        # WIGGLE_SPEED = 0.01  # Adjust this value to change the wiggle speed (lower = slower)


        sites = VGroup()

        for i in range(M):
            sites.add(Text("]", color=BLACK).rotate(-PI/2).shift(i*RIGHT))
        sites.shift(M*(LEFT/2))
        self.add(sites)

        combinations = self.generate_combinations(M, N)
        initial_combinations = [
            [1,1,1,0],
            [1,2,0,0],
            [1,1,1,0],
            [0,2,1,0],
            [0,2,0,1],
            [1,1,0,1]
        ]

        def create_particles(combination):


            def color_gradient(colors, n_colors):
                if n_colors == 1:
                    return colors[:1]
                
                rgb_colors = [color_to_rgb(c) for c in colors]
                gradient = []
                
                for i in range(n_colors):
                    t = i / (n_colors - 1)
                    avg_color = [
                        sum(c[j] * (1-t) + rgb_colors[-1][j] * t for c in rgb_colors[:-1]) / (len(rgb_colors) - 1)
                        for j in range(3)
                    ]
                    gradient.append(rgb_to_color(avg_color))
                
                return gradient




            particles = VGroup()
            site_centers = []
            particle_index = 0
            total_particles = sum(combination)
            
            # Create a color gradient from light blue to dark blue
            color_gradient = color_gradient([BLUE_C, BLUE_E], total_particles)

            for i, count in enumerate(combination):
                for _ in range(count):
                    site_center = sites[i].get_center()
                    particle = Dot(color=color_gradient[particle_index]).move_to(site_center + UP*0.2)
                    particle.particle_index = particle_index
                    particle.last_offset = 0
                    particles.add(particle)
                    site_centers.append(site_center + UP*0.2)
                    particle_index += 1
            particles.site_centers = site_centers
            return particles


        # Animate initial combinations
        for combination in initial_combinations:
            particles = create_particles(combination)
            self.add(particles)
            self.play(SmoothWiggle(particles, run_time=2, ))
            self.remove(particles)

        for combination in combinations:
            particles = create_particles(combination)
            # Use the template and MathTex
            basis_vector = Tex(
                self.combination_to_dirac(combination),
                color=BLACK,
            ).scale(2)
            basis_vector.move_to(DOWN+LEFT*0.35)

            self.add(particles, basis_vector)
            self.play(SmoothWiggle(particles, run_time=0.4))
            self.remove(particles, basis_vector)

        self.wait()
