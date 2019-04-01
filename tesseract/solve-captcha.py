#!/bin/python3
# solve-captcha.py
# USAGE:
# python solve-captcha.py captcha_image_file
# python solve-captcha.py casa.png
# python solve-captcha.py briva.png


import pytesseract, subprocess
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('captcha_image_file', \
type=str, nargs='?',  \
help="Specify captcha image file path")
args=parser.parse_args()
#print(args.captcha_image_file)
save_path = '/tmp/'+ args.captcha_image_file.split('/')[-1]

# convert
subprocess.call(['convert', args.captcha_image_file, '-colorspace', 'gray', '-threshold','50%', save_path])
subprocess.call(['convert', save_path, '-resize','200%', save_path])

# tesseract
tesseract_config = '--psm 8 --oem 0 -c tessedit_char_whitelist=abcdefghijklkmnopqrstuvwxyz0145789 --user-words wordlist'
text_detected = pytesseract.image_to_string(Image.open(save_path),
config=tesseract_config)

print(text_detected)
