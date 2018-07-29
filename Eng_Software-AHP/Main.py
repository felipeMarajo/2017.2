import sys
sys.path.insert(0,'/Interface/')
from Interface import Janela_1
#from Interface.Janela_1 import *
from Interface import Janela_2, janela_3
from Interface import warning
from PyQt5 import QtCore, QtGui, QtWidgets
import functools
# Imports da Main
#------------------------------------------------------------
"""Captura o objetivo que o usuário digitou e
    armazena em uma lista"""
def cadastrar_Objetivo():
    objetivo = Janela_1.ui.writeObjetivo.text()
    print(objetivo)
    return objetivo

"""Captura os critérios que o usuário digitou 
    e armazena em uma lista"""
def cadastrar_Criterio():
    remover = ""
    aux = Janela_1.ui.writeCriterio.text()
    criterios = aux.split("-")
    while remover in criterios:
        criterios.remove(remover)
    print(criterios)
    return criterios

"""Captura as atividades que o usuário digitou
    e armazena em uma lista"""
def cadastrar_Atividade():
    remover = ""
    aux = Janela_1.ui.writeAtividades.text()
    atividades = aux.split("-")
    while remover in atividades:
        atividades.remove(remover)
    print(atividades)
    return atividades

"""Chama as funções de cadastro e inicia a janela de aviso
    ou a próxima janela"""
def cadastrar():
    cadastrar_Objetivo()
    crit = cadastrar_Criterio()
    objetivo = cadastrar_Objetivo()
    ativ = cadastrar_Atividade()

    msg = None
    if len(crit) <= 2 or len(ativ) <= 2:
        msg = "Número de critério ou atividades\n \tinsuficientes"
    elif len(crit) > 15 or len(ativ) > 15:
        msg = "Número de critério ou atividades\n \tmaior que 15"

    if (len(crit) <= 2 or len(crit) > 15) or (len(ativ) <= 2 or len(ativ) > 15):
        warning.MainWindow = QtWidgets.QMainWindow()
        warning.ui = warning.Ui_MainWindow()
        warning.ui.setupUi(warning.MainWindow, msg)

        warning.MainWindow.show()
        warning.ui.pushButton.clicked.connect(functools.partial(warning.MainWindow.close))

    else:
        Janela_2.MainWindow = QtWidgets.QMainWindow()
        Janela_2.ui = Janela_2.Ui_MainWindow()
        Janela_2.ui.setupUi(Janela_2.MainWindow, crit, ativ, objetivo)

        Janela_2.MainWindow.show()

        Janela_2.ui.pushButton.clicked.connect(functools.partial(Janela_2.ui.preencher_Criterio))
        Janela_2.ui.pushButton_2.clicked.connect(functools.partial(Janela_2.ui.central_funcao))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Janela_1.MainWindow = Janela_1.QtWidgets.QMainWindow()
    Janela_1.ui = Janela_1.Ui_MainWindow()
    Janela_1.ui.setupUi(Janela_1.MainWindow)
    Janela_1.MainWindow.show()

    Janela_1.ui.pushButton.clicked.connect(functools.partial(cadastrar))
    sys.exit(app.exec_())
