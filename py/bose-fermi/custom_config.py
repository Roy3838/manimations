from manim import *

config.tex_template = TexTemplate()
config.tex_template.add_to_preamble(r"\usepackage{amsmath}")
config.tex_template.add_to_preamble(r"\usepackage{amssymb}")
config.tex_template.add_to_preamble(r"\usepackage{braket}")
config.background_color = WHITE
config.tex_compiler = "latex"  # Try explicitly setting the compiler
