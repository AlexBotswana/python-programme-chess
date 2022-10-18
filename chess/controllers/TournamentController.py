from models.TournamentModel import TournamentModel
from views.TournamentView import TournamentView

class TournamentController:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def search_one(ids) -> None:
        tournament = TournamentModel.get_one(ids)
        TournamentView.get_tournament(tournament)

    @staticmethod
    def show_all() -> None:
        tournament = TournamentModel.get_all()
        TournamentView.show_tournament(tournament)

    @staticmethod
    def add_one(infos_tournament) -> None:
        TournamentModel.add_one(infos_tournament)