def citire(lista):
    nr_elemente=int(input("Dati numarul de elemente:"))
    for i in range(nr_elemente):
        lista.append(int(input("Dati numar:")))
    return lista

def nr_negative_nenule(l):
    negative=[]
    for x in l:
        if x<0:
            negative.append(x)
    return negative

def test_nr_negative_nenule():
    assert nr_negative_nenule([2,4,-1,0]) == [-1]
    assert nr_negative_nenule([2,4,5]) == []
    assert nr_negative_nenule([-1,-2,-3]) == [-1,-2,-3]



def print_menu():
    print("1. Citire lista.")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("a. Afisare lista.")
    print("x. Iesire.")

def main():
    test_nr_negative_nenule()
    while True:
        print_menu()
        optiune=input("Dati optiunea:")
        if optiune == "1":
            lista=[]
            citire(lista)
        elif optiune == "a":
            print(lista)
        elif optiune == "2":
            print(nr_negative_nenule(lista))
        elif optiune == "x":
            print("Meniul se va inchide.")
            break
        else:
            print("Optiune invalida.Reincercati!")


if __name__ == '__main__':
    main()