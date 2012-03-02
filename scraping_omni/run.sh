mkdir cache
sh scrap_omni.sh
sh extract_puntos.sh > ../puntos.json
sh extract_lineas.sh > ../lineas.json
rm -rf cache
