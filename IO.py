#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Patient import *
from Personnel import *
from Registre import *


class IO:
  """
    CLASS IO
    Définit les 4 méthodes : create, read, update et delete
    @author: Scott RIDEL
  """

  # === CONSTRUCTEUR ===
  def __init__(self):
    self.patients = Registre("patients.json")
    self.personnel = Registre("personnel.json")

  # --- CREATE ---
  def create(self, cmdLst):
    if cmdLst[1].lower() in ("patient", "personnel"):
      if type(cmdLst[2]) == str and type(cmdLst[3]) == str:
        if self.ifInt(cmdLst[4]):
          if cmdLst[1].lower() == "patient":
            try:
              sympLst = eval(cmdLst[5])
            except:
              print(">> La liste des symptomes doit être de type dictionnaire sans espaces !")
              print(">> exemple : {'toux':1,'fievre':5}\n")
            else:
              if type(sympLst) == dict:
                ok = True
                for sever in sympLst.values():
                  if not self.ifInt(sever) or not 1 <= sever <= 5:
                    ok = False
                if ok:
                  if len(sympLst) > 0:
                    self.patients.add(Patient(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), cmdLst[5]))
                    self.patients.saveJson()
                  else:
                    print(">> Le patient doit au moins présenter un symptomes pour être admis !\n")
                else:
                  print(">> La structure de la liste des symptomes est incorrecte (la sévérité doit entre 1 et 5)\n")
          elif cmdLst[1].lower() == "personnel" and type(cmdLst[5]) == str:
            self.personnel.add(Personnel(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), cmdLst[5].lower()))
            self.personnel.saveJson()
          else:
            print(">> Le role doit être de type text !\n")
        else:
          print(">> L'age doit être une valeur numérique !\n")
      else:
        print(">> Le nom et prénom doivent être de type text !\n")
    else:
      print(">> Le deuxième paramètre doit être : patient ou personnel !\n")

  # --- READ ---
  def read(self, _param):
    """Affiche soit : (la liste des patients ordonnés et du personnel) ou (les informations d'un occupant)."""
    if type(_param) == str:
      x = _param.lower()
      if not self.patients.sort(x):
        print(">> Le registre des patients est vide !\n")
      if not self.personnel.sort(x):
        print(">> Le registre du personnel est vide !\n")
    else:
      print(">> Le deuxième paramètre est incorrect !\n")

  # --- UPDATE ---
  def update(self, cmdLst):
    """Permet de metre à jour les informations d'un occupant."""
    if type(cmdLst[2]) == str:
      var = cmdLst[3]
      if cmdLst[1].lower() in ('nom', 'prenom', 'age'):
        if cmdLst[1].lower() == 'age':
          if self.ifInt(var):
            var = int(var)
          else:
            print(">> L'age doit être une valeur numérique !\n")
            return False
        else:
          if type(var) == str:
            if not self.patients.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> Aucun {} dans le registre patient !\n".format(cmdLst[2].upper()))
            if not self.personnel.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> Aucun {} dans le registre personnel !\n".format(cmdLst[2].upper()))

          else:
            print(">> L'age doit être une valeur numérique !\n")
      else:
        print(">> Le dexième paramètre doit être : nom, prenom ou age !\n")
    else:
      print(">> Le nom est incorrect !\n")

  # --- DELETE ---
  def delete(self, _param):
    """Permet de supprimer un occupant."""
    if type(_param) == str:
      if not self.patients.remove(_param.lower()) and not self.personnel.remove(_param.lower()):
        print(">> L'occupant {} est introuvable !\n".format(_param.upper()))
    else:
      print(">> Le nom est incorrect !\n")

  # --- TEST 1 ---
  def test_1(self):
    """Méthode de test 1"""
    self.create(["create", "patient", "smith", "john", 25, "{'toux':2,'fievre':4}"])
    self.create(["create", "personnel", "moser", "mau-britt", 54, "neuroscientist"])
    self.patients.dropLst()
    self.personnel.dropLst()
    print(">> Listes patient et personnel effacées.")
    self.patients.loadJson()
    self.personnel.loadJson()
    print(">> Listes patient et personnel chargées à partir des fichiers json.")
    self.read("all")

  # --- TEST 2 ---
  def test_2(self):
    """Méthode de test 2"""
    self.patients.loadJson()
    self.personnel.loadJson()
    print(">> Listes patient et personnel chargées à partir des fichiers json.")
    self.read("all")
    self.patients.update("nom", "smith", "travis")
    self.delete("moser")
    self.read("all")

  # --- IF INT ---
  def ifInt(self, arg):
    """Retourne True si convertible en Int, sinon False."""
    try:
      var = int(arg)
    except:
      return False
    else:
      return True
