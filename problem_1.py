# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 4 - Problem 1
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Nas questões desse desse conjunto, você deverá escrever uma biblioteca chamada library_problem_1.py que contenha funções, separando a lógica do script principal, onde serão chamadas todas as funções.

Input(s):
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

Processes:
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

Output(s):
Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema.

Exemplo 1:
=-=-=-=-=-=-=-=-=-=
Digite a nota 1: 2.0
Digite a nota 2: 4.0
Digite a nota 3: 7.5
Digite a nota 4: 8.0
Media: 5.4
Aluno em exame.
Digite a nota do exame: 6.4
Aluno aprovado.
Media final: 5.9
=-=-=-=-=-=-=-=-=-=

Exemplo 2:
=-=-=-=-=-=-=-=-=-=
Digite a nota 1: 2.0
Digite a nota 2: 6.5
Digite a nota 3: 4.0
Digite a nota 4: 9.0
Media: 4.8
Aluno reprovado.
=-=-=-=-=-=-=-=-=-=

Exemplo 3:
=-=-=-=-=-=-=-=-=-=
Digite a nota 1: 9.0
Digite a nota 2: 4.0
Digite a nota 3: 8.5
Digite a nota 4: 9.0
Media: 7.3
Aluno aprovado.
=-=-=-=-=-=-=-=-=-=

"""

def calcular_media_ponderada(n1, n2, n3, n4):
    
    media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10
    return media


def verificar_situacao_aluno(media):
    
    if media >= 7.0:
        return "Aluno aprovado."
    elif media < 5.0:
        return "Aluno reprovado."
    else:
        return "Aluno em exame."


def calcular_media_final(media_anterior, nota_exame):
    
    media_final = (media_anterior + nota_exame) / 2
    return media_final
    
def main():
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    n4 = float(input("Digite a nota 4: "))

    
    media = calcular_media_ponderada(n1, n2, n3, n4)
    print(f"Media: {media:.1f}")

    
    situacao = verificar_situacao_aluno(media)
    print(situacao)

    if situacao == "Aluno em exame.":
        
        nota_exame = float(input("Digite a nota do exame: "))
        
        media_final = calcular_media_final(media, nota_exame)
        print(f"Aluno {'aprovado' if media_final >= 5.0 else 'reprovado'}.")
        print(f"Media final: {media_final:.1f}")


if __name__ == '__main__':
    main()
