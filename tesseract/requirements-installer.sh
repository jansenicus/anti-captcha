#!/bin/bash
sudo apt install imagemagick \
            tesseract-ocr \
            libtesseract-dev \
            libleptonica-dev \
            python-pip \
            python3-pip
pip install pytesseract
pip3 install pytesseract
whereis tesseract
wget https://raw.githubusercontent.com/tesseract-ocr/tessdata/master/eng.traineddata
sudo mv eng.traineddata /usr/share/tesseract-ocr/4.00/tessdata/eng.traineddata
