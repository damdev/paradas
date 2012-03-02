#!/bin/bash
for i in $(seq 1 195);
do
   curl "http://movil.omnilineas.com.ar/colectivo/linea-$i/" > cache/$i.html;
done
