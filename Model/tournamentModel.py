from tinydb import TinyDB

from Model.playerModel import Player

db = TinyDB('db.json').table('tournament')


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
