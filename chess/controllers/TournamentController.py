from models.TournamentModel import TournamentModel
from views.TournamentView import TournamentView


class TournamentController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def search_one(id: int) -> None:
        tournament = TournamentModel.get_one(id)
        TournamentView.get_tournament(tournament)

    @staticmethod
    def show_all() -> None:
        tournament = TournamentModel.get_all()
        TournamentView.show_tournament(tournament)

    @staticmethod
    def add_one(infos_tournament: TournamentModel) -> None:
        TournamentModel.add_one(infos_tournament)

    @staticmethod
    def add_players_t() -> None:
        pass
