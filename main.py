def citire(lista):
    nr_elemente=int(input("Dati numarul de elemente:"))
    for i in range(nr_elemente):
        lista.append(int(input("Dati numar:")))
    return lista

def nr_negative_nenule(l):
    """
    -afiseaza toate numerele negative nenule din lista
    :param l: lista data de numere intregi
    :return negative: lista de numere negatice cerute din l
    """
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
    """
    -gaseste cel mai mic numar ce are ca ultima cifra cifra data de utilizator
    :param l: lista de numere intregi
    :param cifra: cifra data de utilizator, de tip intreg
    :return nr_minim: returneaza valoarea ceruta; daca nu
    se gaseste niciun numar valabil,se returneaza None
    """
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



def verificare_prim(n):
    '''
    -determina daca un numar dat n este prim sau nu
    Input:
    -parametru: n (de tip intreg)
    Output:
    -va returna True, daca n este prim, sau False, in caz contrar(de tip bool)
    '''
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n//2+1, 2):
        if n%i == 0:
            return False
    return True


def is_superprime(n):
    ''''
    -deteremina daca un numar este superprim sau nu
    Input:
    -parametru: n (de tip intreg)
    Output:
    -va returna True, daca n este superprim, sau False, in caz contrar(de tip bool)
    '''
    copie = n
    verificare = 1
    #presupunem ca numarul dat este superprim
    while copie:
        if not verificare_prim(copie):
            verificare=0
            break
        copie=copie//10
    if verificare==1:
        return True
    return False

def lista_superprime(l):
    """
    -determina ce numere sunt supeprime din lista data
    :param l: lista de numere intregi
    :return superprime: lista cu numerele din lista l care sunt supeprime
    """
    superprime=[nr for nr in l if nr>0 and is_superprime(nr)]
    return superprime

def test_lista_superprime():
    assert lista_superprime([1,13,14]) == []
    assert lista_superprime([239,23,14]) == [239,23]
    assert lista_superprime([14,173,3]) == [3]


def cmmdc(nr1,nr2):
    while nr1!=nr2:
        if nr1>nr2:
            nr1=nr1-nr2
        else:
            nr2=nr2-nr1
    return nr1

def cmmdc_lista(l):
    """
    -determina cmmdc-ul dintr-o lista data
    :param l: o lista de numere intregi
    :return divizor: returneaza cmmdc-ul tuturor numerelor din l
    """
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return cmmdc(l[0],l[1])
    else:
        divizor == cmmdc(l[0],l[1])
        for i in range(2,len(l)):
            divizor=cmmdc(divizor,l[i])
        return divizor


def modificare_dupa_semn(l):
    """
    -determina lista obținuta din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    :param l: o lista de numere intregi
    :return lista_noua: o lista modificata conform cerintei
    """
    lista_pozitive = [nr for nr in l if nr > 0]
    inlocuire_pozitive=cmmdc_lista(lista_pozitive)
    lista_noua=[]
    for x in l:
        if x>0:
            lista_noua.append(inlocuire_pozitive)
        elif x == 0:
            lista_noua.append(x)
        else:
            negativ= x*(-1)
            negativ="-"+str(negativ)[::-1]
            negativ=int(negativ)
            lista_noua.append(negativ)
    return lista_noua

def test_modificare_dupa_semn():
    assert modificare_dupa_semn([4,-12,-5]) == [4,-21,-5]
    assert modificare_dupa_semn([-32,12,24]) == [-23,12,12]


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
    test_lista_superprime()
    test_modificare_dupa_semn()
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
        elif optiune == "4":
            print(lista_superprime(lista))
        elif optiune == "5":
            print(modificare_dupa_semn(lista))
        elif optiune == "x":
            print("Meniul se va inchide.")
            break
        else:
            print("Optiune invalida.Reincercati!")


if __name__ == '__main__':
    main()