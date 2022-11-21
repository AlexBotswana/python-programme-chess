from models.TournamentModel import round_table
from tinydb import Query


class RoundModel:
    def __init__(self, id,
        round_name,
        begin_time,
        end_time,
        match_list,
        tournament_id
        ):
        self.round_name = round_name
        self.begin_time = begin_time
        self.end_time = end_time
        self.match_list = match_list
        self.tournament_id = tournament_id

    #add a round
    def add_one(self):
        new_round = {"round_name": self.round_name, "begin_time": self.begin_time, "end_time": self.end_time, "match_list": self.match_list, "tournament_id": self.tournament_id}
        round_table.insert(new_round)

    #round ID
    def add_id():
        id_round = int(round_table.count(id)) + 1
        return id_round
    
    #existing round1
    def round_existing(tournament_id:int, round_name:str) -> bool:
        test = round_table.all()
        exist = False
        if test != []:
            existing = Query()
            test = round_table.get((existing.tournament_id == tournament_id) & (existing.round_name == round_name))
            if test != None:
                exist = True
        return exist

    