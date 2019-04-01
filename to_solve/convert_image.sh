#!/bin/bash
convert captcha_images/sivabri.png -colorspace gray converted_images/sivabri-1.png
convert converted_images/sivabri-1.png -colorspace gray -threshold 50% converted_images/sivabri-2.png
tesseract converted_images/sivabri.png stdout --oem 0 --psm 8 -c tessedit_char_whitelist=1589abcdefghijklkmnopqrstuvwxyz
