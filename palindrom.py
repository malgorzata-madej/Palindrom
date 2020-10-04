def palindrom(slowo):
    """
    Funkcja sprawdza, czy dane słowo jest palindromem,
    czyli czy słowo czytane od lewej do prawej i od prawej do lewej jest takie samo.
    """
    lista = []
    lista_odwrotnie= []

    for letter in slowo:
        lista.append(letter)

    lista_odwrotnie = lista[::-1]

    if lista == lista_odwrotnie:
        print("Slowo jest palindromem")
    else:
        print("Słowo nie jest palindromem")

   
slowo = input("Podaj slowo, ktore chcesz sprawdzic: ")
palindrom(slowo)



