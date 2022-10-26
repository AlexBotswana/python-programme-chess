from time import time
from models.RoundModel import RoundModel
from models.TournamentModel import TournamentModel
from views.TournamentView import TournamentView

class TournamentController:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def search_one(ids:int) -> None:
        tournament = TournamentModel.get_one(ids)
        TournamentView.get_tournament(tournament)

    @staticmethod
    def show_all() -> None:
        tournament = TournamentModel.get_all()
        TournamentView.show_tournament(tournament)

    @staticmethod
    def add_one(infos_tournament) -> None:
        TournamentModel.add_one(infos_tournament)
    
    @staticmethod
    def generate_round(tournament_id) -> None:
        #round1 suisse sélection
        name = 'Round1'
        begin_time = time()
        end_time = time()
        match_list = []
        round_list = []
        new_round = RoundModel(name, begin_time ,end_time ,match_list, round_list, tournament_id)
        RoundModel.add_one(new_round)

    @staticmethod
    def add_players_t() -> None:
        pass

