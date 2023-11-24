from View.errorView import InputCheckView


class MenuView:

    def __init__(self):
        self.validate = InputCheckView()

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
        choix = self.validate.input_in_array_of_int("Tapez votre choix : ", range(1, 7))
        return choix

    def show_lists_player(self):
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir.\n"
              "1 : Liste des joueurs par ordre alphabétique\n"
              "2 : Liste des joueurs selon le classement\n"
              "3 : Revenir au menu\n")
        choice = self.validate.input_in_array_of_int("Tapez votre choix : ", range(1, 4))
        return choice

    def tournament_menu(self):
        print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir.\n"
              "1 : Créer un round\n"
              "2 : Terminer un round\n"
              "3 : Afficher les rounds\n"
              "4 : Afficher les joueurs par ordre alphabétique\n"
              "5 : Afficher les joueurs par score\n"
              "6 : Revenir au menu\n")
        choice_t_menu = self.validate.input_in_array_of_int("Tapez votre choix : ", range(1, 7))
        return choice_t_menu
