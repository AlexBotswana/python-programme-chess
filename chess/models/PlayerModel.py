from tinydb import TinyDB
from tinydb import Query


class PlayerModel:
    def __init__(self, id,
        firstname,
        lastname,
        birthdate,
        gender,
        ranking,
        tournament_ids
        ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.tournament_ids = tournament_ids
    
    def add_one(self):
        new_player = {"id": self.id, "firstname": self.firstname, "lastname": self.lastname, "birthdate": self.birthdate, "gender": self.gender, "ranking": self.ranking, "tournament_ids": self.tournament_ids}
        PlayerDb.insert(new_player)

    #data set
    def add_data_set(self):
        PlayerDb.insert_multiple(self)
       
    @staticmethod
    def get_one(player_lastname):
        oneplayer = Query()
        result_one = PlayerDb.search(oneplayer.lastname == player_lastname)
        return result_one

    @staticmethod
    def get_all():
        result_all = PlayerDb.all()
        return result_all

    #Data set for a tournement
    @staticmethod
    def init_db():
        init_player = [
                {"id": 1,"firstname": "Caroline", "lastname": "TATA", "birthdate": "01/12/1970", "gender": "M", "ranking": 1200, "tournament_ids": 10},
                {"id": 2,"firstname": "Xavier", "lastname": "TITI", "birthdate": "02/11/1975", "gender": "F", "ranking": 1210, "tournament_ids": 10},
                {"id": 3,"firstname": "Victor", "lastname": "TOTO", "birthdate": "03/10/1980", "gender": "M", "ranking": 1220, "tournament_ids": 10},
                {"id": 4,"firstname": "Gaspart", "lastname": "TUTU", "birthdate": "04/09/1985", "gender": "F", "ranking": 1230, "tournament_ids": 10},
                {"id": 5,"firstname": "Ditso", "lastname": "TATA", "birthdate": "01/12/1970", "gender": "M", "ranking": 1240, "tournament_ids": 10},
                {"id": 6,"firstname": "Tadiwa", "lastname": "TITI", "birthdate": "02/11/1975", "gender": "F", "ranking": 1250, "tournament_ids": 10},
                {"id": 7,"firstname": "Gorata", "lastname": "TOTO", "birthdate": "03/10/1980", "gender": "F", "ranking": 1260, "tournament_ids": 10},
                {"id": 8,"firstname": "Zenith", "lastname": "TUTU", "birthdate": "04/09/1985", "gender": "F", "ranking": 1270, "tournament_ids": 10}
            ]
        PlayerModel.add_data_set(init_player)

#création db fichier .json
PlayerDb = TinyDB('db/PlayerDb.json')



