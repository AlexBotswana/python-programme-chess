from models.MatchModel import MatchModel
from models.PlayerModel import PlayerModel
from models.TournamentModel import TournamentModel

class MatchController:
    def __init__(self) -> None:
        pass

    #Round1 match
    @staticmethod
    def round1_match() -> None:
        list_players = PlayerModel.sort_ranking()
        print(list_players)
        
