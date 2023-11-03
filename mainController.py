from menuView import MenuView
from playerView import PlayerView
from tournamentView import TournamentView
from playersListView import PlayersListView
from playerModel import Player
from tournamentModel import Tournament
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
                self.create_tournament()
            elif choice == 3:
                print("show player list")
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
        tournament.create()

    def show_players_list(self):
        choice_list = int(self.playersListView.show_lists_player())
        if choice_list == 1:
            players = mainController.players_alphabetic_order()
            sorted_list = sorted(players.split())              #sorted(Player.getAllPlayer())
            print(sorted_list)
        elif choice_list == 2:
            players = mainController.players_alphabetic_order()
            sorted_list = sorted(players)              #sorted(Player.getAllPlayer())
            print(sorted_list)
        elif choice_list == 3:
            print()
        elif choice_list == 4:
            print()
        elif choice_list == 5:
            self.menu()
        else:
            print("Le choix n'est pas valide!!!")
            self.show_lists_player()

    def players_alphabetic_order(self, players):
        try:
            players = Player.getAll()
            self.playerView.show_lists_player(players)
            return True
        except Exception as e:
            print('Erreur:', str(e))
            return False