# python-programme-chess
projet4 openclassroom: application to manage a chess tournament (swiss model)
using MVC model (Models-Views-Controllers) for development and TinyDb as database

Installation    
Copy/paste the repository chess (with all its content)
        
        git clone https://github.com/AlexBotswana/python-programme-chess.git
    
Create and activate a virtual environment:
        
        py -m venv .venv
        .\scripts\activate
    
To desactivate the virtual environment:
        
        deactivate
        
In the virtual environment, paste the file requirements.txt and execute the following command:
        
        pip install -r requirements.txt

Execution
    In the folder chess, execute the program as follow:
            
        py main.py

Générer un rapport flake8

    flake8 --format=html --htmldir=flake8_rapport
