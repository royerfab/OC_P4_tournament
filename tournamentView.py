class TournamentView:

    def prompt_for_tournament(self):
        name = input("tapez le nom du tournoi : ")
        place = input("tapez le lieu du tournoi : ")
        date = input("tapez la date du tournoi : ")
        time_control = input("tapez le temps du tournoi : ")
        description = input("tapez la description du tournoi : ")
        choose_players = input("Choisissez huit joueurs")
        choose_player_one = input("Entrez le numéro du joueur 1")
        choose_player_two = input("Entrez le numéro du joueur 2")
        choose_player_three = input("Entrez le numéro du joueur 3")
        choose_player_four = input("Entrez le numéro du joueur 4")
        choose_player_five = input("Entrez le numéro du joueur 5")
        choose_player_six = input("Entrez le numéro du joueur 6")
        choose_player_seven = input("Entrez le numéro du joueur 7")
        choose_player_eight = input("Entrez le numéro du joueur 8")
        return {'name': name, 'place': place, 'date': date, 'time_control': time_control, 'description': description, 'choose_player_one': choose_player_one, 'choose_player_two': choose_player_two, 'choose_player_three': choose_player_three, 'choose_player_four': choose_player_four, 'choose_player_five': choose_player_five, 'choose_player_six': choose_player_six, 'choose_player_seven': choose_player_seven, 'choose_player_eight': choose_player_eight}
