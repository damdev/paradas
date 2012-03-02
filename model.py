class Linea:
  def __init__(self, numero, ramales):
    self.numero = numero
    self.ramales = ramales

class Ramal:
  def __init__(self, letra, descripcion, recorrido):
    self.letra = letra
    self.descripcion = descripcion
    self.recorrido = recorrido

class Recorrido:
  def __init__(self, puntos):
    self.puntos = puntos
