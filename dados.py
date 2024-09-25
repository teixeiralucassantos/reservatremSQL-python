# Este módulo contém as funções para inserir dados nas tabelas do SQL Server

# Importando os módulos necessários
import csv
import pyodbc

# Funções

def inserir_dados_trem():
    """
    inserir_dados_trem() -> Insere todos os detalhes dos trens na tabela informacoes_trem.

    Parâmetros -> Nenhum
    """

    try:
        # Conectando ao SQL Server
        conexao = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-LMQCQ2J\\MSSQLSERVER1;'
            'DATABASE=trem;'
            'Trusted_Connection=yes;'
        )
        cursor = conexao.cursor()

        # Lendo o arquivo CSV e inserindo os dados na tabela
        # Substitua o caminho abaixo pelo caminho absoluto do arquivo CSV no seu computador
        try:
            print("passou")
            with open(r"C:\Users\User\Documents\portfolio\reservatrem\trens.csv", encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv, delimiter=",")
                for linha in leitor_csv:
                    cursor.execute(
                        """
                        INSERT INTO train_info 
                        (Numero_Trem, Codigo_Estacao, Nome_Estacao, Hora_Chegada, Hora_Partida, Distancia, Codigo_Estacao_Origem, Nome_Estacao_Origem, Codigo_Estacao_Destino, Nome_Estacao_Destino)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, linha)
        except FileNotFoundError:
            print("Arquivo não encontrado. Verifique se o arquivo está na pasta correta e tente novamente.")

        # Confirmando as alterações no banco de dados
        conexao.commit()

    except pyodbc.Error as erro:
        print(f"Erro ao inserir os dados: {erro}")

    finally:
        # Fechando a conexão com o banco de dados
        cursor.close()
        conexao.close()

