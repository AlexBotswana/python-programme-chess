from models.MatchModel import MatchModel
from models.PlayerModel import PlayerModel
from models.TournamentModel import TournamentModel
from views.MatchView import MatchView

class MatchController:
    def __init__(self) -> None:
        pass

    #Round1 match
    @staticmethod
    def round1_match(tournament_id) -> None:
        #players list order by reverse ranking
        list_players = PlayerModel.sort_ranking()
        
        
        #match depending of ranking and numbers of players (1st player against the 1st player of the 2nd half part of the list)
        nb_players = len(list_players)
        half_position = int(nb_players/2)
        
        #match creation
        #to do list_players[0],
        count = 0
        match_list = []
        while count != half_position:
            player1 = list_players[count]
            player2 = list_players[half_position + count]
            match_round1 = MatchModel(tournament_id, 'Round1', player1, player2, 0, 0)
            MatchModel.add_match(match_round1)
            match = (player1, player2)
            match_list.append(match)
            count = count + 1

        return match_list
    
    #Show match list for a round
    @staticmethod
    def show_match(tournament_id, round_name) -> None:
        MatchView.show_match(tournament_id, round_name)

    
        
        