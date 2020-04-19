#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from IO import *
io = IO()


"""
  MODULE PRINCIPAL
  =========================
  Capture les commandes de l'utilisateur et affiche les retours
  @author: Scott RIDEL
"""

print("###### Bienvenue dans l'interface de contrôle du registre hospitalier ######\n")
print("Commandes possibles :")
print(">> create <patient | personnel> <nom> <prénom> <age> <{'symp1':5,'symp2':3} | role>")
print(">> read <all | nom>")
print(">> update <nom | prenom | age> <nom> <valeur>")
print(">> delete <nom>")
print(">> test <1 | 2>")
print(">> quit\n")
print("###### En attente de commande : ######")

while True:
  cmd = input(">> ")
  cmdLst = cmd.split(" ")
  size = len(cmdLst)

  # --- CREATE ---
  if cmdLst[0].lower() == "create" and size == 6:
    io.create(cmdLst)

  # --- READ ---
  elif cmdLst[0].lower() == "read" and size == 2:
    io.read(cmdLst[1])

  # --- UPDATE ---
  elif cmdLst[0].lower() == "update" and size == 4:
    io.update(cmdLst)

  # --- DELETE ---
  elif cmdLst[0].lower() == "delete" and size == 2:
    io.delete(cmdLst[1])

  # --- TEST ---
  elif cmdLst[0].lower() == "test" and size == 2:
    if cmdLst[1] == "1":
      io.test_1()
    elif cmdLst[1] == "2":
      io.test_2()

  # --- QUIT ---
  elif cmdLst[0].lower() == "quit":
    exit()

  else:
    print(">> Commande incorrecte !\n")
