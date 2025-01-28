from manim import *

class TestScene(Scene):
    def construct(self):
        # Get the default template and modify it
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsmath}")
        template.add_to_preamble(r"\usepackage{amssymb}")
        template.add_to_preamble(r"\usepackage{braket}")
        
        # Print the actual template content that will be used
        print("\nTemplate preamble:", template.tex_compiler)
        print("\nTemplate body:", template.body)
        
        # Create temporary directory to see where Manim is trying to write
        import tempfile
        import os
        temp_dir = tempfile.gettempdir()
        print(f"\nTemporary directory being used: {temp_dir}")
        print(f"Temp directory permissions: {oct(os.stat(temp_dir).st_mode)[-3:]}")
        
        # Try the simplest possible math expression first
        text = MathTex(
            r"1+1",
            tex_template=template
        )
        self.add(text)
        self.wait()

from manim import *

config.tex_template = TexTemplate()
config.tex_template.add_to_preamble(r"\usepackage{amsmath}")
config.tex_template.add_to_preamble(r"\usepackage{amssymb}")
config.tex_template.add_to_preamble(r"\usepackage{braket}")
config.background_color = WHITE
config.tex_compiler = "latex"  # Try expli:with  as target:
