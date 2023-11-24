from View.errorView import ErrorHandlerView
from View.menuView import MenuView
from View.playerView import PlayerView
from Controller.tournamentController import TournamentController
from View.tournamentView import TournamentView
from Model.playerModel import Player
from Model.tournamentModel import Tournament


class MainController:
    menuView = MenuView()
    playerView = PlayerView()
    tournamentView = TournamentView()

    def start(self):
        self.menuView.bienvenue()
        while True:
            choice = int(self.menuView.menu())
            if choice == 1:
                self.create_player()
            elif choice == 2:
                if len(Player.getAllPlayer()) < 8:
                    ErrorHandlerView().display_error("8 joueurs sont nécessaires pour créer un tournoi")
                else:
                    tournament = self.create_tournament()
                    TournamentController(tournament).menu()
            elif choice == 3:
                self.load_tournament()
            elif choice == 4:
                self.show_players_list()
            elif choice == 5:
                self.update_ranking()
            elif choice == 6:
                break

    def create_player(self):
        new_player = self.playerView.prompt_for_player()
        player = Player(**new_player)
        player.create()

    def create_tournament(self):
        new_tournament = self.tournamentView.prompt_for_tournament()
        tournament = Tournament(**new_tournament)
        tournament.players = self.tournamentView.select_players(Player.getAllPlayer())
        tournament.create()
        return tournament

    def show_players_list(self):
        while True:
            choice_list = int(self.menuView.show_lists_player())
            if choice_list == 1:
                sorted_list = sorted(Player.getAllPlayer(), key=lambda p: (p.last_name, p.first_name))
                self.tournamentView.show_players(sorted_list)
            elif choice_list == 2:
                sorted_list = sorted(Player.getAllPlayer(), key=lambda p: p.classement)
                self.tournamentView.show_players(sorted_list)
            elif choice_list == 3:
                break

    def update_ranking(self):
        update_player = self.playerView.select_player(Player.getAllPlayer())
        update_player.classement = self.playerView.update_ranking()
        update_player.update()

    def load_tournament(self):
        tournaments = Tournament.getAlltournament()
        choice = self.tournamentView.select_tournament(tournaments)
        tournament = Tournament.read(choice)
        TournamentController(tournament).menu()
