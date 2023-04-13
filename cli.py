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

        action = self.customInput()

        match action:
            case '1':
                self.findBook()
                return True
            case '3':
                self.borrowBook()
                return True
            case '4':
                self.bookManagement()
                return True
            case '5':
                self.userManagement()
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
                print(book['disponible'])
                disponible = 'Disponible' if book['disponible'] == 'True' else 'Non Disponible'

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
        book = books[int(bookId)]

        if book['disponible'] == 'True':
            user['livres'].append(bookId)
            book['disponible'] = 'False'
        else:
            print('Book is unavailable.')
            return

        if (len(user['livres']) == 3):
            bookInfo = books[-1]

            print(f"{user['nom']} {user['prénom']} emprunte {bookInfo['titre']}")
            print(f"{user['nom']} {user['prénom']} ne peut plus emprunter de livres")
        else:
            canBorrow = 3 - len(user['livres'])
            
            print(f"{user['nom']} {user['prénom']} emprunte {book['titre']}")

            writeFileUser = open('utilisateurs.json', 'w')
            writeFileUser.write(json.dumps(users, indent=4))
            writeFileUser.close()

            writeFileBook = open('livres.json', 'w')
            writeFileBook.write(json.dumps(books, indent=4))
            writeFileBook.close()

            print(f"{user['nom']} {user['prénom']} peut encore emprunter {canBorrow} livres.")
        
    def bookManagement(self):
        print(
                """
Que désirez vous faire ? 
    1 modifier un livre
    2 supprimer un livre
    3 ajouter un livre
    4 exit
                """
        )

        bookAction = self.customInput()

        match bookAction:
            case '1':
                self.updateBook()
                return True
            case '2':
                self.removeBook()
                return True
            case '3':
                self.addBook()
                return True
            case '4':
                return False
            case _:
                return True


    def addBook(self):
        print('Titre :')
        title = self.customInput()
        print('Auteur :')
        author = self.customInput()
        print('Année :')
        year = self.customInput()
        print('Editeur :')
        editor = self.customInput()
        print('Genre :')
        genre = self.customInput()

        newBook = {
            "auteur": author,
            "titre": title,
            "editeur": editor,
            "annee": int(year),
            "genre": genre,
            "disponible": "True"
        }

        books = None

        with open('livres.json') as file:
            books = json.load(file)
            books.append(newBook)
            
        with open('livres.json', 'w') as file:
            json.dump(books, file, indent=4)
            print('The book has been created!')


    def removeBook(self):
        print('Book Id :')
        bookId = self.customInput()

        books = None

        with open('livres.json') as file:
            books = json.load(file)
            del books[int(bookId)]
            
        with open('livres.json', 'w') as file:
            json.dump(books, file, indent=4)
            print('The book has been removed!')

    
    def updateBook(self):
        print('Book Id :')
        bookId = self.customInput()
        print('Titre :')
        title = self.customInput()
        print('Auteur :')
        author = self.customInput()
        print('Année :')
        year = self.customInput()
        print('Editeur :')
        editor = self.customInput()
        print('Genre :')
        genre = self.customInput()
        print('Availability :')
        availability = self.customInput()

        books = None

        with open('livres.json') as file:
            books = json.load(file)
            books[int(bookId)] = {
                        **books[int(bookId)],
                        "auteur": author,
                        "titre": title,
                        "editeur": editor,
                        "annee": int(year),
                        "genre": genre,
                        "disponible": availability
            } 

        with open('livres.json', 'w') as file:
            json.dump(books, file, indent=4)
            print('The book has been updated!')


    def userManagement(self):
        print(
                """
Que désirez vous faire ? 
    1 modifier un user
    2 supprimer un user
    3 ajouter un user
    4 exit
                """
        )

        userAction = self.customInput()

        match userAction:
            case '1':
                self.updateUser()
                return True
            case '2':
                self.removeUser()
                return True
            case '3':
                self.addUser()
                return True
            case '4':
                return False
            case _:
                return True

    def addUser(self):
        print('Nom :')
        nom = self.customInput()
        print('Prenom :')
        prenom = self.customInput()
        print('Age :')
        age = self.customInput()
        print('Adresse email :')
        email = self.customInput()
        print('Type :')
        userType = self.customInput()


        newUser = {
            "nom": nom,
            "pr\u00e9nom": prenom,
            "age": int(age),
            "adresse email": email,
            "type": userType,
            "livres": []
        }

        users = None

        with open('utilisateurs.json') as file:
            users = json.load(file)
            users.append(newUser)
            
        with open('utilisateurs.json', 'w') as file:
            json.dump(users, file, indent=4)
            print('The user has been created!')

    def removeUser(self):
        print('User Id :')
        userId = self.customInput()

        users = None

        with open('utilisateurs.json') as file:
            users = json.load(file)
            del users[int(userId)]
            
        with open('utilisateurs.json', 'w') as file:
            json.dump(users, file, indent=4)
            print('The user has been removed!')

    def updateUser(self):
        print('User Id :')
        userId = self.customInput()
        print('Nom :')
        nom = self.customInput()
        print('Prenom :')
        prenom = self.customInput()
        print('Age :')
        age = self.customInput()
        print('Adresse email :')
        email = self.customInput()
        print('Type :')
        userType = self.customInput()

        users = None

        with open('utilisateurs.json') as file:
            users = json.load(file)
            users[int(userId)] = {
                **users[int(userId)],
                "nom": nom,
                "pr\u00e9nom": prenom,
                "age": int(age),
                "adresse email": email,
                "type": userType,
            }
 

        with open('utilisateurs.json', 'w') as file:
            json.dump(users, file, indent=4)
            print('The user has been updated!')

