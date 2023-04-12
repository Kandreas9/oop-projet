import json

class Cli:
    def __init__(self):
        print('===Welcome To The Library System===')

    def customInput(self):
        print('===>', end=" ")
        return input()

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
            case '3':
                self.borrowBook()
                return True
            case '6':
                return False
            case _:
                return True

    def findBook(self):
        print('Quel livre cherchez vous ?')

        bookName = self.customInput()

        file = open('livres.json')
        books = json.load(file)

        for index, book in enumerate(books):
            if bookName in book['titre']:
                disponible = 'Disponible' if book['disponible'] else 'Non Disponible'

                print('Livre correspondant à la recherche :')
                print(f"nº {index} {book['titre']}: {disponible}")

    def borrowBook(self):
        print("Quel est le numéro de l'utilisateur ?")

        userId = self.customInput()

        print('Quel est le numéro du livre ?')

        bookId = self.customInput()
        
        file = open('utilisateurs.json')
        users = json.load(file)
        file2 = open('livres.json')
        books = json.load(file2)

        file.close()
        file2.close()

        user = users[int(userId)]
        
        user['livres'].append(bookId)

        if (len(user['livres']) == 3):
            bookInfo = books[-1]

            print(f"{user['nom']} {user['prénom']} emprunte {bookInfo['titre']}")
            print(f"{user['nom']} {user['prénom']} ne peut plus emprunter de livres")
        else:
            canBorrow = 3 - len(user['livres'])

            bookInfo = books[-1]
            
            print(f"{user['nom']} {user['prénom']} emprunte {bookInfo['titre']}")

            writeFile = open('utilisateurs.json', 'w')
            writeFile.write(json.dumps(users))
            writeFile.close()

            print(f"{user['nom']} {user['prénom']} peut encore emprunter {canBorrow} livres.")
        
