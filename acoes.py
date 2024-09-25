# Módulo para Gerenciar Tarefas Relacionadas ao Trem

# Importando os Módulos Necessários
import pyodbc
import os
import datetime
import time
import random

# Definindo as Tarifas por Km para Cada Classe
tarifa_sleeper = 1.5
tarifa_terceira_ac = 2
tarifa_segunda_ac = 3
tarifa_primeira_ac = 4

# Definindo Variáveis Iniciais
data_atual = datetime.date.today()

# Um Bilhete pode ser Reservado com 4 Meses de Antecedência
data_maxima = data_atual + datetime.timedelta(days=120)

# Funções

def listar_trens():
    """
    listar_trens() -> Exibe a Lista de Trens Disponíveis conforme a Solicitação do Usuário
    """

    conexao = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-LMQCQ2J\\MSSQLSERVER1;'
        'DATABASE=trem;'
        'Trusted_Connection=yes;'
    )
    cursor = conexao.cursor()

    print("Busque Inserindo os Códigos das Estações!")
    partida = input("De: ")
    destino = input("Para: ")
    data = input("Data(YYYY-MM-DD): ")
    data_usuario = datetime.datetime.strptime(data, "%Y-%m-%d").date()
    
    while data_usuario < data_atual or data_usuario > data_maxima:
        print("Por favor, insira uma Data Válida!")
        data = input("Data(YYYY-MM-DD): ")
        data_usuario = datetime.datetime.strptime(data, "%Y-%m-%d").date()

    cursor.execute(
        'SELECT Numero_Trem, Nome_Estacao_Origem, Nome_Estacao_Destino, Hora_Partida, Hora_Chegada '
        'FROM train_info WHERE Codigo_Estacao_Origem = ? AND Codigo_Estacao_Destino = ?',
        (partida, destino)
    )

    resultado = cursor.fetchall()
    os.system("cls")
    time.sleep(1)
    cabecalho = ["Numero_Trem", "Nome_Estacao_Origem", "Nome_Estacao_Destino", "Hora_Partida", "Hora_Chegada"]

    if len(resultado) >= 10:
        try:
            print("Total de", len(resultado), "Registros Encontrados!")
            qtd = int(input("Digite o Número de Registros que deseja Ver: "))
        except ValueError:
            print("Por favor, insira um Número Inteiro Válido!")
        else:
            print(cabecalho)
            print(" ")
            for x in range(qtd):
                print(resultado[x], "\n")
    elif len(resultado) == 0:
        print("Nenhum Trem Disponível!")
    else:
        print(cabecalho)
        print(" ")
        for x in resultado:
            print(x, "\n")

    cursor.close()
    conexao.close()

def verificar_tarifa():
    """
    verificar_tarifa() -> Calcula a Tarifa com Base na Distância
    """

    conexao = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-LMQCQ2J\\MSSQLSERVER1;'
        'DATABASE=trem;'
        'Trusted_Connection=yes;'
    )
    cursor = conexao.cursor()

    print("Busque Inserindo o Código da Estação!")

    cabecalho = [("Train_No", "Distance", "Sleeper", "Third_AC", "Second_AC", "First_AC")]
    partida = input("De: ").strip()
    destino = input("Para: ").strip()


    cursor.execute(
        'SELECT Numero_Trem, Distancia FROM train_info WHERE Codigo_Estacao_Origem = ? AND Codigo_Estacao_Destino = ?',
        (partida, destino)
    )

    resultado_tarifa = cursor.fetchall()
    time.sleep(1)
    os.system("cls")

    if len(resultado_tarifa) >= 10:
        try:
            print("Total de", len(resultado_tarifa), "Registros Encontrados!")
            qtd = int(input("Digite o Número de Registros que deseja Ver: "))
        except ValueError:
            print("Por favor, insira um Número Inteiro Válido!")
        else:
            print(cabecalho)
            print(" ")
            for x in range(qtd):
                y = resultado_tarifa[x]
                print(resultado_tarifa[x], "Rs.", int(y[1]) * tarifa_sleeper, "Rs.", int(y[1]) * tarifa_terceira_ac,
                      "Rs.", int(y[1]) * tarifa_segunda_ac, "Rs.", int(y[1]) * tarifa_primeira_ac, "\n")
    elif len(resultado_tarifa) == 0:
        print("Nenhum Trem Disponível!")
    else:
        print(cabecalho)
        print(" ")
        for x in resultado_tarifa:
            print(x, "Rs.", int(x[1]) * tarifa_sleeper, "Rs.", int(x[1]) * tarifa_terceira_ac, 
                  "Rs.", int(x[1]) * tarifa_segunda_ac, "Rs.", int(x[1]) * tarifa_primeira_ac, "\n")

    cursor.close()
    conexao.close()

def exibir_reservas():
    """
    exibir_reservas() -> Mostra as Reservas Feitas pelo Usuário
    """

    conexao = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-LMQCQ2J\\MSSQLSERVER1;'
        'DATABASE=trem;'
        'Trusted_Connection=yes;'
    )
    cursor = conexao.cursor()

    numero_celular = input("Por favor, insira seu Número de Celular com 11 Dígitos: ")

    cursor.execute('SELECT * FROM bookings1 WHERE Numero_Telefone = ?', (numero_celular,))


    resultado = cursor.fetchall()
    if len(resultado) == 0:
        print("Nenhum Registro Encontrado!")
    else:
        numero_reserva = 1
        print(["Numero_Trem", "Nome_Passageiro", "Numero_Telefone", "Numero_cpf", "Data_Reserva", "Booking_ID", "Classe"])
        for x in resultado:
            print("RESERVA NO", numero_reserva, ":", x, "\n")
            numero_reserva += 1

    cursor.close()
    conexao.close()

