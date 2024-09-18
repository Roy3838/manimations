from manim import *

class PartialTraceAnimation(Scene):
    def construct(self):
        # Define the density matrix ρ for two qubits |a,b⟩
        rho = MathTex(r"\rho = \begin{bmatrix} \rho_{00,00} & \rho_{00,01} & \rho_{00,10} & \rho_{00,11} \\ \rho_{01,00} & \rho_{01,01} & \rho_{01,10} & \rho_{01,11} \\ \rho_{10,00} & \rho_{10,01} & \rho_{10,10} & \rho_{10,11} \\ \rho_{11,00} & \rho_{11,01} & \rho_{11,10} & \rho_{11,11} \end{bmatrix}")
        rho.scale(0.7)
        rho.to_corner(UL)

        # Add title
        title = Text("Partial Trace of Two-Qubit Density Matrix").scale(0.7).to_edge(UP)
        self.play(Write(title), Write(rho))
        self.wait(1)

        # Explain the indices
        explanation = VGroup(
            Text("i: index of reduced matrix row").scale(0.5),
            Text("j: index of reduced matrix column").scale(0.5),
            Text("k: summed over index (traced out)").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(rho, DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Show the reduced density matrix
        reduced_rho = MathTex(r"\rho_A = \begin{bmatrix} \rho_{A,00} & \rho_{A,01} \\ \rho_{A,10} & \rho_{A,11} \end{bmatrix}")
        reduced_rho.scale(0.7).next_to(rho, RIGHT).shift(RIGHT)
        self.play(Write(reduced_rho))
        self.wait(1)

        # Demonstrate the partial trace for ρ_A,00
        highlight_color = YELLOW
        element_00 = reduced_rho.get_part_by_tex("00")
        self.play(element_00.animate.set_color(highlight_color))
        
        calc = VGroup(
            MathTex(r"\rho_{A,00} = \rho_{00,00} + \rho_{01,01}"),
            MathTex(r"= \langle 00|\rho|00\rangle + \langle 01|\rho|01\rangle")  # Using explicit bra-ket notation
        ).arrange(DOWN).next_to(reduced_rho, DOWN)
        self.play(Write(calc))
        self.wait(2)

        # Highlight corresponding elements in the original matrix
        orig_elements = VGroup(
            rho.get_part_by_tex("00,00"),
            rho.get_part_by_tex("01,01")
        )
        self.play(orig_elements.animate.set_color(RED))
        self.wait(1)

        # Clear previous calculation
        self.play(FadeOut(calc), orig_elements.animate.set_color(WHITE), element_00.animate.set_color(WHITE))

        # Demonstrate for ρ_A,01
        element_01 = reduced_rho.get_part_by_tex("01")
        self.play(element_01.animate.set_color(highlight_color))
        
        calc = VGroup(
            MathTex(r"\rho_{A,01} = \rho_{00,10} + \rho_{01,11}"),
            MathTex(r"= \langle 00|\rho|10\rangle + \langle 01|\rho|11\rangle")  # Using explicit bra-ket notation
        ).arrange(DOWN).next_to(reduced_rho, DOWN)
        self.play(Write(calc))
        self.wait(2)

        # Highlight corresponding elements in the original matrix
        orig_elements = VGroup(
            rho.get_part_by_tex("00,10"),
            rho.get_part_by_tex("01,11")
        )
        self.play(orig_elements.animate.set_color(BLUE))
        self.wait(1)

        # Final explanation
        final_text = Text("The partial trace sums over the second qubit (k), reducing the 4x4 matrix to a 2x2 matrix").scale(0.5).next_to(calc, DOWN)
        self.play(Write(final_text))
        self.wait(2)

if __name__ == "__main__":
    scene = PartialTraceAnimation()
    scene.render()
