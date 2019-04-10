#!/bin/bash
sudo apt install subprocess \
            imagemagick \
            tesseract-ocr \
            libtesseract-dev \
            libleptonica-dev
whereis tesseract
wget https://raw.githubusercontent.com/tesseract-ocr/tessdata/master/eng.traineddata
sudo mv eng.traineddata /usr/share/tesseract-ocr/4.00/tessdata/eng.traineddata
