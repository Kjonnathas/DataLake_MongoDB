from pymongo import MongoClient
from pymongo.database import Database
from dotenv import load_dotenv
import os
import yfinance as yf
import pandas as pd
import pyodbc
import logging
from datetime import datetime
from typing import List

load_dotenv()

log_path = os.getenv("LOG_PATH")

date = datetime.today()
day = date.day
month = date.month
year = date.year

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=os.path.join(log_path, f"log_main_{day}_{month}_{year}.log"),
    filemode="a",
)


def extract_data_yfinance(
    ticker_list: List, start_data: str, end_data: str
) -> list | None:
    """
    Extrai dados históricos de ações do Yahoo Finance para uma lista de tickers fornecidos.

    Args:
        ticker_list (list): Lista de tickers de ações para os quais os dados serão recuperados.
        start_data (str): Data de início para o período de dados a ser recuperado (formato 'YYYY-MM-DD').
        end_data (str): Data de fim para o período de dados a ser recuperado (formato 'YYYY-MM-DD').


    Returns:
        list | None: Lista de DataFrames pandas, cada um contendo os dados históricos de uma ação, ou None caso ocorra um erro.

    Notas:
        - Os dados são recuperados para o período de 1º de janeiro de 2010 até 31 de dezembro de 2015.
        - Os DataFrames são enriquecidos com uma coluna "Ticker" para identificar a ação.
        - A função usa a biblioteca `yfinance` para realizar o download dos dados históricos.
        - Em caso de erro durante a extração, a função loga o erro e retorna None.
    """
    try:
        df_list = []

        for ticker in ticker_list:
            ticker_data = yf.download(
                ticker, start=start_data, end=end_data, group_by="ticker"
            )

            ticker_data.columns = ticker_data.columns.droplevel(0)
            ticker_data.reset_index(inplace=True)
            ticker_data.loc[:, "Ticker"] = ticker
            df_list.append(ticker_data)

        logging.info("Dados extraídos da api do yfinance com sucesso!")

        return df_list

    except Exception as e:
        logging.error(
            f"Ocorreu um erro ao extrair os dados da api do yfinance.\n\nErro: {e}"
        )

        return None


def transform_dataframe(df_list: List) -> pd.DataFrame | None:
    """
    Transforma uma lista de DataFrames em um único DataFrame consolidado.

    Args:
    -----
        df_list (list): Lista de DataFrames pandas a serem concatenados.

    Returns:
    -------
        pd.DataFrame | None: Um único DataFrame concatenado se `df_list` não estiver vazio; caso contrário, retorna None.
    """
    return pd.concat(df_list) if df_list else None


def connect_to_mongo(uri: str, database: str) -> Database:
    """
    Estabelece uma conexão com um banco de dados MongoDB.

    Args:
    -----
        uri (str): URI de conexão para o servidor MongoDB.
        database (str): Nome do banco de dados ao qual a conexão será feita.

    Returns:
    --------
        Database: Objeto `Database` representando o banco de dados conectado.
    """
    client = MongoClient(uri)
    database = client[database]

    return database


def delete_data_from_mongo(database: str) -> None:
    """
    Remove todas as coleções de um banco de dados MongoDB.

    Args:
    -----
        database (str): Instância do banco de dados MongoDB de onde as coleções serão removidas.

    Returns:
    --------
        None: A função não retorna nenhum valor. Registra mensagens no log sobre o status da operação.

    Notas:
    ------
        - A função itera por todas as coleções do banco de dados e as remove completamente usando o método `drop`.
        - Diferentemente de `delete_many`, que remove apenas documentos, o método `drop` exclui a coleção inteira.
        - Mensagens de sucesso ou erros são registradas no sistema de logging.
    """
    try:
        for collection_name in database.list_collection_names():
            collection = database[collection_name]
            collection.drop()
            logging.info("Operação de exclusão de coleções efetuada com sucesso!")
    except Exception as e:
        logging.error(
            f"Ocorreu um erro durante a operação de exclusão de coleções no MongoDB.\n\nErro: {e}"
        )


def load_to_mongo(dataframe: pd.DataFrame, database: str, uri: str) -> None:
    """
    Carrega dados de um DataFrame pandas em um banco de dados MongoDB.

    Args:
    -----
        dataframe (pd.DataFrame): O DataFrame contendo os dados a serem carregados.
        database (str): Nome do banco de dados MongoDB.
        uri (str): URI de conexão para o servidor MongoDB.

    Returns:
    --------
        None

    Logs:
    -----
        Registra mensagens indicando sucesso ou erros durante o processo de inserção dos dados.

    Notas:
    ------
        - Cada ticker único no DataFrame cria uma coleção separada no banco de dados.
        - Os dados de cada ticker são inseridos como uma lista de documentos.
    """
    df = dataframe.copy()

    database = connect_to_mongo(uri, database)

    try:
        for ticker in df.Ticker.unique():
            df_ticker = df[df.Ticker == ticker]

            ticker_name = df_ticker.Ticker.to_list()
            opening_price = df_ticker.Open.to_list()
            closing_price = df_ticker.Close.to_list()
            highest_price = df_ticker.High.to_list()
            lowest_price = df_ticker.Low.to_list()
            date = df_ticker.Date.to_list()

            document_list = []

            for _ in range(len(df_ticker)):
                document_list.append(
                    {
                        "Ticker": ticker_name[_],
                        "Data": date[_],
                        "Preço de Abertura": opening_price[_],
                        "Preço de Fechamento": closing_price[_],
                        "Preço Mais Alto": highest_price[_],
                        "Preço Mais Baixo": lowest_price[_],
                    }
                )

            database[ticker].insert_many(document_list)

            logging.info(f"Dados de {ticker} registrados com sucesso!")

        logging.info("Carregamento finalizado com sucesso no MongoDB!")

    except Exception as e:
        logging.error(
            f"Ocorreu um erro durante a operação de inserção de coleções no MongoDB.\n\nErro: {e}"
        )


