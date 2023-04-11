# Définition des questions
question1 = " 1. Chercher un livre "
question2 = " 2. Choisir un utilisateur "
question3 = " 3. Empruntez un livre "
question4 = " 4. Gestion des livres "
question5 = " 5. Gestions des utilisateurs "
question6 = " 1. Modifiez un livre "
question7 = " 2. Supprimez un livre "
question8 = " 3. Gestions des utilisateurs"

# Proposition des questions à l'utilisateur
print("Choisissez l'une des cinq propositions suivantes : ")
print("1. " + question1)
print("2. " + question2)
print("3. " + question3)
print("4. " + question4)
print("5. " + question5)

# Lecture de la réponse de l'utilisateur
choix = input("Entrez le numéro de votre choix (1-5) : ")

# Traitement de la réponse
if choix == "1":
    reponse = input("Quel livre recherchez vous ? Entrez le titre du livre : ")
elif choix == "2":
    reponse = input(question2)
elif choix == "3":
    reponse = input("Quel est le numéro du livre ? Entrez le numéro du livre : ")
elif choix == "4":
    reponse = print("Que désirez vous faire ?")
    
    print(question6)
    print(question7)
    print(question8)

    input(" Entrez le numéro de votre choix (1-3) : ")
    
elif choix == "5":
    reponse = input(question5)
else:
    print("Choix invalide.")

# Affichage de la réponse
print(reponse)
