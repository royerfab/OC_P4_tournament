from menuView import MenuView
from playerModel import Player
from tournamentModel import Round, Match
from tournamentView import TournamentView


class TournamentController:
    def __init__(self, tournament):
        self.tournament = tournament
        self.menuView = MenuView()
        self.tournamentView = TournamentView()

    def menu(self):
        while True:
            choice_t_menu = int(self.menuView.tournament_menu())
            if choice_t_menu == 1:
                self.create_round()
            elif choice_t_menu == 2:
                rounds = Round.get_round_by_tournament(self.tournament.id)
                self.update_match_result(rounds[-1])
            elif choice_t_menu == 3:
                self.show_tournament_round()
            elif choice_t_menu == 4:
                self.show_tournament_players_list()
            elif choice_t_menu == 5:
                self.show_tournament_players_by_score()
            elif choice_t_menu == 6:
                break
            else:
                print("Le choix n'est pas valide!!!")

#Création de la variable round contenant le nom et l'id du tournoi de la classe Round, sélection des paires de joueurs avec range avec un pas de 2 pour ne pas prendre les mêmes et création du score, avec ces données et 'id du round on crée une instance match avec le create() du modèle
    # TODO create_round : pourquoi paramètre tournament, pourquoi tournament.players
    def create_round(self):
        self.tournament.current_round+=1
        round = Round(self.tournament.current_round, self.tournament.id)
        round.create()
        if self.tournament.current_round==1:
            self.first_pairing(round)
        else:
            self.other_pairing(round)

    def first_pairing(self, round):
        for i in range(0, 8, 2):
            # print(players[i], 'vs', players[i+1])
            player_one = self.tournament.players[i].id
            player_two = self.tournament.players[i + 1].id
            result = (0, 0)
            match = Match(player_one, player_two, result, round.id)
            match.create()


    #player 1 et 2 id pour pas que la deuxième boucle ne reprenne pas le même que la première dans la même liste, On crée une liste des anciens matches y compris de ce round, à chaque fois qu'un match est créé dans la boucle 1 il est rajouté à la liste pour le prendre en compte dans la boucle 2 et ne pas le refaire
    def other_pairing(self, round):
        sorted_list_tournament_players = sorted(self.tournament.players, key=lambda player: float(player.score), reverse=True)
        current_round_matches = []
        for player_1 in sorted_list_tournament_players:

            for player_2 in sorted_list_tournament_players:
                if player_1.id==player_2.id:
                    pass
                else:
                    result = (0, 0)
                    current_match = Match(player_1.id, player_2.id, result, round.id)
                    match_exist = self.check_existing_match(current_round_matches, current_match)
                    if match_exist:
                        print(player_1.id, player_2.id, 'Ont déjà joué')
                    else:
                        current_match_exist = self.check_existing_play_in_current_round(current_round_matches, current_match)
                        if current_match_exist:
                            print("L'un des deux joueurs a déjà joué")
                        else:
                            print(player_1.id, player_2.id, 'Nouveau match')
                            current_match.create()
                            current_round_matches.append([[player_1.id, 0], [player_2.id, 0]])

    #la deuxième boucle vérifie que le couple existant de joueurs pour le match ne correspond pas à un match précédent, avec extend on concatène
    #On met deux listes côte à côté parce que le premier 0 correspond à l'emplacement dans la liste des matchs dans le match en question du premier joueur et le deuxième 0 correspond au premier élément qu'on veut y récupérer donc son id, l'autre double liste on écrit 1 pour avoir le deuxième joueur et 0 pour son id aussi
    def check_existing_match(self, current_round_matches, current_match):
        tournament_round = Round.get_round_by_tournament(self.tournament.id)
        old_matches = current_round_matches
        for old_round in tournament_round:
            old_matches.extend(old_round.matches)
        for old_match in old_matches:
            old_match_player_1 = old_match[0][0]
            old_match_player_2 = old_match[1][0]
            current_match_player_1 = current_match.player_one
            current_match_player_2 = current_match.player_two
            if ((current_match_player_1 == old_match_player_1 and current_match_player_2 == old_match_player_2) or (
                    current_match_player_1 == old_match_player_2 and current_match_player_2 == old_match_player_1)):
                return True
        return False

    def check_existing_play_in_current_round(self, current_round_matches, current_match):
        for old_match in current_round_matches:
            old_match_player_1 = old_match[0][0]
            old_match_player_2 = old_match[1][0]
            current_match_player_1 = current_match.player_one
            current_match_player_2 = current_match.player_two
            if ((current_match_player_1 == old_match_player_1 and current_match_player_2 == old_match_player_2) or
                    (current_match_player_1 == old_match_player_2 and current_match_player_2 == old_match_player_1) or
                    (current_match_player_1 == old_match_player_1 or current_match_player_1 == old_match_player_2) or
                    (current_match_player_2 == old_match_player_1 or current_match_player_2 == old_match_player_2)):
                return True
        return False

    # TODO pourquoi update_score avec p1 et p2 ne sont pas redondants avec add_matches et avec result dans create_round au dessus?
    # TODO revoir le parcours intégral du score : set_match_score dans TournamentView, appelé dans update_match_result ici contenant add_matches du tournament model, appelé dans create_round au-dessus
    def update_match_result(self, round):
        matches = Match.get_match_by_round(round.id)
        for match in matches:
            result = self.tournamentView.set_match_score(match)
            match.result = result
            match.update()
            round.add_matches(match)
            player_1_idx = -1
            player_2_idx = -1
            for idx, player in enumerate(self.tournament.players):
                if match.player_one == player.id:
                    player_1_idx = idx
                if match.player_two == player.id:
                    player_2_idx = idx
            self.tournament.players[player_1_idx].score+=result[0]
            self.tournament.players[player_2_idx].score+=result[1]
        round.end_round()
        round.update()
        self.tournament.update()


# à chaque fois qu'on veut changer le score d'un joueur dans le tournoi, on modifie la iste des joueurs du tournoi en la remplaçant par la liste des mêmes joueurs mais avec un score différent
# TODO pourquoi Player.get_tournament_player, nouveau score remplace l'ancien, ancienne liste et nouvelle liste, comment connaître paramètre ici round?
# TODO où je mets le score du match dans le score du joueur pour le tournoi?
#def update_player_score(self, round):


    # TODO remplacer celle d'au-dessus par ça plus update?


    def show_tournament_players_list(self):
        self.tournamentView.show_players(self.tournament.players)

    def show_tournament_players_by_score(self):
        sorted_list_tournament_players = sorted(self.tournament.players, key=lambda player: float(player.score), reverse=True)
        self.tournamentView.show_players(sorted_list_tournament_players)


    def show_tournament_round(self):
        rounds = Round.get_round_by_tournament(self.tournament.id)
        self.tournamentView.show_round(rounds)