def connect_to_mysql(
    driver: str, server: str, db: str, user: str, password: str
) -> pyodbc.Connection:
    """
    Estabelece uma conexão com um banco de dados MySQL usando o pyodbc.

    Args:
    -----
        driver (str): Nome do driver ODBC a ser utilizado.
        server (str): Endereço ou nome do servidor.
        db (str): Nome do banco de dados.
        user (str): Nome de usuário para autenticação.
        password (str): Senha para autenticação.

    Returns:
    --------
        pyodbc.Connection: Objeto de conexão para interagir com o banco de dados MySQL.
    """
    conn = pyodbc.connect(
        f"Driver={driver};"
        f"Server={server};"
        f"Database={db};"
        f"UID={user};"
        f"PWD={password};"
    )

    return conn


def load_to_mysql(con: pyodbc.Connection, dataframe: pd.DataFrame) -> None:
    """
    Carrega dados de um DataFrame pandas em uma tabela de um banco de dados MySQL.

    Args:
    -----
        con (pyodbc.Connection): Objeto de conexão com o banco de dados MySQL.
        dataframe (pd.DataFrame): O DataFrame contendo os dados a serem inseridos.

    Returns:
    --------
        None

    Logs:
    -----
        Registra mensagens indicando sucesso ou erros durante o processo de criação da tabela ou inserção dos dados.

    Notas:
    ------
        - Cria uma tabela `tbl_historico_acoes` caso ela não exista.
        - Os dados do DataFrame são inseridos na tabela linha por linha.
    """
    df = dataframe.copy()

    if con:
        try:
            cursor = con.cursor()

            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS tbl_historico_acoes (
                id INT PRIMARY KEY AUTO_INCREMENT,
                ticker VARCHAR(10) NOT NULL,
                open FLOAT NOT NULL,
                close FLOAT NOT NULL,
                high FLOAT NOT NULL,
                low FLOAT NOT NULL,
                volume FLOAT NOT NULL,
                data DATE NOT NULL
            );
            TRUNCATE TABLE tbl_historico_acoes;
            """,
                multi=True,
            )

            for _, row in df.iterrows():
                cursor.execute(
                    """
                        INSERT INTO tbl_historico_acoes (ticker, open, close, high, low, volume, data)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row["Ticker"],
                    row["Open"],
                    row["Close"],
                    row["High"],
                    row["Low"],
                    row["Volume"],
                    row["Date"],
                )

            con.commit()

            logging.info("Dados inseridos na tabela com sucesso!")

        except pyodbc.Error as e:
            logging.error(f"Erro durante a execução do banco de dados.\n\nErro: {e}")
            con.rollback()

        finally:
            if "cursor" in locals():
                cursor.close()
            con.close()


def main(tickers: List, start_data: str, end_data: str) -> None:
    driver = os.getenv("MYSQL_DRIVER")
    server = os.getenv("MYSQL_SERVER")
    database = os.getenv("MYSQL_DATABASE")
    username = os.getenv("MYSQL_USERNAME")
    password = os.getenv("MYSQL_PASSWORD")
    mongo_uri = os.getenv("MONGO_URI")
    mongo_db = os.getenv("MONGO_DATABASE")

    data = extract_data_yfinance(tickers, start_data=start_data, end_data=end_data)
    delete_data_from_mongo(mongo_db)
    transform_data = transform_dataframe(data)
    load_to_mongo(transform_data, mongo_db, mongo_uri)
    conn_mysql = connect_to_mysql(driver, server, database, username, password)
    load_to_mysql(conn_mysql, transform_data)


if __name__ == "__main__":
    tickers = [
        "EQTL3.SA",
        "PETR4.SA",
        "VALE3.SA",
        "ITUB4.SA",
        "ITSA4.SA",
        "GOLL4.SA",
        "MGLU3.SA",
        "BBDC3.SA",
        "BBAS3.SA",
        "ABEV3.SA",
        "JBSS3.SA",
        "WEGE3.SA",
        "BPAC11.SA",
        "SANB11.SA",
        "SUZB3.SA",
        "GGBR4.SA",
    ]

    main(tickers=tickers, start_data="2010-01-01", end_data="2024-11-30")
