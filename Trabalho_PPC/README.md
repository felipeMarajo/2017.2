# Problema dos Babuínos atravessando o Cânion (Baboon Crossing problem)

## Descrição do problema:
A passagem ao longo da corda segue estas regras:
  - Vários babuínos podem atravessar o cânion ao mesmo tempo, desde que todos estejam indo no mesmo sentido.
  - Babuínos se movendo em sentidos contrários irão produzir um impasse (os babuínos ficarão presos no meio da corda), porque é impossível para um babuíno passar sobre o outro, enquanto estiver suspenso sobre o canyon. Estando no meio da corda os babuínos também não sabem voltar.
  - Quando um babuíno for atravessar o cânion, ele deve verificar se nenhum outro babuíno está atravessando no sentido oposto (deve esperar até a corda ficar livre).
Procure implementar uma solução que evite a fome (starvarion). Se um número grande de babuínos chegar em um lado do cânion, deve ser implementada uma política para permitir que os babuínos no sentido contrário possam atravessar. (alternar a oportunidade de travessia?)

A travessia também deve ser otimizada para evitar esperas muito longas (vários babuínos atravessando ao mesmo tempo).

## Implementação 
Simular cada babuíno como um processo separado.

Ao todo, 50 babuínos irão cruzar o cânion, com um gerador de números aleatórios especificando se estão se movendo para leste ou para oeste (com probabilidade igual).

Use um gerador de números aleatórios, de modo que o tempo entre chegada de babuínos ao cânion seja entre 1 e 8 segundos.

Cada babuíno leva um segundo para chegar na corda (isto é, o espaçamento inter-babuíno mínimo é 1 segundo).

Todos os babuínos atravessam na mesma velocidade. O percurso leva exatamente 4 segundos, após o babuíno chegar na corda.

Use semáforos ou monitor  para sincronização.

Durante a execução do programa  deve mostrar as filas para travessia.
 
Ao final da execução do programa deve ser exibido um relatório contendo:
  - Quantidade de babuínos para cada sentido.
  - Tempo médio de espera para atravessar (tempo de espera + travessia).
  - Taxa de aproveitamento da corda (tempo em uso / tempo total).
