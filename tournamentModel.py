from tinydb import TinyDB, Query

db = TinyDB('db.json')

class Tournament:
    def __init__(self, name, place, date, time_control, description, choose_player_one, choose_player_two, choose_player_three,choose_player_four,choose_player_five,choose_player_six,choose_player_seven,choose_player_eight):
        self.id = -1
        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.description = description
        self.choose_player_one = choose_player_one
        self.choose_player_two = choose_player_two
        self.choose_player_three = choose_player_three
        self.choose_player_four = choose_player_four
        self.choose_player_five = choose_player_five
        self.choose_player_six = choose_player_six
        self.choose_player_seven = choose_player_seven
        self.choose_player_eight = choose_player_eight

    @classmethod
    def getAlltournament(cls):
        tournamentQuery = Query()
        results = db.search(tournamentQuery._type == 'tournament')
        tournaments = []
        for r in results:
            tournaments.append(cls.deserialize(r))
        return tournaments

    def serialize(self):
        tournament = {'name': self.name, 'place': self.place, 'date': self.date, 'time_control': self.time_control, 'descirption': self.description, 'choose_player_one': self.choose_player_one, 'choose_player_two': self.choose_player_two, 'choose_player_three': self.choose_player_three, 'choose_player_four': self.choose_player_four, 'choose_player_five': self.choose_player_five, 'choose_player_six': self.choose_player_six, 'choose_player_seven': self.choose_player_seven, 'choose_player_eight': self.choose_player_eight}
        return tournament

    @classmethod
    def deserialize(self, tournament):
        name = tournament['name']
        place = tournament['place']
        date = tournament['date']
        time_control = tournament['time_control']
        description = tournament['description']
        choose_player_one = tournament['choose_player_one']
        choose_player_two = tournament['choose_player_two']
        choose_player_three = tournament['choose_player_three']
        choose_player_four = tournament['choose_player_four']
        choose_player_five = tournament['choose_player_five']
        choose_player_six = tournament['choose_player_six']
        choose_player_seven = tournament['choose_player_seven']
        choose_player_eight = tournament['choose_player_eight']
        tournament = Tournament(name=name, place=place, date=date, time_control=time_control, description=description, choose_player_one=choose_player_one, choose_player_two=choose_player_two, choose_player_three=choose_player_three, choose_player_four=choose_player_four, choose_player_five=choose_player_five, choose_player_six=choose_player_six, choose_player_seven=choose_player_seven, choose_player_eight=choose_player_eight)
        return tournament

    def create(self):
        self.id = db.insert(self.serialize())
        self.update()

    @classmethod
    def read(cls, name):
        tournamentQuery = Query()
        results = db.search(tournamentQuery.name == name)
        tournament = Tournament.deserialize(results[0])
        for result in results:
            print(result)

    def update(self):
        db.update(self.serialize(), doc_ids=[self.id])

    def delete(self, name):
        tournamentQuery = Query()
        db.remove(tournamentQuery.name == self.name)
        return True
