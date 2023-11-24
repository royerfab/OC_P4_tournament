from tinydb import TinyDB, Query, where

db_match = TinyDB('db.json').table('match')


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