def reservar_trem():
    """
    reservar_trem() -> Permite que o Usuário Reserve um Trem
    """

    conexao = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-LMQCQ2J\\MSSQLSERVER1;'
        'DATABASE=trem;'
        'Trusted_Connection=yes;'
    )
    cursor = conexao.cursor()
    while True:
        try:
            numero_trem = int(input("Número do Trem: "))
        except ValueError:
            print("Por favor, insira um Número de Trem Válido!")
            continue
        else:
            break

    while True:
        nome = input("Digite seu Nome: ")
        if len(nome) == 0:
            print("Por favor, insira um Nome!")
        elif len(nome) > 30:
            print("Nome muito Longo!")
        else:
            break

    while True:
        try:
            celular = int(input("Digite seu Número de Celular: "))
        except ValueError:
            print("Por favor, insira um Número de Celular Válido!")
            continue
        else:
            if len(str(celular)) == 11 and celular != 0000000000:
                break
            elif len(str(celular)) > 11 or len(str(celular)) < 11:
                print("Por favor, insira um Número de Celular de 11 Dígitos Válido!")
            else:
                print("Por favor, insira um Número de Telefone Válido!")

    while True:
        try:
            adhaar = int(input("Digite seu Número de CPF: "))
        except ValueError:
            print("Por favor, insira um Número de CPF Válido!")
            continue
        else:
            if len(str(adhaar)) == 11 and adhaar != 000000000000:
                break
            elif len(str(adhaar)) > 11 or len(str(adhaar)) < 11:
                print("Por favor, insira um Número de CPF de 11 Dígitos Válido!")
            else:
                print("Por favor, insira um Número de CPF Válido!")

    hora_reserva = datetime.datetime.now()
    data_reserva = hora_reserva.date()
    data_reserva = data_reserva.strftime("%d-%m-%y")

    # Criando um ID Único para Cada Reserva
    id_reserva = random.randint(1, 10000)
    cursor.execute("SELECT Booking_ID FROM BOOKINGS1")
    resultado = cursor.fetchall()
    ids_usados = [x[0] for x in resultado]
    
    while id_reserva in ids_usados:
        id_reserva = random.randint(1, 10000)

    print(["Sleeper", "AC-1", "AC-2", "AC-3"])
    classe = None
    while True:
        escolha = input("Por favor, insira uma Classe das opções fornecidas acima: ")
        if escolha == "Sleeper":
            classe = "Sleeper"
            break
        elif escolha == "AC-1":
            classe = "AC-1"
            break
        elif escolha == "AC-2":
            classe = "AC-2"
            break
        elif escolha == "AC-3":
            classe = "AC-3"
            break
        else:
            print(["Sleeper", "AC-1", "AC-2", "AC-3"])
            print("Por favor, escolha uma Opção das opções Acima!")

    while True:
        confirmacao = input("Você tem certeza que deseja Reservar (Y/N): ")
        if confirmacao in ["Y", "y"]:
            print("Reservando...")
            try:
                query = "INSERT INTO bookings1 VALUES({}, '{}', '{}', '{}', '{}', {}, '{}')".format(
                    numero_trem, nome, celular, adhaar, data_reserva, id_reserva, classe)
                cursor.execute(query)
            except Exception as e:
                print("Erro na Reserva:", e)
            else:
                print("Reservado com Sucesso!")
                conexao.commit()
                cursor.close()
                conexao.close()
                break
        elif confirmacao in ["N", "n"]:
            print("Cancelando a Reserva...")
            time.sleep(0.5)
            os.system("cls")
            break
        else:
            print("Por favor, insira Y (Sim) ou N (Não)!")

def cancelar_reserva():
    """
    cancelar_reserva() -> Permite que um Usuário Cancele a Reserva
    """

    conexao = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-LMQCQ2J\\MSSQLSERVER1;'
        'DATABASE=trem;'
        'Trusted_Connection=yes;'
    )
    cursor = conexao.cursor()

    print("Por favor, use a opção Mostrar Minhas Reservas\n para obter o ID Único da Reserva que deseja Cancelar!")

    while True:
        try:
            id_unico = int(input("Digite o ID Único: "))
        except ValueError:
            print("Por favor, insira um ID Válido!")
        else:
            if id_unico < 1 or id_unico > 10000:
                print("ID fora do Intervalo!")
            else:
                cursor.execute("SELECT * FROM bookings1 WHERE Booking_ID={}".format(id_unico))
                resultado = cursor.fetchall()
                if len(resultado) == 0:
                    print("Nenhum Registro Encontrado!")
                    break
                print(["Numero_Trem", "Nome_Passageiro", "Numero_Telefone", "Numero_cpf", "Data_Reserva", "Booking_ID"])
                for x in resultado:
                    print(x)
                while True:
                    confirmacao = input("Você tem certeza que deseja Cancelar (Y/N): ")
                    if confirmacao in ["Y", "y"]:
                        cursor.execute("DELETE FROM bookings1 WHERE Booking_ID={}".format(id_unico))
                        print("Reserva Cancelada!")
                        conexao.commit()
                       
                        break
                    elif confirmacao in ["N", "n"]:
                        break
                    else:
                        print("Por favor, insira Y (Sim) ou N (Não)!")
                break

    cursor.close()
    conexao.close()
