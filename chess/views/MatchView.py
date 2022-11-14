from models.MatchModel import MatchModel
from tinydb import Query

class MatchView:
    def __init__(self) -> None:
        pass

    #Show match for a round
    def show_match(tournament_id, round_name) -> None:
        result = MatchModel.show_match(tournament_id, round_name)
        print('\n\n    Match for tournament ', tournament_id, round_name)

        for p in result:
            print('')
            print(f'        {p["player_1"]["lastname"]} - {p["player_1"]["ranking"]}  versus {p["player_2"]["lastname"]} - {p["player_2"]["ranking"]}')
        print('\n Enter the match results: \n')    
        
        #results record
        for p in result:
            print(f'        {p["player_1"]["lastname"]} versus {p["player_2"]["lastname"]}')
            res_player1 = input(f'\n Result for {p["player_1"]["lastname"]}: ')
            res_player2 = input(f' Result for {p["player_2"]["lastname"]}: ')
            print('')
            #update match table with result
            MatchModel.update_table(res_player1, res_player2,tournament_id, round_name, p["player_1"], p["player_2"])
