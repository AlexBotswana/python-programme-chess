from tinydb import TinyDB
from tinydb import Query


class TournamentModel:
    def __init__(self,
                 tournament_id,
                 name,
                 date,
                 location,
                 count_round,
                 players_ids,
                 # For time_control: bullet : 180s; blitz : 300s; rapid : 600s
                 time_control,
                 description
                 ):
        self.tournament_id = tournament_id
        self.round_name = name
        self.date = date
        self.location = location
        self.count_round = count_round
        self.players_ids = players_ids
        self.time_control = time_control
        self.description = description

    @staticmethod
    def get_one(id: int) -> None:
        one_tournament = Query()
        result_one = Data.search(one_tournament.tournament_id == id)
        return result_one

    @staticmethod
    def get_all() -> None:
        result_all = Data.all()
        return result_all

    @staticmethod
    def add_id() -> None:
        id_tournament = int(Data.count(id)) + 1
        return id_tournament

    # add a tournament
    def add_one(self) -> None:
        new_tournament = {"tournament_id": self.tournament_id,
                          "name": self.round_name,
                          "date": self.date,
                          "location": self.location,
                          "count_round": self.count_round,
                          "players_ids": self.players_ids,
                          "time_control": self.time_control,
                          "description": self.description
                          }
        Data.insert(new_tournament)

    # Data set for a tournement
    @staticmethod
    def init_db() -> None:
        init_tournament = [
                {"tournament_id": 1,
                 "name": "Tournois du Botswana",
                 "date": "13/10/2022",
                 "location": "Gaborone",
                 "count_round": 2,
                 "players_ids": '1;2;3;4;5;6;7;8',
                 "time_control": 'Bullets',
                 "description": 'Tournoi suisse pour les eleves de Westwood IS'
                 },
                            ]
        Data.insert_multiple(init_tournament)

        init_player = [
                {"id": 1,
                 "firstname": "Caroline",
                 "lastname": "TATA",
                 "birthdate": "01/12/1970",
                 "gender": "M",
                 "ranking": 1300,
                 "tournament_id": 1
                 },
                {"id": 2,
                 "firstname": "Xavier",
                 "lastname": "TITI",
                 "birthdate": "02/11/1975",
                 "gender": "F",
                 "ranking": 1250,
                 "tournament_id": 1
                 },
                {"id": 3,
                 "firstname": "Victor",
                 "lastname": "TOTO",
                 "birthdate": "03/10/1980",
                 "gender": "M",
                 "ranking": 1200,
                 "tournament_id": 1
                 },
                {"id": 4,
                 "firstname": "Gaspart",
                 "lastname": "TUTU",
                 "birthdate": "04/09/1985",
                 "gender": "F",
                 "ranking": 1350,
                 "tournament_id": 1
                 },
                {"id": 5,
                 "firstname": "Caroline",
                 "lastname": "ONE",
                 "birthdate": "01/12/1970",
                 "gender": "M",
                 "ranking": 1303,
                 "tournament_id": 1
                 },
                {"id": 6,
                 "firstname": "Xavier",
                 "lastname": "TWO",
                 "birthdate": "02/11/1975",
                 "gender": "F",
                 "ranking": 1252,
                 "tournament_id": 1
                 },
                {"id": 7,
                 "firstname": "Victor",
                 "lastname": "THREE",
                 "birthdate": "03/10/1980",
                 "gender": "M",
                 "ranking": 1201,
                 "tournament_id": 1
                 },
                        ]
        player_table.insert_multiple(init_player)


# création db fichier .json
Data = TinyDB('db/Data.json')
player_table = Data.table('player')
round_table = Data.table('round')
match_table = Data.table('match')
