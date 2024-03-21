from controllers import menu_controller


def main():
    # Création et execution d'une instance du contrôleur de menu principal
    controller = menu_controller.MenuPrincipalControleur()
    controller()


# Point d'entrée du programme
if __name__ == "__main__":
    # Appel de la fonction principale
    main()
