from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.tournament_view import TournamentView

class MainController:
    def __init__(self):
        self.player_controller = PlayerController(None, None)
        self.tournament_controller = TournamentController(None, TournamentView()) 

    def run(self):
        while True:
            print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("   ___         _   _                   _        _____                             _ ")
            print("  / _ \___ ___| |_(_) ___  _ __     __| | ___  /__   \___  _   _ _ __ _ __   ___ (_)")
            print(" / /_\/ _ / __| __| |/ _ \| '_ \   / _` |/ _ \   / /\/ _ \| | | | '__| '_ \ / _ \| |")
            print("/ /_\|  __\__ | |_| | (_) | | | | | (_| |  __/  / / | (_) | |_| | |  | | | | (_) | |")
            print("\____/\___|___/\__|_|\___/|_| |_|  \__,_|\___|  \/   \___/ \__,_|_|  |_| |_|\___/|_|")
            print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            
            print("\n1. Gérer les joueurs")
            print("2. Gérer les tournois")
            print("3. Quitter")

            choice = input("\nChoisissez une option (1, 2, ou 3): ")

            if choice == "1":
                self.player_menu()
            elif choice == "2":
                self.tournament_menu()
            elif choice == "3":
                print("Merci d'avoir utilisé l'application. Au revoir!")
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

    def player_menu(self):
        while True:
            print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("                            __                                  ")
            print("  /\/\   ___ _ __  _   _    \ \  ___  _   _  ___ _   _ _ __ ___ ")
            print(" /    \ / _ | '_ \| | | |    \ \/ _ \| | | |/ _ | | | | '__/ __|")
            print("/ /\/\ |  __| | | | |_| | /\_/ | (_) | |_| |  __| |_| | |  \__ \ ")
            print("\/    \/\___|_| |_|\__,_| \___/ \___/ \__,_|\___|\__,_|_|  |___/")
            print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        
            print("\n1. Ajouter un joueur")
            print("2. Voir la liste des joueurs")
            print("3. Retour au menu principal")

            choice = input("\nChoisissez une option (1, 2, ou 3): ")

            if choice == "1":
                self.player_controller.add_player_menu() 
            elif choice == "2":
                self.player_controller.display_all_players()  
            elif choice == "3":
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

    def tournament_menu(self):
        while True:
            print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("                           _____                             _ ")
            print("  /\/\   ___ _ __  _   _  /__   \___  _   _ _ __ _ __   ___ (_)")
            print(" /    \ / _ | '_ \| | | |   / /\/ _ \| | | | '__| '_ \ / _ \| |")
            print("/ /\/\ |  __| | | | |_| |  / / | (_) | |_| | |  | | | | (_) | |")
            print("\/    \/\___|_| |_|\__,_|  \/   \___/ \__,_|_|  |_| |_|\___/|_|")
            print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        
            print("\n1. Créer un nouveau tournoi")
            print("2. Ajouter des joueurs au tournoi")
            print("3. Générer les appariements pour le prochain tour")
            print("4. Afficher les détails du tournoi")
            print("5. Retour au menu principal")

            choice = input("\nChoisissez une option (1, 2, 3, 4, ou 5): ")

            if choice == "1":
                self.tournament_controller.create_tournament()
            elif choice == "2":
                all_players = self.player_controller.load_players_from_json('players_infos.json')
                self.tournament_controller.add_players_to_tournament()
            elif choice == "3":
                self.tournament_controller.generate_pairings()
            elif choice == "4":
                self.tournament_controller.display_tournament_details()
            elif choice == "5":
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main_controller = MainController()
    main_controller.run()

