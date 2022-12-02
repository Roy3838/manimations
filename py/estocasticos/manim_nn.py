from manim import *
from pathlib import Path
from manim_ml.neural_network.layers import Convolutional3DLayer
from manim_ml.neural_network.layers.feed_forward import FeedForwardLayer
from manim_ml.neural_network.layers.image import ImageLayer
from manim_ml.neural_network.neural_network import NeuralNetwork

ROOT_DIR = Path(__file__).parents[2]

class VariationalAutoencoderScene(Scene):

    def construct(self):
        
        neural_network = NeuralNetwork([
            FeedForwardLayer(1),
            FeedForwardLayer(4),
            FeedForwardLayer(4),
            FeedForwardLayer(1),
        ], layer_spacing=0.5)

        neural_network.scale(4)

        self.play(Create(neural_network))
        self.play(neural_network.make_forward_pass_animation(run_time=1))
        self.play(neural_network.make_forward_pass_animation(run_time=1))
        self.play(neural_network.make_forward_pass_animation(run_time=1))



