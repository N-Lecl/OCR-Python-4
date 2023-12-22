import os

class Utils:
    
    def clear_terminal():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')