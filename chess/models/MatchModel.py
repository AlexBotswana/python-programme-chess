from models.TournamentModel import match_table, player_table
from operator import itemgetter

class MatchModel:
    def __init__(self, tournament_id,
        round_name,
        player_1,
        player_2, 
        score_player_1, 
        score_player_2
        ):
        self.tournament_id = tournament_id
        self.round_name = round_name
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1#voir arjancode énumération
        self.score_player_2 = score_player_2

    #round1
    @staticmethod
    def swiss_method(players:list) -> list[tuple]:
        pass     
            