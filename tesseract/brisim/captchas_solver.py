#!/bin/python3
import glob, os
import pytesseract
import subprocess
from PIL import Image
from difflib import get_close_matches



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
    subprocess.call(['convert', captcha_image_file, '-fuzz', '22%', '-fill', '#0000ff', '-opaque', '#1a67d9', save_path])
    subprocess.call(['convert', save_path, '-fuzz', '55%', '-fill', '#ffffff', '+opaque', '#0000ff', save_path])
    #subprocess.call(['convert', save_path, '-colorspace', 'gray', '-threshold','10%', save_path])
    #subprocess.call(['convert', save_path, '-resize','200%', save_path])

    # tesseract call
    tesseract_config = '--psm 8 --oem 0 -c tessedit_char_whitelist=ABCDEFGIKLMNOPRSTWabcdefghiklkmnopqrstuvwxyz012345679 --user-words wordlist'
    text_detected = pytesseract.image_to_string(Image.open(save_path),
    config=tesseract_config)

    # REPLACE ALL SPACES
    text_detected = text_detected.replace(" ","")

    # TEXT SUGGESTION FROM WORDLIST
    # this method improves accuracy
    
    with open('wordlist') as f:
        content = f.readlines()
    wordlist = [x.strip() for x in content]
    f.close()

    text_suggested = get_close_matches(text_detected, wordlist, n=1, cutoff=0.1)
    if text_suggested:
        text_detected = text_suggested[0]
    try:
        assert filename.split('.')[0].split('-')[0] == text_detected
        cntCorrect += 1
    except:
        cntWrong += 1
        #msgWrong += (filename + '!=' + text_detected) + "\n"
    #print(filename.split('.')[0].split('-')[0], '==', text_detected)
    print(text_detected)

print("")
print("Correct:", str(cntCorrect))
print("Wrong:"+str(cntWrong))
#print(msgWrong)
