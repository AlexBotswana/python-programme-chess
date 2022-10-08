from views.MenuView import MenuView
from models.PlayerModel import PlayerModel

data_set = 0
data_set = int(input('Do you want to upload players data set?\n 1 - Yes\n 2 - No\n Enter your choice :'))
if data_set == 1:
    PlayerModel.init_db()

MenuView.Menu()







