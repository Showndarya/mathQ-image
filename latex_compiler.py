# Simple installation:
# sudo apt-get install texlive-latex-base
#
# If you want everything:
# sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra

import os
from pathlib import Path
import subprocess
from sys import platform

OUTPUT_DIRECTORY = Path("./output_pdf")

if str(OUTPUT_DIRECTORY) not in os.listdir("."):
    os.mkdir(OUTPUT_DIRECTORY)

command = ['pdflatex', '-output-directory', str(OUTPUT_DIRECTORY), 'output_tex/2303.11999v1_2.tex']

if platform == "win32":
    command.insert(0, 'wsl')

subprocess.check_call(command)