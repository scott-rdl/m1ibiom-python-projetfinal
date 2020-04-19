#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
import json


class Registre:
  """
    CLASSE REGISTRE
    Permet de gérer le registre des patients et du personnel.
    @author: Scott RIDEL
  """

  # === CONSTRUCTEUR ===
  def __init__(self, _chemin):
    self.chemin = _chemin
    self.liste = []

  # --- AAD ---
  def add(self, _occupant):
    """Ajoute un occupant au registre."""
    self.liste.append(_occupant.__dict__)

  # --- UPDATE ---
  def update(self, _param, _nom, _value):
    """Modifier le nom, le prénom ou l'age d'un occupant."""
    find = False
    tmpLst = []
    if len(self.liste) > 0:
      for x in self.liste:
        if x['nom'] == _nom:
          print('>> Ancienne données :')
          print(self.printOccup(x))
          x[_param] = _value
          print('>> Mise à jour :')
          print(self.printOccup(x))
          find = True
        tmpLst.append(x)
      self.liste = tmpLst
      self.saveJson()
      print()
      if find:
        return True
      else:
        return False

  # --- REMOVE ---
  def remove(self, _param):
    """Supprime un occupant du registre."""
    tmpLst = []
    find = False
    for x in self.liste:
      if x['nom'] == _param:
        print('>> {} {} {} à été supprimé du registre !'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age']))
        find = True
      else:
        tmpLst.append(x)
    self.liste = tmpLst
    self.saveJson()
    if not find:
      return False
    else:
      return True

  # --- SORT ---
  def sort(self, _param):
    """
      Retourne pour 'all'
        soit la liste patients classés par urgence médicale
        soit la liste du personnel (en fonction du type de dictionnaire)
      sinon pour '<nom>'
        le patient ou le membre du personnel correspondant au nom
    """
    find = False
    if len(self.liste) > 0:
      if _param == 'all':
        if self.liste[0]['type'] == 'patient':
          print(">> Patients ordonnées par urgence médicale :")
          newLst = {}
          for x in self.liste:
            newLst[self.printOccup(x)] = x['etat']
          for key in sorted(newLst, key=newLst.get, reverse=True):
            print(key)
        else:
          print(">> Liste du personnel médical :")
          for x in self.liste:
            print(self.printOccup(x))
        print()
      else:
        for x in self.liste:
          if x['nom'] == _param:
            print(self.printOccup(x), "\n")
            find = True
          if not find:
            print(">> Aucun {} correspondant à {} !\n".format(self.liste[0]['type'], _param.upper()))
      return True
    else:
      return False

  # --- PRINT OCCUP ---
  def printOccup(self, _occupant):
    """Retourne la String d'affichage d'un occupant correspondant à son type"""
    x = _occupant
    if self.liste[0]['type'] == 'patient':
      return '   - {} {} {} ans (sévérité: {})'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age'], x['etat'])
    else:
      return '   - {} {} {} ans, {}'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age'], x['role'])

  # --- DROP LST ---
  def dropLst(self):
    """Vide la liste du registre"""
    self.liste = []

  # --- SAVE JSON ---
  def saveJson(self):
    """Sauvegarde la liste dans le fichier au format Json"""
    with open(self.chemin, 'w') as outf:
      json.dump(self.liste, outf, ensure_ascii=False, indent=2)

  # --- LOAD JSON ---
  def loadJson(self):
    """Charge les données du fichier au format Json"""
    with open(self.chemin, 'r') as inf:
      self.liste = json.load(inf)
