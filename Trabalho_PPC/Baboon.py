import random
import threading
from _datetime import datetime
import time, timeit
import sys
import Listas
import Rope


"""Semáforos para: corda com quatro posições, direção da corda e um que impede que o lado oposto entre na corda(semsubir).
Semáforo para a contadores (sqntL/sqntO) e por último dois semáforos para os babuínos acessarem a fila (smpL/smpO)"""
semCorda = threading.Semaphore(4)
semDirecao = threading.Semaphore()
semsubir = threading.Semaphore()

sqntL = threading.Semaphore()       # Semaforos para os contadores da corda para saber se ainda tem babuíno na corda
sqntO = threading.Semaphore()

smpL = threading.Semaphore()        # Semáforos para chegar na corda (Fila ativa)
smpO = threading.Semaphore()

"""Instanciando uma corda"""
rope = Rope.Rope(None)

"""Objeto thread, class que herda os métodos de thread"""
class Babuino(threading.Thread):
    def __init__(self, tempo):
        threading.Thread.__init__(self)
        self.sentido_movimentacao = None        # Leste ou Oeste

        direcoes = ['Leste', 'Oeste']           # Sorteio direção
        self.sentido_movimentacao = random.choice(direcoes)

        self.tempo_chegada_canyon = tempo       # Entre 1 e 8 segundos
        self.tempo_inicio = None                # Tempo em que babuíno chegou na fila
        self.tempo_fim = None                   # Tempo que o babuíno saiu da corda

    """Método que faz a atravessia dos babuínos, este método é executado por cada babuíno"""
    def subir_corda(self):

        """ Esta condição é executada apenas uma fez durante todo o código, pois será usada apenas para o primeiro
            babuíno que estiver subindo na corda. A corda inicia com a direção setada como None"""
        semsubir.acquire()                  # Semáforo para ordem de subina na corda Leste/Oeste
        if rope.direcao == None:

            semsubir.release()              # Adquire o semaforo para subir na corda

            semDirecao.acquire()            # Adquire semáforo para alterar a direção
            rope.direcao = self.sentido_movimentacao

            time.sleep(1)

            sys.stdout.write("Sentido corda : " + rope.direcao + "\n")
            sys.stdout.flush()

            semCorda.acquire()              # Adquire uma posição do semáforo corda

            sys.stdout.write(str(self.name) + " entrou na corda \n")
            sys.stdout.flush()

            rope.tempoRopeI = timeit.default_timer()   # Guarda tempo inicial em q a corda foi usada

            if self.sentido_movimentacao == "Leste":
                sqntL.acquire()
                rope.qntL += 1
                sqntL.release()
            else:                        # Incrementa os contadores de leste/oeste adquirindo e liberando seus semáforos
                sqntO.acquire()
                rope.qntO += 1
                sqntO.release()

            time.sleep(4)

            sys.stdout.write(str(self.name) + " e saiu da corda \n")
            sys.stdout.flush()

            semCorda.release()              #Libera uma posição da corda

            if self.sentido_movimentacao == "Leste":
                sqntL.acquire()
                rope.qntL -= 1
                sqntL.release()
                                            #Decrementa os contadores Leste/Oeste (Qnt de babuínos na corda)
            else:
                sqntO.acquire()
                rope.qntO -= 1
                sqntO.release()

            if rope.direcao =="Leste" and rope.qntL == 0:
                rope.tempoRopeF = timeit.default_timer()  # Guarda tempo final em que a corda foi usada
                aux = rope.tempoRopeF - rope.tempoRopeI
                print(aux)
                Listas.tempo_Corda.append(aux)
                semDirecao.release()
            elif rope.direcao == "Oeste" and rope.qntO == 0:
                rope.tempoRopeF = timeit.default_timer()
                aux = rope.tempoRopeF - rope.tempoRopeI
                print(aux)
                Listas.tempo_Corda.append(aux)
                semDirecao.release()

            """Esta condição diz que se o proximo babuíno que tenta subir na corda for da mesma direção ele não precisará
            adquirir o semáforo
            """
        elif rope.direcao == self.sentido_movimentacao:

            time.sleep(1)
            semsubir.release()

            semCorda.acquire()              # Adiquire o semaforo corda

            sys.stdout.write(str(self.name) + " entrou na corda \n")
            sys.stdout.flush()

            if self.sentido_movimentacao == "Leste":
                sqntL.acquire()
                rope.qntL += 1
                sqntL.release()
            else:                           # Faz os incrementos em qntL/qntO dentro de uma região critica
                sqntO.acquire()
                rope.qntO += 1
                sqntO.release()

            time.sleep(4)                   # Tempo em que o babuíno fica na corda

            sys.stdout.write(str(self.name) + " saiu da corda \n")
            sys.stdout.flush()

            semCorda.release()              # Libera o semáforo da corda

            if self.sentido_movimentacao == "Leste":
                sqntL.acquire()
                rope.qntL -= 1
                sqntL.release()
                                            # Decrementa os contadores Leste/Oeste (Qnt de Babuínos na corda )
            else:
                sqntO.acquire()
                rope.qntO -= 1
                sqntO.release()

            if rope.direcao =="Leste" and rope.qntL == 0:   # Se a corda estiver vazia então libera a direção
                rope.tempoRopeF = timeit.default_timer()    # captura o tempo que o babuíno saiu da corda
                aux = rope.tempoRopeF - rope.tempoRopeI     # Subtração do tempo final - inicial
                print(aux)
                Listas.tempo_Corda.append(aux)              # Add o tempo do babuíno na lista de tempos
                semDirecao.release()                        # Semáforo direção é liberado

            elif rope.direcao == "Oeste" and rope.qntO == 0:
                rope.tempoRopeF = timeit.default_timer()
                aux = rope.tempoRopeF - rope.tempoRopeI
                print(aux)
                Listas.tempo_Corda.append(aux)
                semDirecao.release()

            """Esta condição altera o sentido da corda, se o babuíno que chegou primeiro for do outro sentido"""
        else:

            semDirecao.acquire()                            # Adquire o semaforo direção
            rope.direcao = self.sentido_movimentacao        # Altera a direção da corda para a direção do babuíno atual

            #sys.stdout.write("\033[31mSentido corda : " + rope.direcao + "\033[m\n")
            sys.stdout.write("Sentido corda : " + rope.direcao + "\n")
            sys.stdout.flush()

            time.sleep(1)
            semsubir.release()                              # Libera o semáforo para subir na corda

            semCorda.acquire()                              # Semaforo é adquirido

            sys.stdout.write(str(self.name) + " entrou na corda \n")
            sys.stdout.flush()

            rope.tempoRopeI = timeit.default_timer()  # Captura o tempo inicial da corda


            if self.sentido_movimentacao == "Leste":
                sqntL.acquire()
                rope.qntL+=1
                sqntL.release()
            else:                                           # Incrementa o contador (Quantidade de babuínos na corda)
                sqntO.acquire()
                rope.qntO += 1
                sqntO.release()

            time.sleep(4)

            sys.stdout.write(str(self.name) + " saiu da corda \n")
            sys.stdout.flush()

            semCorda.release()                              # Semáforo da corda liberado

            if self.sentido_movimentacao == "Leste":
                sqntL.acquire()
                rope.qntL -= 1
                sqntL.release()
                                                            # Decrementa o contador
            else:
                sqntO.acquire()
                rope.qntO -= 1
                sqntO.release()

            if rope.direcao == "Leste" and rope.qntL == 0:  # Se a corda estiver vazia
                rope.tempoRopeF = timeit.default_timer()    # Pega o tempo final da corda
                aux = rope.tempoRopeF - rope.tempoRopeI     # Subtração do tempo fina e inicial da corda
                print(aux)
                Listas.tempo_Corda.append(aux)              # Add a subtração em um lista
                semDirecao.release()                        # Libera o semaforo direção
            elif rope.direcao == "Oeste" and rope.qntO == 0:
                rope.tempoRopeF =  timeit.default_timer() #timeit.default_timer()
                aux = rope.tempoRopeF - rope.tempoRopeI
                print(aux)
                Listas.tempo_Corda.append(aux)
                semDirecao.release()


    def run(self):
        """ As próximas condições faz o babuíno ir para a fila leste ou oeste"""
        self.tempo_chegada_canyon = random.randint(1, 8)        # Escolhe um numero de 1 a 8

        if self.sentido_movimentacao == "Leste":
            smpL.acquire()                                          # Adquire semaforo leste
        else:
            smpO.acquire()                                          # Adquire semáforo oeste

        self.tempo_inicio = timeit.default_timer()                  # Adquire o tempo inicial de espera babuíno

        if Listas.l_canyon == None and self.sentido_movimentacao == "Leste":
            sys.stdout.write(str(self.name) + " entrou na fila " + str(self.sentido_movimentacao) + "\n")
            sys.stdout.flush()

            Listas.l_canyon = str(self.name)+ " Tempo "+ str(self.tempo_chegada_canyon) # Salva fila formada

            smpL.release()                                          # Semáforo lado leste é liberado

        elif Listas.o_canyon == None and self.sentido_movimentacao == "Oeste":
            sys.stdout.write(str(self.name) + " entrou na fila " + str(self.sentido_movimentacao) + "\n")
            sys.stdout.flush()
            Listas.o_canyon = str(self.name)+ " Tempo "+ str(self.tempo_chegada_canyon) # Salva fila formada

            smpO.release()                                          # Semáforo lado oeste liberado
        else:
            time.sleep(self.tempo_chegada_canyon)
            self.tempo_inicio = timeit.default_timer()
            sys.stdout.write(str(self.name) + " Esperou "+ str(self.tempo_chegada_canyon)+ "s "+ "entrou na fila "+ str(self.sentido_movimentacao)+"\n")
            sys.stdout.flush()

            if self.sentido_movimentacao == "Leste":                # As duas proximas condições salva as filas formadas

                Listas.l_canyon = str(Listas.l_canyon) + " | " + str(self.name) + " Tempo " + str(
                    self.tempo_chegada_canyon)
            else:                                                   # Add os babuínos nas suas respectivas filas
                Listas.o_canyon = str(Listas.o_canyon) + " | " + str(self.name) + " Tempo " + str(
                    self.tempo_chegada_canyon)

            if self.sentido_movimentacao == "Leste":
                smpL.release()
            else:                                                   # Libera os  respectivos semáforos das filas leste e oeste
                smpO.release()

        self.subir_corda()                                          # Função para o babuíno atravessar a corda

        self.tempo_fim = timeit.default_timer()                     # guarda o tempo do babuíno quando sai da corda

        aux = self.tempo_fim - self.tempo_inicio                    # Subtrai tempo inicial e tempo final babuíno

        Listas.tempos_de_espera.append(aux)                         # Add o tempo de espera em uma lista