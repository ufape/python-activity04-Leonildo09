# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 4 - Problem 2
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Nas questões desse desse conjunto, você deverá escrever uma biblioteca chamada library_problem_2.py que contenha funções, separando a lógica do script principal, onde serão chamadas todas as funções.

Input(s):
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Processes:
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Output(s):
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Exemplo 1:
=-=-=-=-=-=-=-=-=-=
Digite o valor 1: 10
Digite o valor 2: 18
Os números são..: 12 13 17
=-=-=-=-=-=-=-=-=-=

"""

def resto_de_2_e_3(x,y):
    
    if x < y:
        for resto in range(x + 1, y):
            if resto % 5 == 2 or resto % 5 == 3:
                print(resto)

    else:
        for resto in range(y + 1, x):
            if resto % 5 == 2 or resto % 5 == 3:
                print(resto)
                
def main():
    x = int(input('Digite o valor de x: '))
    y = int(input('Digite o valor de y: '))

    resto_de_2_e_3(x,y)


if __name__ == '__main__':
    main()
