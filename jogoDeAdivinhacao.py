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

nome = input("Olá, como e que se chama?") 
print("Seja bem-vindo ao jogo de adivinhação", nome)

print("\n")

print("Seleccione a dificuldade que pertende...")
print("| (1) - Fácil | (2) - Intermédio | (3) - Avançado |")
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
apostaJogador = int(input("Digite a sua aposta: "))

#Estrutura Condicional (Aposta)
if (apostaJogador > numeroSecreto):
    print("A sua aposta foi maior que o numero secreto!")
elif (apostaJogador < numeroSecreto):
    print("A sua aposta foi menor que o numero secreto!")
else:
    print("Parabens! A sua aposta está correta!!")


"""
    ZONA DE CRÉDITOS || PROGRAMADORES DO PROJETO:

        -Bryan Rodrigues(Mentor do Projeto);
"""
