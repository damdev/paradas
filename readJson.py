import simplejson as json
from model import Linea, Ramal, Recorrido

def readFiles():
  puntosFile = open("puntos.json", 'r').read().decode('ISO-8859-1')
  lineasFile = open("lineas.json", 'r').read().decode('ISO-8859-1')
  puntos = json.loads(puntosFile)
  lineas = json.loads(lineasFile)
  return (puntos, lineas)

def parsePuntos(puntosJson):
  puntos = {}
  puntosList = puntosJson['data']
  for punto in puntosList:
    id = punto['id']
    coords = punto['coords']
    puntos[id] = decodeCoords(coords)
  return puntos

def parseLineas(lineasJson):
  lineas = {}
  jlineas = lineasJson['data']
  for linea in jlineas:
    lineas[linea['linea']] = parseRamales(linea['ramales'])
  return lineas

def parseRamales(jramales):
  ramales = {}
  for ramal in jramales:
    ramales[ramal['nombre']] = ramal['id']
  return ramales

def splitLen(seq, length):
  return [seq[i:i+length] for i in range(0, len(seq), length)]

def decodeCoords(coords):
  return [decodeCoord(coord) for coord in splitLen(coords, 18)]

def decodeCoord(pdat):
  if len(pdat) != 18:
    return false
  datlat = pdat[0:9]
  datlng = pdat[9:18]
  slat = datlat[0:1]
  slng = datlng[0:1]
  ablat = datlat[1:3]
  ablng = datlng[1:3]
  cdelat = datlat[3:6]
  cdelng = datlng[3:6]
  fghlat = datlat[6:9]
  fghlng = datlng[6:9]
  rslat = 1
  if slat == "k":
    rslat = -1
  rslng = 1
  if slng == "k":
    rslng = -1
  rablat = int(ablat, 16)
  rablng = int(ablng, 16)
  rcdelat = int(cdelat, 16)
  rcdelng = int(cdelng, 16)
  rfghlat = int(fghlat, 16)
  rfghlng = int(fghlng, 16)
  reslat = rslat * (rablat + rcdelat/1000.0 + rfghlat/1000000.0)
  reslng = rslng * (rablng + rcdelng/1000.0 + rfghlng/1000000.0)
  resu = (reslat, reslng)
  return resu

def getLineas():
  (jpuntos, jlineas) = readFiles()
  puntos = parsePuntos(jpuntos)
  lineas = parseLineas(jlineas)
  lList = []
  for linea in lineas.keys():
    rList = []
    for ramal in lineas[linea].keys():
      ramalId = lineas[linea][ramal]
      r = Ramal(ramal[0], ramal[4:], Recorrido(puntos[ramalId]))
      rList.append(r)
    l = Linea(int(linea[6:]), rList)
    lList.append(l)
  return lList
