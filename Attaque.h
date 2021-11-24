#ifndef ATTAQUE_H
#define ATTAQUE_H

#include <string>

class Attaque {
    public : 
    Attaque();
    Attaque(std::string nom, int degats, int pc, int coutPc);
    void afficher();
    int getDegats() const;
    int getCoutPc() const;
    void pcDecrease();

    private :
    std::string m_nom;
    int m_degats;
    int m_pc;
    int m_coutPc;

};


#endif