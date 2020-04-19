#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Occupant import *


class Personnel(Occupant):
  """
    CLASSE PERSONNEL
    Hérite d'Occupant
    @author: Scott RIDEL
  """

  # === CONSTRUCTEUR ===
  def __init__(self, _nom, _prenom, _age, _role):
    super().__init__(_nom, _prenom, _age)
    self.role = _role
    self.type = 'personnel'
    print(self)

  def __repr__(self):
    return '{self.__class__.__name__}({self.nom}, {self.prenom}, {self.age}, {self.role})'.format(self=self)

  def __str__(self):
    return '>> Le {} {} {} {} ans, à été ajouté !'.format(self.role, self.nom.upper(), self.prenom.capitalize(), self.age)
