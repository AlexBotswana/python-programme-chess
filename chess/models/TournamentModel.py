from tinydb import TinyDB
from tinydb import Query


class TournamentModel:
    def __init__(self, tournament_ids,
        name,
        date,
        location,
        count_round,
        players_ids,
        round,
        #For time_control: bullet : 180s; blitz : 300s; rapid : 600s
        time_control,
        description
        ):
        self.tournament_ids = tournament_ids
        self.name = name
        self.date = date
        self.count_round = count_round
        self.location = location
        self.players_ids = players_ids
        self.round = round
        self.time_control = time_control
        self.description = description
    
    @staticmethod
    def get_one(ids):
        one_tournament = Query()
        result_one = TournamentDb.search(one_tournament.tournament_ids == ids)
        return result_one

    @staticmethod
    def get_all():
        result_all = TournamentDb.all()
        return result_all

    #add a tournament
    def add_one(self):
        new_tournament = {"tournament_ids": self.tournament_ids, "name": self.name, "date": self.date, "count_round": self.count_round, "location": self.location, "players_ids": self.players_ids, "round": self.round, "time_control": self.time_control, "description": self.description}
        TournamentDb.insert(new_tournament)

    #data set
    def add_data_set(self):
        TournamentDb.insert_multiple(self)

    #Data set for a tournement
    @staticmethod
    def init_db():
        init_tournament = [
                {"tournament_ids": 1,"name": "Tournois du Botswana", "date": "13/10/2022", "count_round": 4, "location": "Gaborone", "round": 1, "players_ids": '1-5;2-6;3-7;4-8', "time_control":'bullets', "description": 'Tournoi suisse pour les eleves de Westwood IS'},
                {"tournament_ids": 1,"name": "Tournois du Botswana", "date": "13/10/2022", "count_round": 4, "location": "Gaborone", "round": 2, "players_ids": '1-4;2-5;3-6;7-8', "time_control":'bullets', "description": 'Tournoi suisse pour les eleves de Westwood IS'},
                {"tournament_ids": 1,"name": "Tournois du Botswana", "date": "13/10/2022", "count_round": 4, "location": "Gaborone", "round": 3, "players_ids": '1-3;2-4;5-7;6-8', "time_control":'bullets', "description": 'Tournoi suisse pour les eleves de Westwood IS'},
                {"tournament_ids": 1,"name": "Tournois du Botswana", "date": "13/10/2022", "count_round": 4, "location": "Gaborone", "round": 4, "players_ids": '1-6;3-2;4-3;5-8', "time_control":'bullets', "description": 'Tournoi suisse pour les eleves de Westwood IS'},
            ]
        TournamentModel.add_data_set(init_tournament)

#création db fichier .json
TournamentDb = TinyDB('db/TournamentDb.json')