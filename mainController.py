from menuView import MenuView
from playerView import PlayerView
from tournamentView import TournamentView
from playerModel import Player
from tournamentModel import Tournament, Round, Match
class MainController:

    menuView = MenuView()
    playerView = PlayerView()
    tournamentView = TournamentView()
    def start(self):
        self.menuView.bienvenue()
        while True :
            choice = int(self.menuView.menu())
            if choice == 1:
                self.create_player()
            elif choice == 2:
                tournament = self.create_tournament()
                #commencer les tours
                self.create_round(tournament)
            elif choice == 3:
                self.load_tournament()
            elif choice == 4:
                self.show_players_list()
            elif choice == 5:
                self.update_ranking()
            elif choice == 6:
                break
            elif choice != 1 or 2 or 3 or 4 or 5 or 6:
                print("Le choix n'est pas valide !!!")

    def create_player(self):
        new_player = self.playerView.prompt_for_player()
        player = Player(**new_player)
        player.create()

    def create_tournament(self):
        new_tournament = self.tournamentView.prompt_for_tournament()
        tournament = Tournament(**new_tournament)
        tournament.players = self.tournamentView.select_players(Player.getAllplayer())
        tournament.create()
        return tournament


    def show_players_list(self):
        while True:
            choice_list = int(self.menuView.show_lists_player())
            if choice_list == 1:
                players = Player.getAllplayer()
                print(players)
            elif choice_list == 2:
                players = self.players_alphabetic_order()
                sorted_list = sorted(players)              #sorted(Player.getAllPlayer())
                print(sorted_list)
            elif choice_list == 3:
                break
            else:
                print("Le choix n'est pas valide!!!")

    def update_ranking(self):
        update_player = self.playerView.select_player(Player.getAllplayer())
        update_player.classement = self.playerView.update_ranking()
        update_player.update()

    def create_round(self, tournament):
        round = Round('1', tournament.id)
        round.create()
        players = tournament.players
        # création de match pour le round 1
        for i in range (0, 8, 2):
            #print(players[i], 'vs', players[i+1])
            player_one = players[i].id
            player_two = players[i+1].id
            result = (0, 0)
            match = Match(player_one, player_two, result, round.id)
            match.create()
        #mettre à jour le score des match
        self.update_match_result(round)

    def update_match_result(self, round):
        matches = Match.get_match_by_round(round.id)
        for match in matches:
            result = self.tournamentView.set_match_score(match)
            match.result = result
            match.update()

    def load_tournament(self):
        tournaments = Tournament.getAlltournament()
        choice = self.tournamentView.select_tournament(tournaments)
        tournament = Tournament.read(choice)
        self.create_round(tournament)
        return tournament