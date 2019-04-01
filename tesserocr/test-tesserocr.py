# https://oded.blog/2017/01/08/ocr-made-easy-using-tesserocr/

from tesserocr import PyTessBaseAPI
import sys
import os

# tesserocr -> https://pypi.python.org/pypi/tesserocr
# cython -> https://pypi.python.org/pypi/Cython
# Pillow -> https://pypi.python.org/pypi/Pillow

if len(sys.argv) != 2:
    print("you need to pass the path to the image as first argument")
    sys.exit(1)

path = sys.argv[1]
if not os.path.exists(path):
    print("image doesn't exist at: " + path)
    sys.exit(2)

with PyTessBaseAPI() as api:
    api.SetImageFile(os.path.abspath(path))
    lines = [ l.strip() for l in api.GetUTF8Text().split('\\') if l.strip() != ""]

for l in lines:
    print(l)
