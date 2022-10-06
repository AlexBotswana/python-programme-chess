from models.PlayerModel import PlayerModel
from controllers.PlayerController import PlayerController

class MenuView:
    def __init__(self) -> None:
        pass

    def Menu() -> None:
        menu_choice = 1
        while int(menu_choice) != 0:
        #Menu selection
            menu_choice = int(input("Player menu\n 0 - Exit\n 1 - Search a player\n 2 - Search all players\n 3 - Add new player\n Choice : "))

            if int(menu_choice) == 1:
                name_choice = input("Enter player lastname: ")
                #search a player
                PlayerController.search_one(name_choice)

            elif int(menu_choice) == 2:
                PlayerController.show_all()
                
            elif int(menu_choice) == 3:
                new_player_id = 0
                new_player_firstname = input("Firstname :  ")
                new_player_lastname = input("Lastname :  ")
                new_player_birthdate = input("Birthdate (dd/mm/yyyy):  ")
                new_player_gender = input("Gender (M or F) :  ")
                new_player_ranking = int(input("Ranking :  "))
                new_player_tournament_ids = 0
                new_player = PlayerModel(new_player_id, new_player_firstname, new_player_lastname, new_player_birthdate, new_player_gender, new_player_ranking, new_player_tournament_ids)
                PlayerController.add_one(new_player)
