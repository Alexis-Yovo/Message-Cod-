# Import de la bibliothèque random (inutile ici, mais conservé si vous souhaitez l'utiliser plus tard)
import random

# On définit 2 types de listes pour faire le cryptage
liste_clair = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
liste_code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

# L'utilisateur saisit un message clair
message_clair = input('Saisir un message clair : ').upper()  # Convertir en majuscules pour correspondre à liste_clair
message_code = ""

# On parcourt chaque lettre du message clair
for lettre in message_clair:
    if lettre in liste_clair:
        indice = liste_clair.index(lettre)
        message_code += liste_code[indice] + " "  # Ajouter un espace entre les codes pour plus de lisibilité
    else:
        message_code += "?"  # Remplacer les caractères inconnus par un "?" ou un autre caractère

# Affichage du message codé
print("Message codé :", message_code.strip())
