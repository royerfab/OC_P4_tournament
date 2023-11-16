from menuView import MenuView
from playerView import PlayerView
from tournamentController import TournamentController
from tournamentView import TournamentView
from playerModel import Player
from tournamentModel import Tournament, Round, Match

#TODO pourquoi une classe MainController sans objets?
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
                TournamentController(tournament).menu()
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

    #TODO COmment fonctionne sorted ici?
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


    #TODO parcours utilisation tournoi : choix 3 menuView, appel load_tournament ici, recupère avec getalltournament plus haut, recupère choix de select_tournament dans tournamentview, lit le choix et selon le choix crée un round dans tournament_state en dessous
    def load_tournament(self):
        tournaments = Tournament.getAlltournament()
        choice = self.tournamentView.select_tournament(tournaments)
        tournament = Tournament.read(choice)
        TournamentController(tournament).menu()


