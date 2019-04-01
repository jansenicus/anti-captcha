#!/bin/python3
import glob, os
import pytesseract
import subprocess
from PIL import Image


CAPTCHA_IMAGE_FOLDER = "captcha_images"
OUTPUT_FOLDER = "converted_images"

# Get a list of all the captcha images we need to process
captcha_image_files = glob.glob(os.path.join(CAPTCHA_IMAGE_FOLDER, "*"))
counts = {}

# loop over the image paths
for (i, captcha_image_file) in enumerate(captcha_image_files):
    #print("[INFO] converting image {}/{}".format(i + 1, len(captcha_image_files)))
    filename = os.path.basename(captcha_image_file)
    save_path = os.path.join(OUTPUT_FOLDER, filename)
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))

    subprocess.call(['convert', captcha_image_file, '-colorspace', 'gray', save_path])
    subprocess.call(['convert', save_path, '-colorspace', 'gray', '-threshold','50%', save_path])
    subprocess.call(['convert', save_path, '-resize','200%', save_path])


    tesseract_config = '--psm 8 --oem 0 -c tessedit_char_whitelist=abcdefghijklkmnopqrstuvwxyz1589 --user-words wordlist'
    text_detected = pytesseract.image_to_string(Image.open(save_path),
    config=tesseract_config)
    try:
        assert filename.split('.')[0] == text_detected
        #print(filename, '==', text_detected)
    except:
        print(filename, '!=', text_detected)
