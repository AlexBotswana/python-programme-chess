from models.TournamentModel import match_table, player_table
from operator import itemgetter
from tinydb import Query

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
    def add_match(self) -> None:
        new_match = {"tournament_id": self.tournament_id, "round_name": self.round_name, "player_1": self.player_1, "player_2": self.player_2, "score_player_1": self.score_player_1, "score_player_2": self.score_player_2}
        match_table.insert(new_match)
    
    #Show match for a round
    def show_match(tournament_id, round_name) -> None:
        match = Query()
        result = match_table.search((match.tournament_id == tournament_id) & (match.round_name == round_name))

        return result
    
    #update match table
    @staticmethod
    def update_table(result1, result2, tournament_id, round_name, player_1, player_2) -> None:
        """result = Query()
        print(({'score_player_1': result1},{'score_player_2': result2}),((result.tournament_id == tournament_id)&(result.round_name == round_name)&(result.player_1 == player_1)&(result.player_2 == player_2)))
        match_table.update(({'score_player_1': result1},{'score_player_2': result2}),((result.tournament_id == tournament_id)&(result.round_name == round_name)&(result.player_1 == player_1)&(result.player_2 == player_2)))  
        """
        pass

    @staticmethod
    def swiss_method(players:list) -> list[tuple]:
        print(players)    