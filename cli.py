import json

class Cli:
    def __init__(self):
        print('===Welcome To The Library System===')

    def start(self):
        print(
                """
Bienvenue que désirez vous faire ? 
    1 Chercher un livre
    2 Choisir un utilisateur
    3 Emprunter un livre
    4 Gestion des livres
    5 Gestion des utilisateurs
    6 Exit
                """
        )

        print ('===>', end=" ")
        action = input()

        match action:
            case '1':
                self.findBook()
                return True
            case '6':
                return False
            case _:
                return True

    def findBook(self):
        print('Quel livre cherchez vous ?')

        print('===>', end=" ")
        bookName = input()

        file = open('livres.json')
        books = json.load(file)

        for index, book in enumerate(books):
            if bookName in book['titre']:
                disponible = 'Disponible' if book['disponible'] else 'Non Disponible'

                print('Livre correspondant à la recherche :')
                print(f"nº {index} {book['titre']}: {disponible}")


        
