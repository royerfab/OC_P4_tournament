from playerView import PlayerView


class TournamentView:

    def prompt_for_tournament(self):
        name = input("tapez le nom du tournoi : ")
        place = input("tapez le lieu du tournoi : ")
        date = input("tapez la date du tournoi : ")
        time_control = input("tapez le temps du tournoi : ")
        description = input("tapez la description du tournoi : ")
        return {'name': name, 'place': place, 'date': date, 'time_control': time_control, 'description': description}

    #création d'une liste des joueurs sélectionnés, on ajoute avec append dans la liste ceux sélectionnés dans select_player dans playerView, chaque joueur sélectionné est retiré de la liste pour ne pas choisir le m^meme et on limite le choix à 8 avec len
    #TODO pourquoi pas dans le contrôleur?
    def select_players(self, players):
        selected_players = []
        while True:
            player = PlayerView().select_player(players)
            selected_players.append(player)
            players.remove(player)
            if len(selected_players) == 8:
                break
        return selected_players

#Pour sélectionner un tournoi on print pour chaque tournoi son nom et son id, on return le choix fait dans l'input de l'utilisateur, on en fait un entier avec int
    def select_tournament(self, tournaments):
        for tournament in tournaments:
            print(tournament.id, tournament.name)

        choice = int(input("Entrez l'id du tournoi à charger : "))
        return choice

#L'utilisateur entre le résultat, selon l'input un score différent est return
    def set_match_score(self, match):
        print(match.player_one, 'vs', match.player_two)
        print('1. Player 1 a gagné le match')
        print('2. Player 2 a gagné le match')
        print('3. Match nul')
        choice = int(input('Entrez votre choix : '))
        if choice == 1:
            return (1,0)
        elif choice == 2:
            return (0,1)
        elif choice == 3:
            return (0.5,0.5)

    def show_players(self, players):
        for player in players:
            print(player)

    def show_round(self, rounds):
        for round in rounds:
            print(round.id, round.name)