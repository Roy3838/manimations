import os
import subprocess

from hashlib import md5
from tempfile import TemporaryDirectory


TEX_TEMPLATE = r'''
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{amssymb,amsmath}
\usepackage{color}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{pst-plot}
\usepackage{braket}
\begin{document}
\pagestyle{empty}
\Large
\begin{displaymath}
$$
\end{displaymath}
\end{document}
'''

class ConvertError(RuntimeError):
    pass

class Tex2Img:
    def __init__(self, formula, fmt='png', dpi=300):
        self.formula = formula.strip()
        self.format = fmt
        self.dpi = dpi
        self.hash = md5(formula.encode()).hexdigest()

    def generate(self):
        with TemporaryDirectory() as tdir:
            tex_path = os.path.join(tdir, "{}.tex".format(self.hash))
            dvi_path = os.path.join(tdir, "{}.dvi".format(self.hash))
            png_path = os.path.join(tdir, "{}.png".format(self.hash))
            svg_path = os.path.join(tdir, "{}.svg".format(self.hash))
            with open(tex_path, "w") as tex_file:
                tex_file.write(TEX_TEMPLATE.replace('$$', self.formula))
            self.run_latex(tdir, tex_path, dvi_path)
            if self.format == 'png':
                self.run_dvipng(dvi_path, png_path)
            elif self.format == 'svg':
                self.run_dvisvgm(dvi_path, svg_path)
            result_path = png_path if self.format == 'png' else svg_path
            with open(result_path, 'rb') as rf:
                return rf.read()

    def run_latex(self, directory, tex_path, dvi_path):
        subp = subprocess.Popen(['latex',
            '-output-format=dvi',
            '-output-directory={}'.format(directory),
            tex_path], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subp.wait()
        if subp.returncode != 0 or not os.path.exists(dvi_path):
            raise ConvertError("cannot compile tex file to dvi")

    def run_dvipng(self, dvi_path, png_path):
        status = subprocess.run(['dvipng',
            '-D', str(self.dpi),  # Set the resolution
            '-q', '-T', 'tight',
            '-bg', 'Transparent',
            '-o', png_path, dvi_path]).returncode
        if status != 0 or not os.path.exists(png_path):
            raise ConvertError("cannot convert dvi to png")
    
    def run_dvisvgm(self, dvi_path, svg_path):
        status = subprocess.run(['dvisvgm', \
            '-output-format=dvi', \
            '-v', '0', \
            '--no-fonts', \
            '-o', svg_path, dvi_path]).returncode
        if status != 0 or not os.path.exists(svg_path):
            raise ConvertError("cannot convert dvi to svg")

def generate_svg(formula):
    return Tex2Img(formula, 'svg').generate()


def generate_png(formula):
    return Tex2Img(formula, 'png').generate()


formula = r'\Phi = sinc[\frac{L}{2}\Delta k]\exp{[\frac{iL}{2}\Delta k]}'

# Generate the PNG image
image_data = generate_png(formula)

# Specify the path where you want to save the image
image_path = '/Users/jay/manimations/image2.png'

# Write the image data to the file
with open(image_path, 'wb') as file:
    file.write(image_data)
