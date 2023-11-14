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

#Création de la variable round contenant le nom et l'id du tournoi de la classe Round, sélection des paires de joueurs avec range avec un pas de 2 pour ne pas prendre les mêmes et création du score, avec ces données et 'id du round on crée une instance match avec le create() du modèle
    #create_round :
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

    #TODO pourquoi update_score avec p1 et p2 ne sont pas redondants avec add_matches et avec result dans create_round au dessus?
    # TODO revoir le parcours intégral du score : set_match_score dans TournamentView, appelé dans update_match_result ici contenant add_matches du tournament model, appelé dans create_round au-dessus
    def update_match_result(self, round):
        matches = Match.get_match_by_round(round.id)
        for match in matches:
            result = self.tournamentView.set_match_score(match)
            match.result = result
            match.update()
            round.add_matches(match)
            # update_players_score
            p1 = Player.read(match.player_one)
            p2 = Player.read(match.player_two)
            p1.update_score(result[0])
            p2.update_score(result[1])
        self.update_player_score(round)

    #TODO parcours utilisation tournoi : choix 3 menuView, appel load_tournament ici, recupère avec getalltournament plus haut, recupère choix de select_tournament dans tournamentview, lit le choix et selon le choix crée un round dans tournament_state en dessous
    def load_tournament(self):
        tournaments = Tournament.getAlltournament()
        choice = self.tournamentView.select_tournament(tournaments)
        tournament = Tournament.read(choice)
        self.tournament_state(tournament)
        return tournament

    def tournament_state(self, tournament):
        rounds = Round.get_round_by_tournament(tournament.id)
        if len(rounds)==0:
            print('Création de round 1')
            self.create_round(tournament)
        elif len(rounds)<4:
            print('Création du round', len(rounds)+1)
        else:
            print('Tournoi terminé')

    #à chaque fois qu'on veut changer le score d'un joueur dans le tournoi, on modifie la iste des joueurs du tournoi en la remplaçant par la liste des mêmes joueurs mais avec un score différent
   #TODO pourquoi Player.get_tournament_player, nouveau score remplace l'ancien, ancienne liste et nouvelle liste
    def update_player_score(self, round):
        tournament = Tournament.read(round.tournament_id)
        players_id_list = []
        for player in tournament.players:
            players_id_list.append(player.id)
        players = Player.get_tournament_player(players_id_list)
        tournament.players = players
        tournament.update()
