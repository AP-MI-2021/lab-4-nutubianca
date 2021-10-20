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


def nr_minim_cifra_data(l,cifra):
    nr_minim=None
    for x in l:
        if x%10==cifra or -x%10==cifra:
            if nr_minim==None:
                nr_minim=x
            else:
                if x<nr_minim:
                    nr_minim=x
    return nr_minim


def test_nr_minim_cifra_data():
    assert nr_minim_cifra_data([-2,3,-3,2], 2) == -2
    assert nr_minim_cifra_data([3,13,43], 3) == 3
    assert nr_minim_cifra_data([2,4,5], 1) == None


def print_menu():
    print("1. Citire lista.")
    print("2. Afișarea tuturor numerelor negative nenule din listă.")
    print("3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
    print("4. Afișarea tuturor numerelor din listă care sunt superprime.")
    print("5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu"
          "CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
    print("a. Afisare lista.")
    print("x. Iesire.")


def main():
    test_nr_negative_nenule()
    test_nr_minim_cifra_data()
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
        elif optiune == "3":
            cifra=int(input("Dati cifra:"))
            print(nr_minim_cifra_data(lista,cifra))
        elif optiune == "x":
            print("Meniul se va inchide.")
            break
        else:
            print("Optiune invalida.Reincercati!")


if __name__ == '__main__':
    main()