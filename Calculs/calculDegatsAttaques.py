# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 23:50:33 2021

@author: angel
"""
from random import randint

"""
puissance = puissance de l'attaque OK
degats = degats du pokemon OK
random = [randint(217,255) * 100] / 255 OK
type1 = 2 si le type contre, 0,5 si peu efficace, 0 si inneficace, sinon 1 ; typeAttaque contre type1PokemonDefence OK
type2 = 2 si le type contre, 0,5 si peu efficace, 0 si inneficace, sinon 1 ; typeAttaque contre type2PokemonDefence OK
coupCrit = 2 si crit sinon 1, calculé a partir de T/256
                                                  T = vitesse (arrondi a l'entier pair supérieur) / 2
stab = si type1 ou type2 = type attaque = 1,50;
       sinon = 1
"""

def valRandom():
    return (randint(217, 255) * 100) / 255

def valType(typeAttaque, type1Pokemon):
    if typeAttaque == "Normal":
        if type1Pokemon == "Roche":
            return 1/2
        elif type1Pokemon == "Spectre":
            return 0
        else:
            return 1
        
    elif typeAttaque == "Feu":
        if type1Pokemon == "Feu" or type1Pokemon == "Eau" or type1Pokemon == "Roche" or type1Pokemon == "Dragon":
            return 1/2
        elif type1Pokemon == "Plante" or type1Pokemon == "Glace" or type1Pokemon == "Insecte":
            return 2
        else:
            return 1
        
    elif typeAttaque == "Eau":
        if type1Pokemon == "Eau" or type1Pokemon == "Plante" or type1Pokemon == "Dragon":
            return 1/2
        elif type1Pokemon == "Feu" or type1Pokemon == "Sol" or type1Pokemon == "Roche":
            return 2
        else:
            return 1
        
    elif typeAttaque == "Plante":
        if type1Pokemon == "Feu" or type1Pokemon == "Plante" or type1Pokemon == "Poison" or type1Pokemon == "Vol" or type1Pokemon == "Insecte" or type1Pokemon == "Dragon":
            return 1/2
        elif type1Pokemon == "Eau" or type1Pokemon == "Sol" or type1Pokemon == "Roche":
            return 2
        else:
            return 1
    
    elif typeAttaque == "Electrik":
        if type1Pokemon == "Plante" or type1Pokemon == "Electrik" or type1Pokemon == "Dragon":
            return 1/2
        elif type1Pokemon == "Eau" or type1Pokemon == "Vol":
            return 2
        elif type1Pokemon == "Roche":
            return 0
        else:
            return 1
        
    elif typeAttaque == "Glace":
        if type1Pokemon == "Eau" or type1Pokemon == "Glace":
            return 1/2
        elif type1Pokemon == "Plante" or type1Pokemon == "Sol" or type1Pokemon == "Vol" or type1Pokemon == "Dragon":
            return 2
        else:
            return 0
        
    elif typeAttaque == "Combat":
        if type1Pokemon == "Poison" or type1Pokemon == "Vol" or type1Pokemon == "Psy" or type1Pokemon == "Insecte":
            return 1/2
        elif type1Pokemon == "Normal" or type1Pokemon == "Glace" or type1Pokemon == "Roche":
            return 2
        elif type1Pokemon == "Spectre":
            return 0
        else:
            return 1
        
    elif typeAttaque == "Poison":
        if type1Pokemon == "Poison" or type1Pokemon == "Sol" or type1Pokemon == "Roche" or type1Pokemon == "Spectre":
            return 1/2
        elif type1Pokemon == "Plante" or type1Pokemon == "Insecte":
            return 2
        else:
            return 1
        
    elif typeAttaque == "Sol":
        if type1Pokemon == "Plante" or type1Pokemon == "Insecte":
            return 1/2
        elif type1Pokemon == "Feu" or type1Pokemon == "Electrik" or type1Pokemon == "Poison" or type1Pokemon == "Roche":
            return 2
        elif type1Pokemon == "Vol":
            return 0
        else:
            return 1
        
    elif typeAttaque == "Vol":
        if type1Pokemon == "Electrik" or type1Pokemon == "Roche":
            return 1/2
        elif type1Pokemon == "Plante" or type1Pokemon == "Combat" or type1Pokemon == "Insecte":
            return 2
        else:
            return 1
        
    elif typeAttaque == "Psy" :
        if type1Pokemon == "Combat" or type1Pokemon == "Poison":
            return 2
        elif type1Pokemon == "Psy":
            return 1/2
        else:
            return 1
    
    elif typeAttaque == "Insecte":
        if type1Pokemon == "Plante" or type1Pokemon == "Poison" or type1Pokemon == "Psy":
            return 2
        elif type1Pokemon == "Feu" or type1Pokemon == "Combat" or type1Pokemon == "Vol" or type1Pokemon == "Spectre":
            return 1/2
        else:
            return 1
        
    elif typeAttaque == "Roche":
        if type1Pokemon == "Feu" or type1Pokemon == "Glace" or type1Pokemon == "Vol" or type1Pokemon == "Insecte":
            return 2
        elif type1Pokemon == "Combat" or type1Pokemon == "Sol":
            return 1/2
        else:
            return 1
    
    elif typeAttaque == "Spectre":
        if type1Pokemon == "Spectre":
            return 2
        elif type1Pokemon == "Normal" or type1Pokemon == "Psy":
            return 0
        else:
            return 1
    elif typeAttaque == "Dragon":
        if type1Pokemon == "Dragon":
            return 2
        else:
            return 1

#A FINIR
def valT(vitesse):
    if vitesse%2 == 0:
        return vitesse
    valModif = int(vitesse)
    if valModif%2 == 0:
        valModif += 2
    else:
        valModif += 1
    if valModif > 255:
        valModif = 255
    return valModif
print(valT(600))
