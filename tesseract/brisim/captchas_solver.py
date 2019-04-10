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
msgWrong = ''; msgCorrect = '';
cntWrong = 0; cntCorrect = 0;

# loop over the image paths
for (i, captcha_image_file) in enumerate(captcha_image_files):
    #print("[INFO] converting image {}/{}".format(i + 1, len(captcha_image_files)))
    filename = os.path.basename(captcha_image_file)
    save_path = os.path.join(OUTPUT_FOLDER, filename)
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))

    # imagemagick convert command
    subprocess.call(['convert', captcha_image_file, '-fuzz', '15%', '-fill', '#0000ff', '-opaque', '#1a67d9', save_path])
    subprocess.call(['convert', save_path, '-fuzz', '55%', '-fill', '#ffffff', '+opaque', '#0000ff', save_path])
    #subprocess.call(['convert', save_path, '-colorspace', 'gray', '-threshold','60%', save_path])
    #subprocess.call(['convert', save_path, '-resize','200%', save_path])

    # tesseract call
    tesseract_config = '--psm 8 --oem 0 -c tessedit_char_whitelist=ABCDEFIKLMNOPRSTKabcdefghiklkmnopqrstuvwxyz012345679 --user-words wordlist'
    text_detected = pytesseract.image_to_string(Image.open(save_path),
    config=tesseract_config)

    try:
        assert filename.split('.')[0].split('-')[0] == text_detected
        cntCorrect += 1
        print(filename, '==', text_detected)

    except:
        cntWrong += 1
        msgWrong += (filename + '!=' + text_detected) + "\n"

print("")
print("Correct:", str(cntCorrect))
print("Wrong:"+str(cntWrong))
#print(msgWrong)
