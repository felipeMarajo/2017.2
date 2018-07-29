from collections import deque
import threading

smpFila_L = threading.Semaphore()
smpFila_O = threading.Semaphore()

class Rope():
    def __init__(self, direcao):
        self.direcao = direcao          # Direção da corda
        self.corda = deque(maxlen=4)    # Tamanho maximo da corda
        self.tempoRopeI = None          # Tempo de utilização
        self.tempoRopeF = None
        self.qntL = 0                   # Variavel para controle
        self.qntO = 0                   # Variavel para controle
