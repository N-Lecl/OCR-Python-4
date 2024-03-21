import os


class Utils:
    """
    Classe utilitaire pour fournir des fonctionnalités utilitaires.
    """

    def clear_terminal():
        """
        Efface le terminal pour améliorer la lisibilité de l'interface utilisateur.
        """
        # Vérifie le système d'exploitation pour déterminer la commande appropriée pour effacer le terminal
        if os.name == 'nt':  # Si le système d'exploitation est Windows
            os.system('cls')  # Efface la console Windows
        else:  # Pour les autres systèmes d'exploitation (Linux, MacOS)
            os.system('clear')  # Efface le terminal en utilisant la commande clear
