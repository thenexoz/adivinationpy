#coding: utf-8
"""
    Jogo de Adivinhação Numérica - Versão 0.1
    Contém:
        -Pergunta a identidade do Jogador(Nome);
        -Sistema de Dificuldade;
        -Aposta do Jogador;

    Proxima atualização:
        -Sistema de Repetição do Jogo;
        -Interface mais trabalhada;
"""
#Importação da biblioteca randomica do Python e todas as suas funções
from random import *

nome = input("Olá, como e que se chama? ")
print("\n***Seja bem-vindo ao jogo de adivinhação {name}***\n".format(name=nome))
print("*** Seleccione a dificuldade que pertende! ***")
print("* 1 - Fácil\n* 2 - Intermédio\n* 3 - Avançado\n")

dificuldadeEscolhida = input("Escolha de acordo com as opçoes acima: ")

#Estrutura Condicional (Dificuldade)
if (dificuldadeEscolhida == '1'):
    numeroSecreto = randint(1, 30)
    print("O numero secreto vai variar entre 1 e 30!")
elif (dificuldadeEscolhida == '2'):
    numeroSecreto = randint(1, 75)
    print("O numero secreto vai variar entre 1 e 75!")
elif (dificuldadeEscolhida == '3'):
    numeroSecreto = radint(1, 150)
    print("O numero secreto vai variar entre 1 e 150!")
else:
    print("Nao digitou uma opção válida!")

print("\n")

print("Agora que já escolheu a dificuldade (",dificuldadeEscolhida,") está na hora de jogar. Boa sorte", nome,"!")
errou = False
#Estrutura Condicional (Aposta)
while errou == False:
	apostaJogador = int(input("Digite a sua aposta: "))
	print(numeroSecreto)
	if (apostaJogador == numeroSecreto):
		print("Parabens! A sua aposta está correta!!")
		errou = True
	elif (apostaJogador >= numeroSecreto):
		print("A sua aposta foi maior que o numero secreto!")
	elif (apostaJogador <= numeroSecreto):
		print("A sua aposta foi menor que o numero secreto!")

"""
    ZONA DE CRÉDITOS || PROGRAMADORES DO PROJETO:

        -Bryan Rodrigues(Mentor do Projeto);
"""
