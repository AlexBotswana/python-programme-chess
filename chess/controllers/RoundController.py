from models.RoundModel import RoundModel
from controllers.MatchController import MatchController

class RoundController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_round1(tournament_id) -> None:
        #round1 suisse sélection
        round_id = RoundModel.add_id()
        name = 'Round1'
        begin_time = 0
        end_time = 0
        match_list = MatchController.round1_match(tournament_id)
        new_round = RoundModel(round_id, name, begin_time , end_time, match_list, tournament_id)
        RoundModel.add_one(new_round)
        
    @staticmethod
    def round_existing(tournament_id:int, round_name:str) -> bool:
        return RoundModel.round_existing(tournament_id, round_name)

    @staticmethod
    def generate_round(tournament_id, round_name) -> None:
        round_id = RoundModel.add_id()
        begin_time = 0
        end_time = 0
        #round1 suisse sélection
        if round_name == 'Round1':
            match_list = MatchController.round1_match(tournament_id)
        else:
            match_list = MatchController.round_match(tournament_id, round_name)
        new_round = RoundModel(round_id, round_name, begin_time , end_time, match_list, tournament_id)
        RoundModel.add_one(new_round)