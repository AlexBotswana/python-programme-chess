from models.TournamentModel import TournamentModel
from views.TournamentView import TournamentView


class TournamentController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def search_one(id: int) -> None:
        tournament = TournamentModel.get_one(id)
        TournamentView.show_tournament(tournament)

    @staticmethod
    def show_all() -> None:
        tournament = TournamentModel.get_all()
        TournamentView.show_tournament(tournament)

    @staticmethod
    def add_one(infos_tournament: TournamentModel) -> None:
        TournamentModel.add_one(infos_tournament)

    def add_tournament() -> None:
        # automatic +1 regarding total number of tournaments
        tournament_id = TournamentModel.add_id()
        name = input("Tournament Name: ")
        date = input("Tournament date (dd/mm/yyyy): ")
        location = input("Location: ")
        number_round = input("Number of round: ")
        player_ids = input("Enter players' ID (with ; as separator): ")
        time_control = input("Time control (1 - Bullets, 2 - Blitz, 3 - Rapid): ")
        if time_control == '1':
            time_control = 'Bullets'
        elif time_control == '2':
            time_control = 'Blitz'
        elif time_control == '3':
            time_control = 'Rapid'
        description = input("Enter a tournament description: ")
        new_tournament = TournamentModel(tournament_id,
                                         name,
                                         date,
                                         location,
                                         number_round,
                                         player_ids,
                                         time_control,
                                         description
                                         )
        TournamentController.add_one(new_tournament)