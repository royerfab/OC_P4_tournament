from datetime import datetime
from tinydb import TinyDB, Query

db_round = TinyDB('db.json').table('round')


class Round:
    def __init__(self, name, tournament_id, matches=[]):
        self.id = -1
        self.name = name
        self.start_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        self.end_time = None
        self.tournament_id = tournament_id
        self.matches = matches

    def add_matches(self, match):
        self.matches.append(
            ([match.player_one, match.result[0]], [match.player_two, match.result[1]])
        )
        self.update()

    def serialize(self):
        round = {
            'id': self.id,
            'name': self.name,
            'tournament_id': self.tournament_id,
            'matches': self.matches
        }
        return round

    @classmethod
    def deserialize(self, round):
        name = round['name']
        matches = round['matches']
        tournament_id = round['tournament_id']
        round_object = Round(
            name=name,
            matches=matches,
            tournament_id=tournament_id
        )
        round_object.id = round['id']
        return round_object

    def create(self):
        self.id = db_round.insert(self.serialize())
        self.update()

    def update(self):
        db_round.update(self.serialize(), doc_ids=[self.id])

    @classmethod
    def get_round_by_tournament(cls, tournament_id):
        RoundQuery = Query()
        round_db = db_round.search(RoundQuery.tournament_id == int(tournament_id))
        rounds = []
        for r in round_db:
            rounds.append(cls.deserialize(r))
        return rounds

    def end_round(self):
        self.end_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
