# Simple installation:
# sudo apt-get install texlive-latex-base
#
# If you want everything:
# sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra

import subprocess
from sys import platform

if platform == "win32":
    subprocess.check_call(['wsl', 'pdflatex', 'output_tex/2303.11999v1_0.tex'])
else:
    subprocess.check_call(['pdflatex'])