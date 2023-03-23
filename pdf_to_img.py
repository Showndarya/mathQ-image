# sudo apt install ghostscript
# pip install pdfCropMargins

import os
from pathlib import Path
from pdfCropMargins import crop

INPUT_DIRECTORY = Path("./output_pdf")
OUTPUT_DIRECTORY = Path("./output_pdf_cropped")

if str(OUTPUT_DIRECTORY) not in os.listdir("."):
    os.mkdir(OUTPUT_DIRECTORY)

for filename in os.listdir(INPUT_DIRECTORY):
    if filename.endswith('.pdf'):
        try:
            cropped = crop(["-p", "10", "-u", "-s", "-o", str(OUTPUT_DIRECTORY), str(INPUT_DIRECTORY / filename)])
            if cropped[0] is not None: # succeeded
                print(filename + " cropped successfully")
            else:
                print(filename + " failed to crop, skipping")
        except:
            print(filename + " failed to crop with error")