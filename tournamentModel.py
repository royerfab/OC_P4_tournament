from tinydb import TinyDB, Query, where

from playerModel import Player

db = TinyDB('db.json').table('tournament')
db_round = TinyDB('db.json').table('round')
db_match = TinyDB('db.json').table('match')


class Tournament:
    def __init__(self, name, place, date, time_control, description):
        self.id = -1
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.description = description
        self.rounds = 4
        self.rounds_list = []
        self.current_round = 0
        self.players = []


    @classmethod
    def getAlltournament(cls):
        tournaments = []
        for r in db.all():
            tournaments.append(cls.deserialize(r))
        return tournaments

    def serialize(self):
        tournament = {
            'id': self.id,
            'name': self.name,
            'place': self.place,
            'date': self.date,
            'time_control': self.time_control,
        # TODO : corriger faute de frappe
            'descirption': self.description,
            'rounds': self.rounds,
            'current_round': self.current_round,
            'players': [p.serialize() for p in self.players],
        }
        return tournament

    @classmethod
    def deserialize(self, tournament):
        place = tournament['place']
        date = tournament['date']
        time_control = tournament['time_control']
        # TODO : corriger faute de frappe
        description = tournament['descirption']
        tournament_object = Tournament(
            name=tournament["name"],
            place=place,
            date=date,
            time_control=time_control,
            description=description)
        tournament_object.id = tournament['id']
        tournament_object.rounds = tournament['rounds']
        tournament_object.current_round = tournament['current_round']
        tournament_object.players = [Player.deserialize(p) for p in tournament['players']]
        return tournament_object

    def create(self):
        self.id = db.insert(self.serialize())
        self.update()

    @classmethod
    def read(cls, id):
        return cls.deserialize(db.get(doc_id=id))

    def update(self):
        db.update(self.serialize(), doc_ids=[self.id])

class Round:
    def __init__(self, name, tournament_id):
        self.id = -1
        self.name = name
        self.tournament_id = tournament_id

    def serialize(self):
        round = {
            'id': self.id,
            'name': self.name,
            'tournament_id': self.tournament_id
        }
        return round

    def create(self):
        self.id = db_round.insert(self.serialize())
        self.update()

    def update(self):
        db_round.update(self.serialize(), doc_ids=[self.id])

class Match:

    def __init__(self, player_one, player_two, result, round_id):
        self.player_one = player_one
        self.player_two = player_two
        self.result = result
        self.round_id = round_id
        self.id = -1

    def serialize(self):
        match = {
            'id': self.id,
            'player_one': self.player_one,
            'player_two': self.player_two,
            'result': list(self.result),
            'round_id': self.round_id
        }
        return match

    def create(self):
        self.id = db_match.insert(self.serialize())
        self.update()

    def update(self):
        db_match.update(self.serialize(), doc_ids=[self.id])

    @classmethod
    def get_match_by_round(cls, round_id):
        #matches_db = db_match.search(where('round_id') == round_id)
        MatchQuery = Query()
        matches_db = db_match.search(MatchQuery.round_id == int(round_id))
        matches = []
        for r in matches_db:
            matches.append(cls.deserialize(r))
        return matches

    @classmethod
    def deserialize(self, match):
        player_one = match['player_one']
        player_two = match['player_two']
        result = match['result']
        round_id = match['round_id']
        match_object = Match(
            player_one=player_one,
            player_two=player_two,
            result=result,
            round_id=round_id
            )
        match_object.id = match['id']
        return match_object