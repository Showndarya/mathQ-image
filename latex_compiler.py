# Simple installation:
# sudo apt-get install texlive-latex-base
#
# If you want everything:
# sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra

import os
from pathlib import Path
import subprocess
from sys import platform

# INPUT_DIRECTORY = Path("./output_tex")
# OUTPUT_DIRECTORY = Path("./output_pdf")

INPUT_DIRECTORY = Path("./output_tex_temp")
OUTPUT_DIRECTORY = Path("./output_pdf_temp")

if str(OUTPUT_DIRECTORY) not in os.listdir("."):
    os.mkdir(OUTPUT_DIRECTORY)

# command = ['wsl', 'pdflatex', '-output-directory', str(OUTPUT_DIRECTORY), 'output_tex/2303.11999v1_0.tex']
# subprocess.check_call(command)

command = ['pdflatex', '-interaction=batchmode', '-output-directory', str(OUTPUT_DIRECTORY)]
if platform == "win32":
    command.insert(0, 'wsl')

# TODO: add timeout as batchmode encounters infinite loops while compiling
for filename in os.listdir(INPUT_DIRECTORY):
    try:
        subprocess.check_call(command + [str(INPUT_DIRECTORY) + "/" + filename])
    except:
        print(filename + " failed to compile, skipping")