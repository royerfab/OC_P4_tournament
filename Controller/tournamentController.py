from View.menuView import MenuView
from Model.roundModel import Round
from Model.matchModel import Match
from View.tournamentView import TournamentView


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

    def create_round(self):
        if self.tournament.current_round >= 4:
            self.tournamentView.tournament_end()
        else:
            self.tournament.current_round += 1
            round = Round(self.tournament.current_round, self.tournament.id)
            round.create()
            if self.tournament.current_round == 1:
                self.first_pairing(round)
            else:
                self.other_pairing(round)
            self.tournament.update()

    def first_pairing(self, round):
        for i in range(0, 8, 2):
            player_one = self.tournament.players[i].id
            player_two = self.tournament.players[i + 1].id
            result = (0, 0)
            match = Match(player_one, player_two, result, round.id)
            match.create()

    def other_pairing(self, round):
        sorted_list_tournament_players = sorted(self.tournament.players, key=lambda player: float(player.score),
                                                reverse=True)
        current_round_matches = []
        for player_1 in sorted_list_tournament_players:

            for player_2 in sorted_list_tournament_players:
                if player_1.id == player_2.id:
                    pass
                else:
                    result = (0, 0)
                    current_match = Match(player_1.id, player_2.id, result, round.id)
                    match_exist = self.check_existing_match(current_round_matches, current_match)
                    if match_exist:
                        self.tournamentView.match_exist(player_1.id, player_2.id)
                    else:
                        current_match_exist = self.check_existing_play_in_current_round(current_round_matches,
                                                                                        current_match)
                        if current_match_exist:
                            self.tournamentView.one_player()
                        else:
                            self.tournamentView.new_match(player_1.id, player_2.id)
                            current_match.create()
                            current_round_matches.append([[player_1.id, 0], [player_2.id, 0]])

    def check_existing_match(self, current_round_matches, current_match):
        tournament_round = Round.get_round_by_tournament(self.tournament.id)
        old_matches = current_round_matches.copy()
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
            self.tournament.players[player_1_idx].score += result[0]
            self.tournament.players[player_2_idx].score += result[1]
        round.end_round()
        round.update()
        self.tournament.update()

    def show_tournament_players_list(self):
        sorted_list = sorted(self.tournament.players, key=lambda p: (p.last_name, p.first_name))
        self.tournamentView.show_players(sorted_list)

    def show_tournament_players_by_score(self):
        sorted_list_tournament_players = sorted(self.tournament.players, key=lambda player: float(player.score),
                                                reverse=True)
        self.tournamentView.show_players(sorted_list_tournament_players)

    def show_tournament_round(self):
        rounds = Round.get_round_by_tournament(self.tournament.id)
        matches = Match.get_match_by_round(self.tournament.id)
        self.tournamentView.show_round(rounds, matches)
