#!/usr/bin/env sh
cat cache/*.html | grep "myarr[0-9]*[[:space:]]=[[:space:]][[:alnum:]]*('[[:alnum:]]*')\;" -o | sed "s/polyline[0-9]*.*//g" | sed "s/myarr/{ \"id\": \"/g" | sed "s/ = str2garr('/\", \"coords\": \"/g" | sed "s/');/\" },/g" | sed "s/\t//g" | cat head.txt - tail.txt | sed -n -e ":a" -e "$ s/\n//gp;N;b a" | sed "s/,]}/]}/g"
