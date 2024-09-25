# Este módulo contém algumas funções comuns utilizadas no sistema

# Importando os módulos necessários
import os
import time

# Funções

def sobre():
    """
    sobre() -> Exibe as informações sobre o sistema na tela.

    Parâmetros -> Nenhum
    """
    # Altere o caminho abaixo para o caminho absoluto do arquivo README
    try:
        with open(r"C:\Users\User\Documents\portfolio\reservatrem\read.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo README não encontrado. Verifique o caminho e tente novamente.")

def limpar_tela():
    """
    limpar_tela() -> Limpa a tela do terminal.

    Parâmetros -> Nenhum
    """
    print("Limpando a tela...")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

def exibir_menu(opcao="Sim"):
    """
    exibir_menu() -> Mostra o menu de opções ao usuário.

    Parâmetros -> opcao (Escolha do usuário para mostrar o menu, padrão é "Sim")
    """
    if opcao in ["Sim", "S"]:
        print("  BEM-VINDO AO SISTEMA DE RESERVAS DE TRENS")
        print("1. Comprar uma Passagem")
        print("2. Cancelar uma Reserva")
        print("3. Verificar Tarifas")
        print("4. Exibir Minhas Reservas")
        print("5. Exibir Trens Disponíveis")
        print("6. Limpar Tela")
        print("7. Exibir Menu")
        print("8. Sobre o Sistema")
        print("9. Sair")
    else:
        print("Opção inválida. Tente novamente.")
        pass
