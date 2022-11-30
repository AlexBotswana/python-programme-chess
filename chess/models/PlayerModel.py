from tinydb import Query
from models.TournamentModel import player_table
import operator


class PlayerModel:
    def __init__(self, id,
                 firstname,
                 lastname,
                 birthdate,
                 gender,
                 ranking,
                 tournament_id
                 ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.tournament_id = tournament_id

    def add_one(self) -> None:
        new_player = {"id": self.id, "firstname": self.firstname,
                      "lastname": self.lastname, "birthdate": self.birthdate,
                      "gender": self.gender, "ranking": self.ranking,
                      "tournament_id": self.tournament_id
                      }
        player_table.insert(new_player)

    @staticmethod
    def get_one(player_id: int) -> None:
        oneplayer = Query()
        result_one = player_table.search(oneplayer.id == player_id)
        return result_one

    @staticmethod
    def add_id() -> None:
        id_player = int(player_table.count(id)) + 1
        return id_player

    # players list order by reverse ranking
    @staticmethod
    def sort_ranking() -> list:
        order_ranking = []
        order_ranking = player_table.all()
        order_ranking.sort(reverse=True, key=operator.itemgetter("ranking"))
        return order_ranking

    # update ranking in player table
    @staticmethod
    def update_ranking(player_id: int, ranking: int) -> None:
        result = Query()
        player_table.update(
                        {'ranking': ranking},
                        (result.id == player_id)
                            )
