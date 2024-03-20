import os


class Utils:

    def clear_terminal():
        """
        Nettoye la console pour plus de lisibilité
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
