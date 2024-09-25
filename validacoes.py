# Este módulo contém as funções que verificam os requisitos do projeto

# Importando os módulos necessários
import pyodbc
import sistema.dados as Inserir

# Funções

def verificar_banco_dados():
    """
    verificar_banco_de_dados() -> Verifica se o banco de dados necessário existe ou não.

    Parâmetros -> Nenhum
    """

    print("Verificando os requisitos do banco de dados...")

    try:
        conexao = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-LMQCQ2J\\MSSQLSERVER1;'
            'DATABASE=trem;'
            'Trusted_Connection=yes;'
        )
        cursor = conexao.cursor()
        resultado = None

        try:
            cursor.execute("USE trem;")
        except pyodbc.ProgrammingError:
            print("Banco de dados não existe!")
            resultado = False
        else:
            resultado = True

        if resultado:
            print("Banco de dados encontrado!")

            # Verificando se há tabelas no banco de dados
            cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';")
            table_count = cursor.fetchone()[0]

            if table_count == 0:
                print("Nenhuma tabela encontrada. Criando as tabelas necessárias...")
                criar_tabelas()
            else:
                print(f"{table_count} tabelas encontradas. Nenhuma nova tabela será criada.")
        else:
            print("Criando o banco de dados e as tabelas necessárias...")
            cursor.execute("CREATE DATABASE trem;")
            cursor.execute("USE trem;")
            criar_tabelas()
            print("Banco de dados e tabelas criados com sucesso!")

        cursor.close()
        conexao.close()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    except pyodbc.Error as erro:
        print(f"Erro ao conectar ao SQL Server: {erro}")
        return False

def criar_tabelas():
    """
    criar_tabelas() -> Cria todas as tabelas necessárias para o projeto.

    Parâmetros -> Nenhum
    """

    try:
        conexao = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-LMQCQ2J\\MSSQLSERVER1;'
            'DATABASE=trem;'
            'Trusted_Connection=yes;'
        )
        cursor = conexao.cursor()

        cursor.execute(
            """
            CREATE TABLE train_info (
                Numero_Trem VARCHAR(10) NOT NULL, 
                Codigo_Estacao VARCHAR(20) NOT NULL, 
                Nome_Estacao VARCHAR(30) NOT NULL, 
                Hora_Chegada VARCHAR(20) NOT NULL, 
                Hora_Partida VARCHAR(20) NOT NULL, 
                Distancia VARCHAR(10) NOT NULL, 
                Codigo_Estacao_Origem VARCHAR(20) NOT NULL, 
                Nome_Estacao_Origem VARCHAR(70) NOT NULL, 
                Codigo_Estacao_Destino VARCHAR(20) NOT NULL, 
                Nome_Estacao_Destino VARCHAR(60) NOT NULL
            );
            """
        )

        cursor.execute(
            """
            CREATE TABLE bookings1 (
                Numero_Trem INT NOT NULL, 
                Nome_Passageiro VARCHAR(30) NOT NULL, 
                Numero_Telefone VARCHAR(11) NOT NULL, 
                Numero_cpf VARCHAR(11) NOT NULL, 
                Data_Reserva VARCHAR(20) NOT NULL, 
                Booking_ID INT NOT NULL, 
                Classe VARCHAR(20) NOT NULL
            );
            """
        )

        #Inserir.inserir_dados_trem()
        conexao.commit()
        cursor.close()
        conexao.close()
        Inserir.inserir_dados_trem()

    except pyodbc.Error as erro:
        print(f"Erro ao criar as tabelas: {erro}")

def validar_conexao():
    """
    testar_conexao() -> Verifica se a conexão com o servidor SQL está funcionando.

    Parâmetros -> Nenhum
    """

    try:
        print("Verificando a conexão com o servidor SQL Server...")

        conexao = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-LMQCQ2J\\MSSQLSERVER1;'
            'Trusted_Connection=yes;'
        )

        if conexao:
            info_servidor = conexao.getinfo(pyodbc.SQL_DBMS_VER)
            print("Conectado ao SQL Server, versão:", info_servidor)
            return True
        
                
        #conexao.close()

    except pyodbc.Error as erro:
        print("Erro ao conectar ao SQL Server. Verifique se o servidor está ativo e tente novamente.")
        print(f"Erro: {erro}")
        return False
