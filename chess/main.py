from models.TournamentModel import TournamentModel
from views.MenuView import MenuView
from models.PlayerModel import PlayerModel

data_set = 0
data_set = int(input('\n 1 - Upload players data set?\n 2 - Upload tournament data set\n 3 - Do nothing\n Your choice : '))
if data_set == 1:
    PlayerModel.init_db()
elif data_set == 2:
    TournamentModel.init_db()

MenuView.menu()







