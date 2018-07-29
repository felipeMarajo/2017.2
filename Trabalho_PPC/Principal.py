# coding:utf-8
from Baboon import Babuino
import random
import Listas
import sys
import timeit

"""Cria os 50 babuínos"""
def Criar_baboon():
    field = []
    Qmax = random.randint(24, 27)
    auxL = 0
    auxO = 0
    while not len(field) == 50:
        babuino = Babuino(None)
        if auxL == Qmax:
            if babuino.sentido_movimentacao == "Leste":
                babuino.sentido_movimentacao = "Oeste"
                field.append(babuino)
            else:
                field.append(babuino)
        elif auxO == Qmax:
            if babuino.sentido_movimentacao == "Oeste":
                babuino.sentido_movimentacao = "Leste"
                field.append(babuino)
            else:
                field.append(babuino)
        else:
            if babuino.sentido_movimentacao == "Leste":
                field.append(babuino)
                auxL += 1
            else:
                field.append(babuino)
                auxO += 1

    return field


def relatorio(campo, time_total):
    print("============================================")
    print("Babuinos Leste")
    sys.stdout.write(Listas.l_canyon)
    sys.stdout.flush()
    print("\n----------------------")

    print("\nBabuinos Oeste")
    sys.stdout.write(Listas.o_canyon)
    sys.stdout.flush()

    print("\n\n============== RELATÓRIO =================")
    qntL = 0
    qntO = 0
    for i in range(len(campo)):
        if campo[i].sentido_movimentacao == "Leste":
            qntL += 1
        else:
            qntO += 1
    print("Quantidade de Babuínos Leste: ", qntL)
    print("Quantidade de babuínos Oeste: ", qntO)

    aux = 0
    for i in range(len(Listas.tempos_de_espera)):
        aux = aux + Listas.tempos_de_espera[i]
    aux = aux/len(Listas.tempos_de_espera)
    sys.stdout.write("\nTempo médio de espera: " + str(aux)+ " s"+ "\n")
    sys.stdout.flush()

    aux2 = 0
    for i in range(len(Listas.tempo_Corda)):
        aux2 = aux2 + Listas.tempo_Corda[i]
    print("Tempo da corda: ", aux2)
    aux2 = aux2/time_total
    sys.stdout.write("\nTaxa de aproveitamento: " + str(aux2)+ " ou "+ str(aux2*100) +"%" +"\n")
    sys.stdout.flush()
    print("==========================================")

def inicio(principio):
# Vetor com todos os babuínos
    campo = Criar_baboon()
#Iniciar Treads
    print("=================================================")
    for i in range(len(campo)):
        campo[i].start()

    for i in range(len(campo)):
        campo[i].join()

    extincao = timeit.default_timer()  # guarda o tempo final do programa
    time = extincao - principio
    print("Tempo total do programa: ", time)
    relatorio(campo, time)

if __name__ == "__main__":
    principio = timeit.default_timer()  # guarda o tempo do inicio do programa
    inicio(principio)