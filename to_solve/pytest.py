import pytesseract
from PIL import Image

tesseract_config = '--psm 7 --oem 1 -c tessedit_char_whitelist=abcdefghijklkmnopqrstuvwxyz1589'

textimage = pytesseract.image_to_string(Image.open('converted_images/pinwil.png'),
config=tesseract_config)
print(textimage)
