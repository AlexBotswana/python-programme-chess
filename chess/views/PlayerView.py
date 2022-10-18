
class PlayerView:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_player(player_info) -> None:
        for p in player_info:
            print('')
            print(f'Id              {p["id"]}')
            print(f'Firstname       {p["firstname"]}')
            print(f'Lastname        {p["lastname"]}')
            print(f'Birthdate       {p["birthdate"]}')
            print(f'Gender          {p["gender"]}')
            print(f'Ranking         {p["ranking"]}')
            

    @staticmethod
    def show_players(players_info) -> None:
        for p in players_info:
            print('')
            print(f'Id              {p["id"]}')
            print(f'Firstname       {p["firstname"]}')
            print(f'Lastname        {p["lastname"]}')
            print(f'Birthdate       {p["birthdate"]}')
            print(f'Gender          {p["gender"]}')
            print(f'Ranking         {p["ranking"]}')