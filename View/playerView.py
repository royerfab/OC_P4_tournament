from View.errorView import InputCheckView


class PlayerView:
    def __init__(self):
        self.validate = InputCheckView()

    def prompt_for_player(self):
        last_name = self.validate.check_string("tapez le nom du joueur : ")
        first_name = self.validate.check_string("tapez le prénom du joueur : ")
        date_of_birth = self.validate.check_date("tapez la date de naissance du joueur (YYYY/MM/DD) : ")
        sexe = self.validate.check_sex("tapez le sexe du joueur : ")
        classement = self.validate.check_int("tapez le classement du joueur : ")
        age = self.validate.check_int("tapez l'âge du joueur : ")
        return {'last_name': last_name, 'first_name': first_name, 'date_of_birth': date_of_birth, 'sexe': sexe,
                'classement': classement, 'age': age}

    def select_player(self, players):
        for key, player in enumerate(players):
            print(f'{key}: {player}')
        choice = self.validate.input_in_array_of_int("Numéro de joueur : ", range(0, len(players)))
        return players[choice]

    def update_ranking(self):
        return self.validate.check_int("Nouveau classement : ")
