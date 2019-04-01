import pytesseract
from PIL import Image

tesseract_config = '--psm 8 --oem 0 -c tessedit_char_whitelist=abcdefghijklkmnopqrstuvwxyz0145789 --user-words wordlist'
text_detected = pytesseract.image_to_string(Image.open('converted_images/brilink.png'),
config=tesseract_config)

print(text_detected)
