
def addition(a, b):
    result = a + b
    return result

def main():
    # Entrées pour l'addition
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))

    # Appeler la fonction d'addition
    sum_result = addition(num1, num2)

    # Afficher le résultat
    print(f"La somme de {num1} et {num2} est : {sum_result}")

if __name__ == "__main__":
    main()
