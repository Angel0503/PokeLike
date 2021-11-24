#include "Pokemon.h"
#include <iostream>

using namespace std;
//!Constructeur
//Par defaut
Pokemon::Pokemon() : m_nom("Tiplouf"), m_type("Eau"), m_vie(100) {

}
//Surchargé
Pokemon::Pokemon(string nom, string type1, sring Attaque attaque1, Attaque attaque2, Attaque attaque3, Attaque attaque4) : m_nom("Roucoul"), m_type("Normal"), m_vie(100),
m_attaque1(attaque1), m_attaque2(attaque2), m_attaque3(attaque3), m_attaque4(attaque4)  {

}

void Pokemon::recevoirDegats(int nbDegats){
    m_vie -= nbDegats;
    if(m_vie < 0){
        m_vie = 0;
    }
}

void Pokemon::attaquer(Pokemon &cible, Attaque attaque){
    
    cible.recevoirDegats(attaque.getDegats());
}

bool Pokemon::estVivant() const{
    return m_vie > 0;
}

void Pokemon::afficherEtat() const{
   cout << "Nom : " << m_nom <<endl;
   cout << "Type : " << m_type <<endl;
   cout << "Vie : " << m_vie <<endl;
}