from View.playerView import PlayerView
from View.errorView import InputCheckView


class TournamentView:
    def __init__(self):
        self.validate = InputCheckView()

    def prompt_for_tournament(self):
        name = self.validate.check_string("tapez le nom du tournoi : ")
        place = self.validate.check_string("tapez le lieu du tournoi : ")
        date = self.validate.check_date("tapez la date du tournoi (YYYY/MM/DD) : ")
        time_control = self.validate.time_option()
        description = self.validate.check_string("tapez la description du tournoi : ")
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
            print(tournament.id, tournament.name, tournament.date)

        choice = self.validate.input_in_array_of_int("Entrez l'id du tournoi à charger : ",
                                                     range(0, len(tournaments) + 1))
        return choice

    def set_match_score(self, match):
        print(match.player_one, 'vs', match.player_two)
        print('1. Player 1 a gagné le match')
        print('2. Player 2 a gagné le match')
        print('3. Match nul')
        choice = self.validate.input_in_array_of_int('Entrez votre choix : ', range(1, 4))
        if choice == 1:
            return (1, 0)
        elif choice == 2:
            return (0, 1)
        elif choice == 3:
            return (0.5, 0.5)

    def show_players(self, players):
        for player in players:
            print(player)

    def show_round(self, rounds, matches):
        for round in rounds:
            print("Round id : ", round.id, "Nom du round : ", round.name)
            for match in round.matches:
                print('Joueur 1 :', match[0][0], 'Joueur 2 :', match[1][0], 'Résultat : (', match[0][1], '-',
                      match[1][1], ')')

    def match_exist(self, player_one, player_two):
        print(player_one, player_two, 'Ont déjà joué')

    def new_match(self, player_one, player_two):
        print(player_one, player_two, 'Nouveau match')

    def one_player(self):
        print("L'un des deux joueurs a déjà joué")

    def tournament_end(self):
        print('Tournoi terminé)')
