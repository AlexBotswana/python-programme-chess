from models.TournamentModel import round_table


class RoundModel:
    def __init__(self, id,
        step,
        begin_time,
        end_time,
        match_list,
        tournament_id
        ):
        self.name = step
        self.begin_time = begin_time
        self.end_time = end_time
        self.match_list = match_list
        self.tournament_id = tournament_id

#add a round
    def add_one(self):
        new_round = {"step": self.name, "begin_time": self.begin_time, "end_time": self.end_time, "match_list": self.match_list, "tournament_id": self.tournament_id}
        round_table.insert(new_round)

    #round ID
    def add_id():
        id_round = int(round_table.count(id)) + 1
        return id_round