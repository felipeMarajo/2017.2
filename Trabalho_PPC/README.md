# Problema dos Babuínos atravessando o Cânion (Baboon Crossing problem)#

# Descrição do problema:#
A passagem ao longo da corda segue estas regras:
  - Vários babuínos podem atravessar o cânion ao mesmo tempo, desde que todos estejam indo no mesmo sentido.
  - Babuínos se movendo em sentidos contrários irão produzir um impasse (os babuínos ficarão presos no meio da corda), porque é impossível para um babuíno passar sobre o outro, enquanto estiver suspenso sobre o canyon. Estando no meio da corda os babuínos também não sabem voltar.
  - Quando um babuíno for atravessar o cânion, ele deve verificar se nenhum outro babuíno está atravessando no sentido oposto (deve esperar até a corda ficar livre).
Procure implementar uma solução que evite a fome (starvarion). Se um número grande de babuínos chegar em um lado do cânion, deve ser implementada uma política para permitir que os babuínos no sentido contrário possam atravessar. (alternar a oportunidade de travessia?)

A travessia também deve ser otimizada para evitar esperas muito longas (vários babuínos atravessando ao mesmo tempo).
