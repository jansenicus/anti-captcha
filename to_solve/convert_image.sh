#!/bin/sh
convert captcha_images/sivabri.png -colorspace gray converted_images/sivabri-1.png
convert converted_images/sivabri-1.png -colorspace gray -threshold 50% converted_images/sivabri-2.png
tesseract converted_images/sivabri-1.png -
