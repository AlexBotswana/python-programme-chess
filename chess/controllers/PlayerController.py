from models.PlayerModel import PlayerModel
from views.PlayerView import PlayerView


class PlayerController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def search_one(player_id: int) -> None:
        player = PlayerModel.get_one(player_id)
        PlayerView.show_players(player)

    @staticmethod
    def show_all() -> None:
        # order by ranking
        players = PlayerModel.sort_ranking()
        PlayerView.show_players(players)

    @staticmethod
    def add_one(infos_player) -> None:
        PlayerModel.add_one(infos_player)

    @staticmethod
    def add_id_player() -> None:
        id = PlayerModel.add_id()
        return id

    @staticmethod
    def add_player() -> None:
        id = PlayerController.add_id_player()
        firstname = input("Firstname :  ")
        lastname = input("Lastname :  ")
        birthdate = input("Birthdate (dd/mm/yyyy):  ")
        gender = input("Gender (M or F) :  ")
        ranking = int(input("Ranking :  "))
        tournament_id = int(input("Tournament ID : "))
        new_player = PlayerModel(id,
                                 firstname,
                                 lastname,
                                 birthdate,
                                 gender,
                                 ranking,
                                 tournament_id
                                 )
        PlayerController.add_one(new_player)

    @staticmethod
    def update_ranking(player_id: int) -> None:
        PlayerController.search_one(player_id)
        new_ranking = int(input('\n\nEnter new ranking : '))
        PlayerModel.update_ranking(player_id,new_ranking)
        print('\n\n')
        PlayerController.search_one(player_id)

