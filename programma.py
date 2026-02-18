import random
import os

q = 0
N = 0
s = 0
numero_punti = 0
conta_riga = 0
stringa = ""
lista = []
sottospazi =[]

#Domanda 1
def lettura_input():
    global conta_riga, q, N, s, numero_punti, lista, stringa, sottospazi
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, "PG_2_16.txt")
    with open(filepath) as file:
        while True:
            riga = file.readline() #Lettura riga per riga
            if not riga: 
                break
            
            if(conta_riga <=2):
                if(conta_riga == 0):
                    q = int(riga.strip())
                    print("Q = ", q)
                elif(conta_riga == 1):
                    N = int(riga.strip())
                elif(conta_riga == 2):
                    s = int(riga.strip())
                    numero_punti = calcola_punti_spazio(q, N)
                conta_riga = conta_riga + 1
            elif(conta_riga > 2):
                stringa = stringa + riga.strip()
            #print(riga.strip())  #Strip tagli l'ultimo carattere della riga cioe "\n"
        lista=stringa.split('}') #split per separare la stringa ad ogni lettura di ','
        #for i in range(len(lista)):
        #    lista[i] = lista[i]+"}"
        for l in lista:
            l = l.lstrip('{')
            a = l.split(',')
            r = [int(x) for x in a if x != '']
            s = set(r)
            sottospazi.append(s)

#Domanda 2
def calcola_intersezione(retta, insieme_punti):
    if(retta == 1):
        exit(1)
    #print("La retta ", retta)
    #print("Insieme di punti ", insieme_punti)
    
    return set.intersection(retta,insieme_punti)

#Domanda 3
def calcola_cardinalita_intersezione(retta, insieme_punti):
    intersezione = calcola_intersezione(retta, insieme_punti)
    return len(intersezione)

#Domanda 4
def calcola_specie(insieme_punti):
    # massimo = 0
    # for s in sottospazi:
    #     m = calcola_cardinalita_intersezione(s, insieme_punti)
    #     if massimo < m :
    #         massimo = m
    # return massimo
    return max(calcola_cardinalita_intersezione(s, insieme_punti) for s in sottospazi)


def calcola_punti_spazio(campo, dimensione):
    somma = 0
    for i in range(dimensione+1):#Il mio for parte da 0 fino a dimenzione
        somma = somma + campo**i
    return somma

def stampa_numero_rette_sottospazio(sottospazio):
    return len(sottospazio)

def  stampa_sottospazi():
    print(lista)

def stampa_sottospazio(posizione):
    print(lista[posizione])

# def ricava_retta(sottospazio, posizione_retta):
#     rette = sottospazio.split('}')
#     for i in range(len(rette)):
#         rette[i]=rette[i].lstrip("{") #Togliere il carattere a Sx
#         rette[i]=rette[i].rstrip("}")#Togliere il carattere a Dx
#     if(posizione_retta < len(rette) and posizione_retta >= 0):
#         retta = rette[posizione_retta].split(',')
#         for j in range(len(retta)):
#             retta[j]=int(retta[j])
#         return retta
#     else:
#         print("Posizione non corretta")
#         return 1

#Domanda 5
def verifica_retta_con_s_piu_uno_punti_intersezioni(insieme_punti, specie):
    for l in sottospazi:
        if calcola_cardinalita_intersezione(l, insieme_punti)>= specie + 1:
            print("Esiste almeno una retta con almeno ",specie +1," punti")
            break


#Domanda 6
def punti_coperti(insieme_punti, specie):
    coperti = insieme_punti
    for s in sottospazi:
        if calcola_cardinalita_intersezione(s, insieme_punti) == specie:
            #print(s)
            coperti = set.union(s, coperti)
    return coperti

#Domanda 7
def punti_non_coperti(insieme_punti, specie):
    coperti = punti_coperti(insieme_punti, specie)
    non_coperti = []
    #li = []
    #for s in range(1,273+1):
    #    li.append(s)
    #non_coperti = set(li)
    non_coperti = set(range(1,numero_punti+1))
    lista_non_coperti = non_coperti.difference(coperti)
    #lista_non_coperti = [item for item in non_coperti if item not in coperti]
    return lista_non_coperti


