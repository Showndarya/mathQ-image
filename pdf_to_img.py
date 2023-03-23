# INSTALLATION:
# sudo apt install ghostscript
# pip install pdfCropMargins

# TODO: write instructions for poppler install
# pip install pdf2image

import os
from pathlib import Path
from pdfCropMargins import crop
from pdf2image import convert_from_path

INPUT_DIRECTORY = Path("./output_pdf")
OUTPUT_DIRECTORY_CROPPED = Path("./output_pdf_cropped")

# TODO: remove local reference
POPPLER_PATH = Path("C:\\Users\\ivanb\\Desktop\\poppler-0.68.0\\bin")
OUTPUT_DIRECTORY_PNG = Path("./output_png")

if str(OUTPUT_DIRECTORY_CROPPED) not in os.listdir("."):
    os.mkdir(OUTPUT_DIRECTORY_CROPPED)

if str(OUTPUT_DIRECTORY_PNG) not in os.listdir("."):
    os.mkdir(OUTPUT_DIRECTORY_PNG)

for filename in os.listdir(INPUT_DIRECTORY):
    if filename.endswith('.pdf'):
        try:
            cropped = crop(["-p", "10", "-u", "-s", "-o", str(OUTPUT_DIRECTORY_CROPPED), str(INPUT_DIRECTORY / filename)])
            if cropped[0] is not None: # succeeded
                print(filename + " cropped successfully")
            else:
                print(filename + " failed to crop, skipping")
        except:
            print(filename + " failed to crop with error")

# done with cropping, now convert to png

for filename in os.listdir(OUTPUT_DIRECTORY_CROPPED):
    output_filename = filename.replace('_cropped.pdf', '')
    convertedpdf = convert_from_path(str(OUTPUT_DIRECTORY_CROPPED / filename), \
                                            grayscale=False, \
                                            poppler_path=str(POPPLER_PATH), \
                                            output_folder=str(OUTPUT_DIRECTORY_PNG), \
                                            output_file=output_filename,
                                            fmt='jpg')