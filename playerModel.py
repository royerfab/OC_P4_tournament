from tinydb import TinyDB, Query

db = TinyDB('db.json').table("player")

class Player:
    def __init__(self, last_name, first_name, date_of_birth, sexe, classement, age):
        self.id = -1
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.classement = classement
        self.age = age
        self.score = 0
        #indiquer que le chiffre est forcément positif? Mettre if où on réupère la valeur

    def __str__(self):
        return f'{self.first_name} {self.last_name}, classement : {self.classement}'

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, classement : {self.classement}'

    @classmethod
    def getAllplayer(cls):
        players = []
        for r in db.all():
            players.append(cls.deserialize(r))
        return players

    def serialize(self):
        player = {'id': self.id, 'last_name': self.last_name, 'first_name': self.first_name, 'date_of_birth': self.date_of_birth, 'sexe': self.sexe, 'classement': self.classement, 'age': self.age, 'score': self.score}
        return player

    @classmethod
    def deserialize(cls, player):
        last_name = player['last_name']
        first_name = player['first_name']
        date_of_birth = player['date_of_birth']
        sexe = player['sexe']
        classement = player['classement']
        age = player['age']
        player_object = Player(last_name=last_name, first_name=first_name, date_of_birth=date_of_birth, sexe=sexe, classement=classement, age=age)
        player_object.id = player['id']
        player_object.score = player['score']
        return player_object

    def create(self):
        self.id = db.insert(self.serialize())
        self.update()

    @classmethod
    def read(cls, id):
        return cls.deserialize(db.get(doc_id=id))

    def update(self):
        db.update(self.serialize(), doc_ids=[self.id])

    #On n'utilise pas juste update pour plus de simplicité et ne pas réécrire dans le contrôleur
    def update_score(self, score):
        self.score = self.score + score
        self.update()

    @classmethod
    def get_tournament_player(cls, player_id_list):
        player_db = db.all()
        players = []
        for r in player_db:
            if r['id'] in player_id_list:
                players.append(cls.deserialize(r))
        return players