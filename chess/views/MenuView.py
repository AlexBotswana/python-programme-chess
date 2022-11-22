from controllers.TournamentController import TournamentController
from models.PlayerModel import PlayerModel
from models.TournamentModel import TournamentModel
from controllers.PlayerController import PlayerController
from controllers.RoundController import RoundController
from controllers.MatchController import MatchController


class MenuView:
    def __init__(self) -> None:
        pass

    def menu() -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
            # Menu selection
            print('\n\n---------------- Chess Tournament ----------------\n')
            print(' 0 - Exit')
            print(' 1 - Tournaments menu')
            print(' 2 - Players menu')
            menu_choice = int(input(' Choice : '))

            if int(menu_choice) == 1:
                menu_choice_t = 1
                # Menu selection
                while int(menu_choice_t) != 0:
                    print('\n\n------------ Tournaments menu ------------\n')
                    print('     0 - Exit')
                    print('     1 - Create a new tournament')
                    print('     2 - Start/update a tournament')
                    print('     3 - Consult a tournament')
                    print('     4 - Generate report')
                    menu_choice_t = int(input('     Choice : '))

                    if int(menu_choice_t) == 1:
                        MenuView.add_tournament()
                    elif int(menu_choice_t) == 2:
                        # generate round
                        tournament_id = int(input("\nEnter tournament's ID: "))
                        # test if  round already exist
                        test = RoundController.round_exist(tournament_id,
                                                           'Round1'
                                                           )
                        if test is False:
                            RoundController.generate_round(tournament_id,
                                                           'Round1'
                                                           )
                        MatchController.show_match(tournament_id,
                                                   'Round1'
                                                   )
                        print('\n\n---------- Round1 Menu -----------\n')
                        print('     0 - Exit')
                        print('     1 - Start time')
                        print('     2 - End time')
                        print('     3 - Register the results')
                        menu_choice_m = int(input(' Choice : '))

                        if int(menu_choice_m) == 1:
                            pass
                        elif int(menu_choice_m) == 2:
                            pass
                        elif int(menu_choice_m) == 3:
                            # register the results in db
                            MatchController.reg_results(tournament_id,
                                                        'Round1'
                                                        )
                            # create round2
                            # test if  round already exist
                            test = RoundController.round_exist(tournament_id,
                                                               'Round2'
                                                               )
                            if test is False:
                                RoundController.generate_round(tournament_id,
                                                               'Round2'
                                                               )
                            MatchController.show_match(tournament_id,
                                                       'Round2'
                                                       )
                            print('\n\n----- Round2 Menu ------\n')
                            print('     0 - Exit')
                            print('     1 - Start time')
                            print('     2 - End time')
                            print('     3 - Register the results')
                            menu_choice_m = int(input(' Choice : '))
                            if int(menu_choice_m) == 1:
                                pass
                            elif int(menu_choice_m) == 2:
                                pass
                            elif int(menu_choice_m) == 3:
                                # register the results in db
                                MatchController.reg_results(tournament_id,
                                                            'Round2'
                                                            )
                    elif int(menu_choice_t) == 3:
                        consult_choice = int(input("\nEnter tournament ID: "))
                        TournamentController.search_one(consult_choice)

                    elif int(menu_choice_t) == 4:
                        consult_choice = int(input("\nEnter tournament ID: "))
                        TournamentController.search_one(consult_choice)

                    elif int(menu_choice_t) == 5:
                        TournamentController.show_all()

            elif int(menu_choice) == 2:
                menu_choice_p = 1
                while int(menu_choice_p) != 0:
                    # Menu selection
                    print('\n\n---------------- Players menu ----------------')
                    print(' 0 - Exit')
                    print(' 1 - Search a player')
                    print(' 2 - Search all players')
                    print(' 3 - Add new player')
                    menu_choice_p = int(input(" Choice : "))

                    if int(menu_choice_p) == 1:
                        name_choice_p = input("Enter player lastname: ")
                        # search a player
                        PlayerController.search_one(name_choice_p)

                    elif int(menu_choice_p) == 2:
                        PlayerController.show_all()

                    elif int(menu_choice_p) == 3:
                        MenuView.add_player()

    def add_player() -> None:
        id = PlayerController.add_id_player()
        firstname = input("Firstname :  ")
        lastname = input("Lastname :  ")
        birthdate = input("Birthdate (dd/mm/yyyy):  ")
        gender = input("Gender (M or F) :  ")
        ranking = int(input("Ranking :  "))
        tournament_ids = 0
        new_player = PlayerModel(id,
                                 firstname,
                                 lastname,
                                 birthdate,
                                 gender,
                                 ranking,
                                 tournament_ids
                                 )
        PlayerController.add_one(new_player)

    def add_tournament() -> None:
        tournament_ids = int(input("IDS: "))
        name = input("Tournament Name: ")
        date = input("Tournament date (dd/mm/yyyy): ")
        number_round = input("Number of round: ")
        location = input("Location: ")
        round = 0
        player_ids = input("Enter players' ID (with ; as separator): ")
        time_control = input("Time control (Bullets, Blitz or Rapid): ")
        description = input("Enter a tournament description: ")
        new_tournament = TournamentModel(tournament_ids,
                                         name,
                                         date,
                                         number_round,
                                         location,
                                         round,
                                         player_ids,
                                         time_control,
                                         description
                                         )
        TournamentController.add_one(new_tournament)
