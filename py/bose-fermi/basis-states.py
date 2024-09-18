from manim import *
import numpy as np
from itertools import combinations_with_replacement

class SmoothWiggle(Animation):
    def __init__(self, mobject, amplitude=0.1, angular_frequency=0.1, **kwargs):
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
            particle.move_to(center + UP*0.2 + offset)

class BoseHubbardModel(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
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

        WIGGLE_SPEED = 0.1  # Adjust this value to change the wiggle speed (lower = slower)


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
            particles = VGroup()
            site_centers = []
            for i, count in enumerate(combination):
                for _ in range(count):
                    site_center = sites[i].get_center()
                    particle = Dot(color=BLUE).move_to(site_center + UP*0.2)
                    particles.add(particle)
                    site_centers.append(site_center + UP*0.2)
            particles.site_centers = site_centers
            return particles

        # Animate initial combinations
        for combination in initial_combinations:
            particles = create_particles(combination)
            self.add(particles)
            self.play(SmoothWiggle(particles, run_time=2, angular_frequency=WIGGLE_SPEED))
            self.remove(particles)

        # Animate all combinations
        for combination in combinations:
            particles = create_particles(combination)
            basis_vector = Tex(self.combination_to_dirac(combination), color=BLACK)
            basis_vector.to_edge(DOWN)
            self.add(particles, basis_vector)
            self.play(SmoothWiggle(particles, run_time=0.8, angular_frequency=WIGGLE_SPEED))
            self.remove(particles, basis_vector)

        self.wait()
