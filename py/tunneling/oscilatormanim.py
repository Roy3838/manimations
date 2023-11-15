from manim import Scene, ImageMobject
import numpy as np

class HarmonicOscillator(Scene):
    def construct(self):
        img = ImageMobject(np.zeros((200, 200))).scale(5)

        # Load W matrices from the binary file
        W_matrices = np.load('tunneling/W_matrices.npy')
        n_timesteps = W_matrices.shape[0]

        img.funcs = [W_matrices[i] / W_matrices[i].max() * 255 for i in range(n_timesteps)]

        def function_updater(image, dt):
            density = image.funcs[int(dt*60) % len(image.funcs)]
            image.become(ImageMobject(density))

        img.add_updater(function_updater)
        self.add(img)
        self.wait(1)
