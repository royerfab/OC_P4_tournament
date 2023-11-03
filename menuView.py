class MenuView:
    def bienvenue(self):
        print("Bienvenue")
        print("\n")

    def menu(self):
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir.\n"
              "1 : Créer un joueur\n"
              "2 : Créer un tournoi\n"
              "3 : Charger un tournoi\n"
              "4 Voir les listes de joueurs\n"
              "5 Modifier le classement\n"
              "6 : Quitter le programme\n")
        choix = input("Tapez votre choix : ")
        return choix

