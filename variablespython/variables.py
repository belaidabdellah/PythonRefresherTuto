# Règles de nommages
# 1 - les variables sont en miniscule avec _ comme espace, mais caractères spéciaux
# 2 - mettre des commentaires clairs à chaque nouvelle opération
# 3 - laisser un espace après les virgules dans les paramètres

# recolter une valeur porte monnaie
wallet = int(input("Entrer le nombre d'€ que vous possedez"))
print("Vous avez actuellement", wallet, "euros")

# creer un produit qui aura pour valeur 50
produit = 50
print("Le Produit vaut ", produit, "euros")

# enleve au "wallet" le prix du produit
wallet = wallet - produit
# ou wallet -= produit

# afficher la nouvelle valeur
print("Produit acheté !")
print("Il ne vous reste plus que", wallet, "euros")