"""Ce code vérifie si une chaîne de caractères est un palindrome
"""
import re
#### Fonction secondaire

def ispalindrome(p:str)->bool:
    """
    cette fonction vérifie si une chaîne de caractères est un palindrome
    en retournant True si p est un palindrome, False sinon.
    p est La chaîne de caractères à vérifier.
    """
    accents = str.maketrans("éèêëàâäîïôöùûüç","eeeeaaaiioouuuc")
    p=p.lower().translate(accents)
    p=re.sub(r'[^a-z0-9]', '', p)
    p_second=p[::-1]
    return p_second == p

#### Fonction principale

def main():
    """
    Fonction principale pour tester la fonction ispalindrome avec plusieurs cas de test.
    """
    # Liste des cas de test
    test_cases= [
        "radar",# True
        "kayak",# True
        "civic",# True
        "deified",# True
        "hello",# False
        "world",# False
    ]
    # Test de chaque chaîne de caractères
    for i in test_cases:
        print(i, ispalindrome(i))
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
