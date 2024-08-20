from manim import *
from manim_ml.neural_network import FeedForwardLayer, NeuralNetwork


class LLMPrediction(ThreeDScene):
    def construct(self):
        
        self.camera.background_color ="#E2E2E2" 

        # Create the input text
        input_text = Text("Rate the quality of this YouTube Title:", font_size=24).set_color(BLACK)
        youtube_title = Text("{the BEST youtube title}", font_size=20, color=GREY_D)
        input_group = VGroup(input_text, youtube_title).arrange(DOWN, buff=0.3)
        input_group.to_edge(UP)

        # Create the neural network
        nn = NeuralNetwork([
                FeedForwardLayer(5),
                FeedForwardLayer(8),
                FeedForwardLayer(8),
                FeedForwardLayer(8),
                FeedForwardLayer(5),
            ],
            layer_spacing=0.5,
        )
        nn.scale(0.8)
        nn.move_to(ORIGIN)
        nn[0].set_color(BLACK)

        # Create the 3D embedding vector
        embedding = ThreeDAxes(
            x_range=[-1, 1, 0.5],
            y_range=[-1, 1, 0.5],
            z_range=[-1, 1, 0.5],
            x_length=2,
            y_length=2,
            z_length=2
        ).set_color(BLACK)
        embedding_vector = Arrow3D(start=ORIGIN, end=np.array([0.5, 0.7, -0.3]), color=GREEN)
        embedding_group = VGroup(embedding, embedding_vector)
        embedding_group.scale(0.5)
        embedding_group.next_to(nn, LEFT, buff=1)
        embedding_text = Text("Embedding Vector", font_size=20).next_to(embedding_group, UP, buff=0.2).set_color(BLACK)

        # Create the output vector
        output_values = [0.3, 0.2, 0.1, 0.15, 0.25]
        output_labels = ["Excellent", "Great", "Good", "Fair", "Poor"]
        bar_chart = BarChart(
            values=output_values,
            bar_names=output_labels,
            y_range=[0, 1, 0.2],
            y_length=2,
            x_length=3,
            bar_width=0.5,
        ).scale(0.5)
        bar_chart.next_to(nn, RIGHT, buff=1)
        output_text = Text("Output Probabilities", font_size=20).next_to(bar_chart, UP, buff=0.2).set_color(BLACK)

        # Animations
        self.play(Write(input_group))
        self.play(FadeIn(nn),run_time=1)
        self.move_camera(phi=35 * DEGREES, theta=-15 * DEGREES)
        self.play(Create(embedding_group), Write(embedding_text))
        self.play(Create(bar_chart), Write(output_text))

        # Animate embedding going into LLM
        moving_embedding = embedding_vector.copy()
        self.play(moving_embedding.animate.move_to(nn[0].get_left()))
        self.play(FadeOut(moving_embedding))

        # Add title
        title = Title("LLM Prediction Process")
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        self.wait(2)

if __name__ == "__main__":
    scene = LLMPrediction()
    scene.render()
