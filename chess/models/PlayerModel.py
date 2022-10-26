from tinydb import Query
from models.TournamentModel import player_table


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
        player_table.insert(new_player)
    
    @staticmethod
    def get_one(player_lastname):
        oneplayer = Query()
        result_one = player_table.search(oneplayer.lastname == player_lastname)
        return result_one

    @staticmethod
    def get_all():
        result_all = player_table.all()
        return result_all

    



