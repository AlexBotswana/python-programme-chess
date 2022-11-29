class TournamentView:
    def __init__(self) -> None:
        pass

    @staticmethod
    def show_tournament(tournament_info) -> None:
        for p in tournament_info:
            print('')
            print(f'tournament_id               {p["tournament_id"]}')
            print(f'name                        {p["name"]}')
            print(f'date                        {p["date"]}')
            print(f'location                    {p["location"]}')
            print(f'count_round                 {p["count_round"]}')
            print(f'players_ids                 {p["players_ids"]}')
            print(f'time_control                {p["time_control"]}')
            print(f'description                 {p["description"]}')
