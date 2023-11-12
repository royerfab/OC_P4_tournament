from playerView import PlayerView


class TournamentView:

    def prompt_for_tournament(self):
        name = input("tapez le nom du tournoi : ")
        place = input("tapez le lieu du tournoi : ")
        date = input("tapez la date du tournoi : ")
        time_control = input("tapez le temps du tournoi : ")
        description = input("tapez la description du tournoi : ")
        return {'name': name, 'place': place, 'date': date, 'time_control': time_control, 'description': description}

    def select_players(self, players):
        selected_players = []
        while True:
            player = PlayerView().select_player(players)
            selected_players.append(player)
            players.remove(player)
            if len(selected_players) == 8:
                break
        return selected_players

    def select_tournament(self, tournaments):
        for tournament in tournaments:
            print(tournament.id, tournament.name)

        choice = int(input("Entrez l'id du tournoi à charger : "))
        return choice

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
