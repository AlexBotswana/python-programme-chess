from models.PlayerModel import PlayerModel
from views.PlayerView import PlayerView

class PlayerController:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def search_one(lastname:str) -> None:
        player = PlayerModel.get_one(lastname)
        PlayerView.get_player(player)

    @staticmethod
    def show_all() -> None:
        players = PlayerModel.get_all()
        PlayerView.show_players(players)

    @staticmethod
    def add_one(infos_player) -> None:
        PlayerModel.add_one(infos_player)

    @staticmethod
    def add_id_player() -> None:
        id = PlayerModel.add_id()
        return id
        