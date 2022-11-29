from models.TournamentModel import TournamentModel
from views.MenuView import MenuView


# try:
data_set = 0
print('\n1 - Upload data set?')
print('2 - Do nothing')
data_set = int(input('\n Your choice: '))
if data_set == 1:
    TournamentModel.init_db()
MenuView.menu()
# except Exception:
    # print('WRONG CHOICE')
