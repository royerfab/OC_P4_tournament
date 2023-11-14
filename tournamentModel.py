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

#création d'une liste des tournois contenant tous les tournois trouvés dans la base de donnée et desérialisés
    @classmethod
    def getAlltournament(cls):
        tournaments = []
        for r in db.all():
            tournaments.append(cls.deserialize(r))
        return tournaments

#TODO ligne players explications?
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

#Deserialize : classmethod pour ,
    #TODO pourquoi classmathod?
    @classmethod
    def deserialize(self, tournament):
        place = tournament['place']
        date = tournament['date']
        time_control = tournament['time_control']
        # TODO : corriger faute de frappe
        description = tournament['descirption']
        tournament_object = Tournament(
            #TODO pourquoi écrire comme ça?
            name=tournament["name"],
            place=place,
            date=date,
            time_control=time_control,
            description=description)
        #TODO pourquoi changer tournament en tournament_object?
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

    #class Round : création de la classe Round et du constructeur, un round a un nom, l'id permet d'identifier chaque round.
    #TODO tournament id
class Round:
    def __init__(self, name, tournament_id, matches=[]):
        self.id = -1
        self.name = name
        self.tournament_id = tournament_id
        self.matches = matches

    #Dans le tupple matches, ajout de deux listes comprenant chacune un joueur et un score pour le match
    def add_matches(self, match):
        self.matches.append(
            ([match.player_one, match.result[0]], [match.player_two, match.result[1]])
        )
        self.update()
#serialize : création du dictionnaire round avec 3 clés venues du constructeur, pas besoin de désérialiser on ne récupérera pas la donnée directement.
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


#create : avec Tinydb on enregistre avec insert le dictionnaire round dans la base de données,
    #TODO pourquoi self.id? pourquoi self.update() ici et pas juste create?
    def create(self):
        self.id = db_round.insert(self.serialize())
        self.update()

#update : avec Tinydb on modifie avec update le dictionnaire round dans la base de données, doc_ids permet de retrouver l'id du round à modifier
    def update(self):
        db_round.update(self.serialize(), doc_ids=[self.id])

    @classmethod
    def get_round_by_tournament(cls, tournament_id):
        # matches_db = db_match.search(where('round_id') == round_id)
        RoundQuery = Query()
        round_db = db_round.search(RoundQuery.tournament_id == int(tournament_id))
        rounds = []
        for r in round_db:
            rounds.append(cls.deserialize(r))
        return rounds

    #class Match : création de la classe Match et du constructeur, 4 paramètres, l'id permet d'identifier chaque match.
    # TODO round_id
class Match:

    def __init__(self, player_one, player_two, result, round_id):
        self.player_one = player_one
        self.player_two = player_two
        self.result = result
        self.round_id = round_id
        self.id = -1

    # serialize : création du dictionnaire match avec 4 clés venues du constructeur, le résultat est placé sous forme de liste.
    def serialize(self):
        match = {
            'id': self.id,
            'player_one': self.player_one,
            'player_two': self.player_two,
            'result': list(self.result),
            'round_id': self.round_id
        }
        return match

    # create : avec Tinydb on enregistre avec insert le dictionnaire match dans la base de données,
    def create(self):
        self.id = db_match.insert(self.serialize())
        self.update()

    # update : avec Tinydb on modifie avec update le dictionnaire round dans la base de données, doc_ids permet de retrouver l'id du round à modifier
    def update(self):
        db_match.update(self.serialize(), doc_ids=[self.id])

#get_match : dans les matchs de la base de données on uilise Query avec search, on crée une liste dans laquelle on intègre avec append chaque match du round désérialisé de la base de données
    #TODO on retrouve le round avec match_id,
    @classmethod
    def get_match_by_round(cls, round_id):
        #matches_db = db_match.search(where('round_id') == round_id)
        MatchQuery = Query()
        matches_db = db_match.search(MatchQuery.round_id == int(round_id))
        matches = []
        for r in matches_db:
            matches.append(cls.deserialize(r))
        return matches

#deserialize :
    #TODO : pareil que tournoi
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