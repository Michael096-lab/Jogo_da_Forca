# Projeto 1 - Desenvolvimento de Game em Liguangem Python

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

# Função
def game(): # Função principal do jogo, onde se encontra quase toda a estrutura

    limpa_tela()

    print("\nBem-Vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo: \n")

    # Lista de palavras para o jogo
    # Aqui temos algumas somente para a primeira parte do jogo.
    palavras = ['banana', 'abacate', 'laranja', 'uva', 'morango']

    # Escolhe randomicamente uma palvra
    # A cada nova tentativa uma nova palavra é sorteada automaticamente
    palavra = random.choice(palavras)

    # List Comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances para tentar acertar a palavra
    chances = 6

    # Lista para as letras erradas.
    letras_erradas = []

    # Loop enquanto o número de chances for maior do que zero
    while chances > 0:

        # Print
        print("".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("\nLetras Erradas: ", "".join(letras_erradas))

        #  Tentativa
        tentativa = input("\nDigite uma letra: ").lower()
        print("")

        # Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            print("#" * 43)
            print(f"\nVocê venceu, a palavra era: {palavra} ")
            break
    # Condicional
    if "_" in letras_descobertas:
        print("#" * 43)
        print(f"\nVocê perdeu, a palavra era: {palavra} ")


# Bloco main
if __name__ == "__main__":
    game()
    print("\nAprendendo Programação Python com a DSA.:)\n")
    print("#" * 43)
