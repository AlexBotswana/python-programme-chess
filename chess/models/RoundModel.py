from models.TournamentModel import round_table


class RoundModel:
    def __init__(self, name,
        begin_time,
        end_time,
        finished_match_list,
        round_list,
        tournament_id
        ):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.finished_match_list = finished_match_list
        self.round_list = round_list
        self.tournament_id = tournament_id

#add a round
    def add_one(self):
        new_round = {"name": self.name, "begin_time": self.begin_time, "end_time": self.end_time, "finished_match_list": self.finished_match_list, "round_list": self.round_list, "tournament_id": self.tournament_id}
        round_table.insert(new_round)