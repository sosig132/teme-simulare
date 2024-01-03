#Importam librariile necesare
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import concurrent.futures

def generate_exp():
#Generam variabila exponentiala Exp(1), cu cea de-a treia teorema de respingere, folosind algoritmul Resp3-Exp din cursul 5
    X = 0
    #Pas 1
    N=0
    #Pas 2: Generam doua variabile uniform distribuite U0 si U1 pe intervalul [0,1], independente una de cealalta

    steps_0=0
    while True:
        steps_0+=1
        steps_1=0
        U0=np.random.uniform(0,1)
        U1=np.random.uniform(0,1)

        #Pas 3: U* = U0, K=1
        U_star=U0
        K=1

        #Pas 4: Daca U0>=U1 mergem la pasul 5, altfel mergem la pasul 7
        local_counter=0
        while U0>=U1:

            steps_1+=1
            K=K+1
            local_counter+=1
            print(local_counter)
            U0=U1
            U1=random.uniform(0,1)
            if steps_1 > 1000:  # Add a limit to avoid infinite loop during debugging
                print("Breaking out of loop for debugging.")
                break

        if K%2==1:
            X=N+U_star
            break
        else:
            N+=1

    return X

how_many_executions=0
def generate_N4_2():
    #Generam variabila N(4,2) printr-o metoda de compunere-respingere
    #Generam variabila N(0,1)
    #Daca Y = N(m, gamma) atunci X = m + gamma*Y=> Daca il generam pe X il generam si pe Y, deci generam variabila N(0,1)
    #Apoi variabila N(4,2) unde m=4 si gamma=2
    #Pas 1: Generam U, uniform distribuita pe [0,1]
    #Pas 2: generam Y = Esp(1) = X de mai devreme
    what=0
    while True:
        X=generate_exp()
        Y=X
        e = math.exp(-Y**2/2+Y-0.5)

        U=np.random.uniform(0,1)
        #Pas 3: daca U <= e^(-Y^2/2+Y-0.5) mergem la pasul 4, altfel mergem la pasul 1, 
        if U<=e:#math.exp(-Y**2/2+Y-0.5) = e^(-Y^2/2+Y-0.5)
            break
        what+=1
        if what > 1000:
            print("Breaking out of loop for debugging.")
            break
    #Pas 4: X1=Y
    X1=Y
    #Pas 5: generam U, uniform distribuita pe [0,1]
    U=np.random.uniform(0,1)
    #Pas 6: daca U<=0.5 atunci s=1, altfel s=-1
    s=0
    if U<=0.5:
        s=1
    else:
        s=-1
    #Pas 7: X=X1*s
    X=X1*s


    m=4
    gamma=2
    N4_2 = m+gamma*X
    global how_many_executions
    how_many_executions+=1
    print(how_many_executions)
    return N4_2

def validate(nr_teste):

    #Media si dispersia pentru Exp(1)=1
    Exp1=[generate_exp() for _ in range(nr_teste)]
    #Calculam media de selectie
    media_selectie_exp=np.mean(Exp1)
    print("Media teoretica este: 1")
    print("Media de selectie este: ",media_selectie_exp)
    #Calculam dispersia de selectie
    dispersia_selectie_exp=np.var(Exp1)
    print("Dispersia teoretica este: 1")
    print("Dispersia de selectie este: ",dispersia_selectie_exp)

    #Media teoretica pentru N(4,2)=4
    #Dispersia teoretica pentru N(4,2)=4
    #Validam cu media si dispersia de selectie
    N4_2=[generate_N4_2() for _ in range(nr_teste)]
    #Calculam media de selectie
    media_selectie=np.mean(N4_2)
    print("Media teoretica este: 4")
    print("Media de selectie este: ",media_selectie)
    #Calculam dispersia de selectie
    dispersia_selectie=np.var(N4_2)
    print("Dispersia teoretica este: 4")
    print("Dispersia de selectie este: ",dispersia_selectie)
    with open("rezultate.txt", "w") as f:
        f.write(f"===== NUMARUL DE TESTE: {str(nr_teste)}" + " =====\n")
        f.write("Media teoretica este: 1\n")
        f.write(f"Media de selectie este: {str(media_selectie_exp)}" + "\n")
        f.write("Dispersia teoretica este: 1\n")
        f.write(f"Dispersia de selectie este: {str(dispersia_selectie_exp)}" + "\n")
        f.write("Media teoretica este: 4\n")
        f.write(f"Media de selectie este: {str(media_selectie)}" + "\n")
        f.write("Dispersia teoretica este: 4\n")
        f.write(f"Dispersia de selectie este: {str(dispersia_selectie)}" + "\n")

    #Histograma pentru Exp(1)
    plt.hist(Exp1, bins=100)
    plt.title("Histograma pentru Exp(1)")
    plt.xlabel("Valori")
    plt.ylabel("Frecventa")
    plt.savefig("histograma_exp.png")
    plt.show()

    #Histograma pentru N(4,2)
    plt.hist(N4_2, bins=100)
    plt.title("Histograma pentru N(4,2)")
    plt.xlabel("Valori")
    plt.ylabel("Frecventa")
    plt.savefig("histograma_N4_2.png")
    plt.show()


validate(100000)

