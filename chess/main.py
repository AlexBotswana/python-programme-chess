from models.TournamentModel import TournamentModel
from views.MenuView import MenuView


data_set = 0
print('\n1 - Upload data set?')
print('2 - Do nothing')
data_set = int(input('\n Your choice: '))
if data_set == 1:
    TournamentModel.init_db()
out = 0
while out != 1:
    try:
        MenuView.menu()
        out = 1
    except Exception:
        print('WRONG CHOICE')

