#ifndef POKEMON_H
#define POKEMON_H

#include <string>
#include "Attaque.h"

class Pokemon {
    public :
    //!Constructeur
    Pokemon();
    Pokemon(std::string nom, std::string type1, std::string type2, int vie, Attaque attaque1, Attaque attaque2, Attaque attaque3, Attaque attaque4);

    //!Methode
    void recevoirDegats(int nbDegats);
    void attaquer(Pokemon &cible, Attaque attaque);
    bool estVivant() const;
    void afficherEtat() const;

    private :
    //!Attributs
    std::string m_nom;
    std::string m_type1;
    std::string m_type2;
    int m_vie;
    Attaque m_attaque1;
    Attaque m_attaque2;
    Attaque m_attaque3;
    Attaque m_attaque4;
};

#endif
