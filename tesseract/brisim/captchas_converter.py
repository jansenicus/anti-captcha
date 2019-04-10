#!/bin/python3
import subprocess
import glob, os


CAPTCHA_IMAGE_FOLDER = "captcha_images"
OUTPUT_FOLDER = "converted_images"

# Get a list of all the captcha images we need to process
captcha_image_files = glob.glob(os.path.join(CAPTCHA_IMAGE_FOLDER, "*"))
counts = {}

# loop over the image paths
for (i, captcha_image_file) in enumerate(captcha_image_files):
    print("[INFO] converting image {}/{}".format(i + 1, len(captcha_image_files)))
    #print(captcha_image_file)
    filename = os.path.basename(captcha_image_file)

    # Get the folder to save the image in
    save_path = os.path.join(OUTPUT_FOLDER, filename)
    # if the output directory does not exist, create it
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    # write the letter image to a file

    # change text color
    subprocess.call(['convert', captcha_image_file, '-fuzz', '15%', '-fill', '#0000ff', '-opaque', '#1a67d9', save_path])
    subprocess.call(['convert', save_path, '-fuzz', '50%', '-fill', '#ffffff', '+opaque', '#0000ff', save_path])
    #subprocess.call(['convert', save_path, '-colorspace', 'gray', '-threshold','65%', save_path])
    #subprocess.call(['convert', save_path, '-resize','200%', save_path])

    # clear noise
    # subprocess.call(['convert', save_path, '-threshold', '70%', '-define', 'connected-components:verbose=true', '-define', 'connected-components:area-threshold=5', '-define', 'connected-components:mean-color=true', '-connected-components', '15', save_path])
