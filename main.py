# Script principal para lidar com interações do usuário e inicializar o sistema

# Importando os módulos necessários

import sistema.acoes as Acoes
import sistema.utilitarios as Util
import sistema.validacoes as Validar
from time import sleep

# Realizar as validações iniciais

# Validar a conexão com o banco de dados
conexao_bd = Validar.validar_conexao()
if not conexao_bd:
    quit()

Validar.verificar_banco_dados()

# Limpar a janela do console
Util.limpar_tela()

# Exibir o menu principal
Util.exibir_menu()



# Loop principal para lidar com as entradas do usuário

while True:
    opcao = input("Por favor, selecione uma opção: ")
    if opcao == "1":
        Acoes.reservar_trem()
    elif opcao == "2":
        Acoes.cancelar_reserva()
    elif opcao == "3":
        Acoes.verificar_tarifa()
    elif opcao == "4":
        Acoes.exibir_reservas()
    elif opcao == "5":
        Acoes.listar_trens()
    elif opcao == "6":
        Util.limpar_tela()
        Util.exibir_menu()
    elif opcao == "7":
        Util.exibir_menu()
    elif opcao == "8":
        Util.limpar_tela()
        Util.sobre()
        while True:
            voltar_menu = input("Deseja voltar ao menu? (S/N): ")
            if voltar_menu in ["S", "s"]:
                Util.exibir_menu()
                break
            elif voltar_menu in ["N", "n"]:
                break
            else:
                print("Por favor, insira S (Sim) ou N (Não).")
    elif opcao == "9":
        print("Encerrando todos os processos...")
        sleep(0.5)
        print("Até logo!")
        quit()
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
