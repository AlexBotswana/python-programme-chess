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
        self.round_name = name
        self.date = date
        self.count_round = count_round
        self.location = location
        self.players_ids = players_ids
        self.round = round
        self.time_control = time_control
        self.description = description
    
    @staticmethod
    def get_one(id:int) -> None:
        one_tournament = Query()
        result_one = Data.search(one_tournament.tournament_ids == id)
        return result_one

    @staticmethod
    def get_all() -> None:
        result_all = Data.all()
        return result_all

    #add a tournament
    def add_one(self) -> None:
        new_tournament = {"tournament_ids": self.tournament_ids, "name": self.round_name, "date": self.date, "count_round": self.count_round, "location": self.location, "players_ids": self.players_ids, "round": self.round, "time_control": self.time_control, "description": self.description}
        Data.insert(new_tournament)

    #Data set for a tournement
    @staticmethod
    def init_db() -> None:
        init_tournament = [
                {"tournament_ids": 1,"name": "Tournois du Botswana", "date": "13/10/2022", "count_round": 3, "location": "Gaborone", "round": 1, "players_ids": '1;2;3;4', "time_control":'bullets', "description": 'Tournoi suisse pour les eleves de Westwood IS'},
                {"tournament_ids": 2,"name": "Tournois de Toulouse", "date": "14/10/2022", "count_round": 3, "location": "Toulouse", "round": 1, "players_ids": '1;2;3;4', "time_control":'rapid', "description": 'Tournoi suisse'},
                ]
        Data.insert_multiple(init_tournament)

        init_player = [
                {"id": 1,"firstname": "Caroline", "lastname": "TATA", "birthdate": "01/12/1970", "gender": "M", "ranking": 1300, "tournament_ids": 1},
                {"id": 2,"firstname": "Xavier", "lastname": "TITI", "birthdate": "02/11/1975", "gender": "F", "ranking": 1250, "tournament_ids": 1},
                {"id": 3,"firstname": "Victor", "lastname": "TOTO", "birthdate": "03/10/1980", "gender": "M", "ranking": 1200, "tournament_ids": 1},
                {"id": 4,"firstname": "Gaspart", "lastname": "TUTU", "birthdate": "04/09/1985", "gender": "F", "ranking": 1350, "tournament_ids": 1},
                ]
        player_table.insert_multiple(init_player)

        """init_round = [
                {"name": 'Round1', "begin_time": 'begin_time', "end_time": 'end_time', "match_list": '1;2;3', "tournament_id": 1},
                {"name": 'Round2', "begin_time": 'begin_time', "end_time": 'end_time', "match_list": '1;2;3', "tournament_id": 1},
                {"name": 'Round3', "begin_time": 'begin_time', "end_time": 'end_time', "match_list": '1;2;3', "tournament_id": 1},
                {"name": 'Round4', "begin_time": 'begin_time', "end_time": 'end_time', "match_list": '1;2;3', "tournament_id": 1},
                ]
        round_table.insert_multiple(init_round)"""

#création db fichier .json
Data = TinyDB('db/Data.json')
player_table = Data.table('player')
round_table = Data.table('round')
match_table = Data.table('match')