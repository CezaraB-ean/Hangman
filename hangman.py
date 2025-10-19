import csv

cuvinte_posibile = []
with open('cuvinte_de_verificat.csv', newline='',encoding='utf-8-sig') as fisier_intrare:
    reader = csv.reader(fisier_intrare,delimiter=';')
    for linie in reader:
        if not linie or all(cell.strip() == "" for cell in linie):
            print("Exista o eroare in fisierul de date. Rezolvati problema si rulati din nou!")
            continue
        if len(linie) != 3:
            print(f"Linia {linie} este invalida.")
            continue
        if len(linie[1]) != len(linie[2]):
            print(f"Cuvantul {linie[1]} este invalid. Rezolvati problema si rulati din nou!")
            continue
        try:
            linie_formatata = [int(linie[0]),linie[1],linie[2]]
            cuvinte_posibile.append(linie_formatata)
        except ValueError:
            print(f"Linia {linie} este invalida.")

litere = ['E', 'I', 'A', 'U', 'T', 'R', 'N', 'L', 'C', 'S', 'O', 'M', 'Ă', 'Â', 'Î', 'Ș', 'Ț', 'D', 'P', 'B', 'V', 'F', 'G', 'Z', 'H', 'K', 'J', 'Q', 'W', 'X', 'Y']
incercari_totale = 0
n = 0
lista_cuv_de_incercat = []
lista_litere_de_incercat = []
lista_semifinala = []
lista_finala = []
lista_incercari = []
date_finale = [[] for i in range(len(cuvinte_posibile))]

def determinare_lista_cuv_de_incercat(pereche):
    dictionar = open("dictionar_mijloc.txt", "r", encoding="UTF-8")
    linie = dictionar.readline()
    while linie != "":
        linie = linie.replace("\n", "")
        if len(linie) == len(pereche[2]):
            lista_cuv_de_incercat.append(linie.upper())
        linie = dictionar.readline()
    dictionar.close()

def rarire_cuvinte(lista_cuv_de_incercat,pereche):
    litere_folosite = []
    poz_litere_folosite = []
    for i in range(len(pereche[1])):
        if pereche[1][i] != "*":
            litere_folosite.append(pereche[1][i])
            poz_litere_folosite.append(i)
    for element in lista_cuv_de_incercat:
        contor = 0
        for i in range(len(litere_folosite)):
            if litere_folosite[i] in element:
                contor += 1
        if contor == len(litere_folosite):
            lista_semifinala.append(element)

def rarire_extra(lista,pereche):
    cuv = pereche[1]
    global lista_semifinala,lista_finala
    for element in lista:
        for char_e,char_c in zip(element,cuv):
            if char_c != "*" and char_e != char_c:
                element = ''
                break
        if element != '':
            lista_finala.append(element)

def litere_de_incercat(lista):
    lista_litere_de_incercat = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] not in lista_litere_de_incercat:
                lista_litere_de_incercat.append(lista[i][j])
    return lista_litere_de_incercat

def raritoare(lista,pereche):
    global lista_semifinala,lista_finala,lista_litere_de_incercat
    rarire_cuvinte(lista,pereche)
    rarire_extra(lista_semifinala,pereche)
    lista_litere_de_incercat = litere_de_incercat(lista_finala)

def ghicitoare(lista_litere, pereche):
    cuvant_de_ghicit = list(pereche[1])
    cuvant = list(pereche[2])
    out,i,nr_incercari = 0,0,0
    global incercari_totale,lista_litere_de_incercat,lista_incercari,n
    while cuvant_de_ghicit != cuvant and out<100:
        if lista_litere[i] in cuvant_de_ghicit: lista_litere.pop(i)
        elif lista_litere[i] in cuvant and lista_litere[i] not in cuvant_de_ghicit:
            nr_incercari += 1
            print(f"Incercarea cu nr. {nr_incercari} este {lista_litere[i]} si se afla in cuvant.")
            for j in range(len(cuvant)):
                if cuvant[j] == lista_litere[i]:
                    cuvant_de_ghicit[j] = cuvant[j]
            lista_incercari.append(lista_litere[i])
            i += 1
        else:
            nr_incercari += 1
            print(f"Incercarea cu nr. {nr_incercari} este {lista_litere[i]} si NU se afla in cuvant.")
            lista_incercari.append(lista_litere[i])
            i += 1
        out+= 1
    if out < 100:
        status = "OK"
    else:
        status = "FAIL"
    incercari_totale += nr_incercari
    adaugitoare(n, pereche, nr_incercari, lista_incercari, status)
    lista_litere_de_incercat,lista_incercari = [],[]

def adaugitoare(n,pereche,nr_incercari,lista_incercari,status):
    global date_finale,incercari_totale
    incercari = ''
    date_finale[n].append(pereche[0])
    date_finale[n].append(nr_incercari)
    date_finale[n].append(pereche[2])
    if status == "OK":
        date_finale[n].append("OK")
    else:
        date_finale[n].append("FAIL")
    for litera in lista_incercari:
        incercari += litera + " "
    date_finale[n].append(incercari)
    if n == 99:
        date_finale.append(['total','incercari','este',f"{incercari_totale}",'!'])

def sal_vere():
    with open("date_iesire.csv",'w+',newline='',encoding='utf-8-sig') as date_iesire:
        writer = csv.writer(date_iesire,delimiter=',')
        writer.writerows(date_finale)

def joc():
    for pereche in cuvinte_posibile:
        global lista_cuv_de_incercat, lista_litere_de_incercat, lista_semifinala, lista_finala, n
        lista_cuv_de_incercat = []
        lista_litere_de_incercat = []
        lista_semifinala = []
        lista_finala = []
        determinare_lista_cuv_de_incercat(pereche)
        raritoare(lista_cuv_de_incercat, pereche)
        ghicitoare(lista_litere_de_incercat,pereche)
        n += 1
    sal_vere()
    print(f"Numarul incercarilor totale este: {incercari_totale}")

joc()