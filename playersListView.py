class PlayersListView:

        def show_lists_player(self):
            print("Entrez le numéro correspondant à l'action que vous souhaitez accomplir."
                "1 Liste des joueurs par ordre alphabétique"
                "2 Liste des joueurs selon le classement"
                "3 Liste des acteurs par ordre alphabétique"
                "4 Liste des acteurs selon le classement"
                "5 Revenir au menu")
            choice = input("Tapez votre choix : ")
            return choice