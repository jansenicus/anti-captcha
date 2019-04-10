curl -q -s -k -X 'GET' https://devicelocator.bri.co.id/get_captcha.php -o /tmp/file.png
python solve-captcha.py /tmp/file.png
