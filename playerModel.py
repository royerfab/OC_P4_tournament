from tinydb import TinyDB, Query

db = TinyDB('db.json')

class Player:
    def __init__(self, last_name, first_name, date_of_birth, sexe, classement, age, score):
        self.id = -1
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.classement = classement
        self.age = age
        self.score = 0
        #indiquer que le chiffre est forcément positif? Mettre if où on réupère la valeur

    @classmethod
    def getAllplayer(cls):
        playerQuery = Query()
        results = db.search(playerQuery._type == 'player')
        players = []
        for r in results:
            players.append(cls.deserialize(r))
        return players

    def serialize(self):
        player = {'last_name': self.last_name, 'first_name': self.first_name, 'date_of_birth': self.date_of_birth, 'sexe': self.sexe, 'classement': self.classement, 'age': self.age}
        return player

    @classmethod
    def deserialize(cls, player):
        last_name = player['last_name']
        first_name = player['first_name']
        date_of_birth = player['date_of_birth']
        sexe = player['sexe']
        classement = player['classement']
        age = player['age']
        player = Player(last_name=last_name, first_name=first_name, date_of_birth=date_of_birth, sexe=sexe, classement=classement, age=age)
        return player

    def create(self):
        self.id = db.insert(self.serialize())
        self.update()

    @classmethod
    def read(cls, last_name):
        playerQuery = Query()
        results = db.search(playerQuery.last_name == last_name)
        player = Player.deserialize(results[0])
        for result in results:
            print(result)

    def update(self):
        db.update(self.serialize(), doc_ids=[self.id])

