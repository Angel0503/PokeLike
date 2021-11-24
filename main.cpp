#include <iostream>
#include "Pokemon.h"
#include "Attaque.h"
#include "game-tools.h"

using namespace std;
void attaquer(Pokemon attaquant, Pokemon &cible);

int main() {

    Pokemon tiplouf;
    Attaque pistO;

    Attaque charge("charge", 10, 20, 2);
    Pokemon roucool(charge);

    string pokeTour;
    Pokemon doitJouer;
    Pokemon attend;
    Attaque possible;
    Attaque attente;

    int i = 1;
    //int tour;
    int choix;
    while(tiplouf.estVivant() && roucool.estVivant()) {
        cout << "Tour numero " << i << endl;
        cout << "Choisir qui attaque" << endl << " 1 pour roucool et 2 pour tiplouf : ";
        cin >> choix;
        if(choix == 1) {
            attaquer(roucool, tiplouf);
        }
        else {
            attaquer(tiplouf, roucool);
        }
        i++;
    }

    return 0;
}

void attaquer(Pokemon attaquant, Pokemon &cible) {
    attaquant.attaquer(cible);
    attaquant.afficherEtat();
    cout << endl;
    cible.afficherEtat();
    cout << endl;
}
    