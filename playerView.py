class PlayerView:
    def prompt_for_player(self):
        last_name = input("tapez le nom du joueur : ")
        first_name = input("tapez le prénom du joueur : ")
        date_of_birth = input("tapez la date de naissance du joueur : ")
        sexe = input("tapez le sexe du joueur : ")
        classement = input("tapez le classement du joueur : ")
        age = input("tapez l'âge' du joueur : ")
        return {'last_name': last_name, 'first_name': first_name, 'date_of_birth': date_of_birth, 'sexe': sexe, 'classement': classement, 'age': age}

#boucle for, dans la liste des joueurs pour chaque on print, renvoie de la liste des joueurs sélectionnés
    #key et enumerate pour avoir l'élément selon sa position dans la iste, f'' permet de mettre des variables en texte, choisi juste un joueur
# TODO pourquoi key, enumerate, pourquoi f? différence selcted_players tournamentview?
    def select_player(self, players):
        for key, player in enumerate(players):
            print(f'{key}: {player}')
        choice = int(input("Numéro de joueur : "))
        return players[choice]

    def update_ranking(self):
        return input("Nouveau classement : ")
