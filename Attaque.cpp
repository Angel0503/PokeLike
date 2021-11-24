#include "Attaque.h"
#include <iostream>
using namespace std;

Attaque::Attaque() : m_nom("Jet d'O"), m_degats(15), m_pc(20), m_coutPc(1) {

}

Attaque::Attaque(string nom, int degats, int pc, int coutPc) : m_nom(nom), m_degats(degats), m_pc(pc), m_coutPc(coutPc) {

}


void Attaque::afficher() {
    cout << "Nom : " << m_nom << endl;
    cout << "Degats : " << m_degats << endl;
    cout << "Pc Totaux : " << m_pc << endl;
    cout << "Cout en pc : " << m_coutPc << endl;
}

int Attaque::getDegats() const {
    return m_degats;
}

int Attaque::getCoutPc() const {
    return m_coutPc;
}

void Attaque::pcDecrease() {
    m_pc -= m_coutPc;
}