#!/bin/bash
# captcha_downloader
N_CAPTCHAS=2
for i in `seq 1 $N_CAPTCHAS`;
do
 curl -s -k -X 'GET' https://devicelocator.bri.co.id/get_captcha.php -o file$i.png
 echo $i
done
