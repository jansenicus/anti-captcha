#!/bin/sh
for i in `seq 1 20`;
do
 curl -s -k -X 'GET' https://devicelocator.bri.co.id/get_captcha.php -o file$i.png
 echo $i
done