#Domanda 8
def calcola_insieme_completo_greedy(insieme_iniziale, specie, a_caso = 0.1):
    
    insieme_punti = insieme_iniziale.copy()
    ins_punti_coperti = punti_coperti(insieme_punti, specie)
    if len(ins_punti_coperti) == numero_punti:
        return insieme_punti

    while(1):
        ins_punti_non_coperti = punti_non_coperti(insieme_punti, specie)
        if random.random() < a_caso:
            px = random.choice(list(ins_punti_non_coperti))
            insieme_punti.add(px)
            massimo_num_punti_coperti = len(punti_coperti(insieme_punti ,  specie))
        else :
            massimo_num_punti_coperti = 0
            insieme_punti_aggiunger = []
            for punto in ins_punti_non_coperti:
                insieme_punti.add(punto)
                punti = punti_coperti(insieme_punti, specie)
                nb = len(punti)
                if nb > massimo_num_punti_coperti:
                    massimo_num_punti_coperti = nb
                    insieme_punti_aggiunger = [punto]
                elif nb == massimo_num_punti_coperti:
                    insieme_punti_aggiunger.append(punto)
                insieme_punti.remove(punto)
            px = random.choice(insieme_punti_aggiunger)
            insieme_punti.add(px)
        
        if massimo_num_punti_coperti == numero_punti:
            return insieme_punti

#Domanda 9
def calcola_insieme_completo_greedy_grande(insieme_iniziale, specie, a_caso = 0.1):
    
    insieme_punti = insieme_iniziale.copy()
    ins_punti_coperti = punti_coperti(insieme_punti, specie)
    if len(ins_punti_coperti) == numero_punti:
        return insieme_punti

    while(1):
        ins_punti_non_coperti = punti_non_coperti(insieme_punti, specie)
        if random.random() < a_caso:
            px = random.choice(list(ins_punti_non_coperti))
            insieme_punti.add(px)
            minimo_num_punti_coperti = len(punti_coperti(insieme_punti ,  specie))
        else :
            minimo_num_punti_coperti = numero_punti
            insieme_punti_aggiunger = []
            for punto in ins_punti_non_coperti:
                insieme_punti.add(punto)
                punti = punti_coperti(insieme_punti, specie)
                nb = len(punti)
                if nb < minimo_num_punti_coperti:
                    minimo_num_punti_coperti = nb
                    insieme_punti_aggiunger = [punto]
                elif nb == minimo_num_punti_coperti:
                    insieme_punti_aggiunger.append(punto)
                insieme_punti.remove(punto)
            px = random.choice(insieme_punti_aggiunger)
            insieme_punti.add(px)
        
        if minimo_num_punti_coperti == numero_punti:
            return insieme_punti

x = set([1, 2, 23, 34, 84, 123, 136, 142, 146, 160, 176, 201, 227, 230, 232, 239, 247])#insieme di punti
y = set([1, 2, 3, 200])
lettura_input()         
print("q = ",q)
print("N = ", N)
print("s = ", s)
print("I punti dello spazio = ", calcola_punti_spazio(16,2))
#print(ricava_retta(lista[0], 0))

print("Punti di intersezione: ", calcola_intersezione(sottospazi[10], x))
print("Cardinalità ", calcola_cardinalita_intersezione(sottospazi[10], x))

print("La specie : ", calcola_specie(y))

print("I punti coperti", punti_coperti(y, 2))
print("I punti coperti cardinalità ", len(punti_coperti(y, 2)))
print("Lunghezza y: ", len(y))
verifica_retta_con_s_piu_uno_punti_intersezioni(x, 2)
print("Punti non coperti : ", punti_non_coperti(y, 2))
print("Cardinalita punti non coperti :", len(punti_non_coperti(y,2)))

s1 = calcola_insieme_completo_greedy(set([1,2,3]), 4)
print(s1 )
print( len(s1))

s1 = calcola_insieme_completo_greedy(set([1,2,3]), 4)
print(s1 )
print( len(s1))

s1 = calcola_insieme_completo_greedy(set([1,2,3]), 4)
print(s1 )
print( len(s1))

s1 = calcola_insieme_completo_greedy_grande(set([1,2,3]), 4)
print(s1 )
print(len(s1))

s1 = calcola_insieme_completo_greedy_grande(set([1,2,3]), 4)
print(s1 )
print(len(s1))

s1 = calcola_insieme_completo_greedy_grande(set([1,2,3]), 4)
print(s1 )
print( len(s1))

s1 = calcola_insieme_completo_greedy(set([1,2,3]), 4, 1)
print(s1 )
print( len(s1))

s1 = calcola_insieme_completo_greedy(set([1,2,3]), 4, 1)
print(s1 )
print(len(s1))

s1 = calcola_insieme_completo_greedy(set([1,2,3]), 4, 1)
print(s1 )
print(len(s1))
