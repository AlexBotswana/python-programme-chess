from controllers.TournamentController import TournamentController
from models.PlayerModel import PlayerModel
from models.TournamentModel import TournamentModel
from controllers.PlayerController import PlayerController

class MenuView:
    def __init__(self) -> None:
        pass

    def menu() -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
        #Menu selection
            menu_choice = int(input("\n\n---------------- Chess Tournament ----------------\n 0 - Exit\n 1 - Tournaments menu \n 2 - Players menu\n Choice : "))

            if int(menu_choice) == 1:
                menu_choice_t = 1
                #Menu selection
                while int(menu_choice_t) != 0:
                    menu_choice_t = int(input("\n\n---------------- Tournaments menu ----------------\n 0 - Exit\n 1 - Start a new tournament\n 2 - Continue a tournament\n 3 - Consult a tournament\n 4 - Generate report\n Choice : "))
                    
                    if int(menu_choice_t) == 1:
                        MenuView.add_tournament()
                        TournamentController
                    
                    elif int(menu_choice_t) == 2:
                        continue_choice = int(input("\nEnter the tournament's ID: "))
                        

                    elif int(menu_choice_t) == 3:
                        consult_choice = int(input("\nEnter the tournament's ID: "))
                        TournamentController.search_one(consult_choice)

                    elif int(menu_choice_t) == 4:
                        TournamentController.show_all()

            elif int(menu_choice) == 2:
                menu_choice_p = 1
                while int(menu_choice_p) != 0:
                #Menu selection
                    menu_choice_p = int(input("\n\n---------------- Players menu ----------------\n 0 - Exit\n 1 - Search a player\n 2 - Search all players\n 3 - Add new player\n Choice : "))

                    if int(menu_choice_p) == 1:
                        name_choice_p = input("Enter player lastname: ")
                        #search a player
                        PlayerController.search_one(name_choice_p)

                    elif int(menu_choice_p) == 2:
                        PlayerController.show_all()
                        
                    elif int(menu_choice_p) == 3:
                        MenuView.add_player()

    def add_player() -> None:
        id = 0
        firstname = input("Firstname :  ")
        lastname = input("Lastname :  ")
        birthdate = input("Birthdate (dd/mm/yyyy):  ")
        gender = input("Gender (M or F) :  ")
        ranking = int(input("Ranking :  "))
        tournament_ids = 0
        new_player = PlayerModel(id, firstname, lastname, birthdate, gender, ranking, tournament_ids)
        PlayerController.add_one(new_player)

    def add_tournament() -> None:
        tournament_ids = int(input("IDS: "))
        name = input("Tournament Name: ")
        date = input("Tournament date (dd/mm/yyyy): ")
        number_round = input("Number of round: ")
        location = input("Location: ")
        round = 0
        player_ids = '1;2;3;4'
        time_control = input("Time control (Bullets, Blitz or Rapid): ")
        description = input("Enter a tournament description: ")
        new_tournament = TournamentModel(tournament_ids, name, date, number_round, location, round, player_ids, time_control, description)
        TournamentController.add_one(new_tournament)
        TournamentController.generate_round(tournament_ids)