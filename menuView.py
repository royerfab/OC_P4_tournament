class MenuView:
    def bienvenue(self):
        print("Bienvenue")
        print("\n")

    def menu(self):
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir.\n"
              "1 : Créer un joueur\n"
              "2 : Créer un tournoi\n"
              "3 : Charger un tournoi\n"
              "4 : Voir les listes de joueurs\n"
              "5 : Modifier le classement\n"
              "6 : Quitter le programme\n")
        choix = input("Tapez votre choix : ")
        return choix

    def show_lists_player(self):
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir.\n"
              "1 : Liste des joueurs par ordre alphabétique\n"
              "2 : Liste des joueurs selon le classement\n"
              "3 : Revenir au menu\n")
        choice = input("Tapez votre choix : ")
        return choice

    def tournament_menu(self):
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir.\n"
              "1 : Créer un round\n"
              "2 : Terminer un round\n"
              "3 : Afficher les rounds\n"
              "4 : Afficher les matchs\n"
              "5 : Afficher les joueurs\n"
              "6 : Revenir au menu\n")
        choice_t_menu = input("Tapez votre choix : ")
        return choice_t_menu