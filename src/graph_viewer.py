import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from main import connect_to_mysql
from warnings import filterwarnings
import os
from pyodbc import Connection
from typing import Tuple

filterwarnings("ignore")


def extract_data_from_mysql(
    first_ticker: str, second_ticker: str, con: Connection
) -> Tuple[pd.DataFrame, str, str]:
    """
    Extrai dados históricos de ações do banco de dados MySQL para os tickers fornecidos.

    Args:
    -----
        first_ticker (str): O ticker da primeira ação.
        second_ticker (str): O ticker da segunda ação.
        con (Connection): Conexão ativa com o banco de dados MySQL.

    Returns:
    --------
        tuple: Retorna uma tupla contendo:
            - pd.DataFrame: DataFrame contendo os dados históricos das ações filtradas pelos tickers.
            - str: O nome do primeiro ticker.
            - str: O nome do segundo ticker.

    Raises:
    -------
        Exception: Em caso de falha na execução da consulta ou manipulação dos dados.

    Notas:
    ------
        - A função formata a coluna de data no formato datetime.
        - A conexão é fechada automaticamente no bloco `finally`.
    """
    try:
        sql = f"SELECT * FROM db_acoes.tbl_historico_acoes WHERE ticker IN('{first_ticker}', '{second_ticker}')"
        cursor = con.cursor()
        cursor.execute(sql)
        columns = [desc[0] for desc in cursor.description]
        records = cursor.fetchall()

        df = pd.DataFrame.from_records(data=records, columns=columns)
        df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d")

        return df, first_ticker, second_ticker

    except Exception as e:
        print(f"Ocorreu um erro ao extrair os dados do banco de dados.\n\nErro: {e}")
    finally:
        if "cursor" in locals():
            cursor.close()
        conn.close()


def plot_graph(
    first_ticker: str, second_ticker: str, folder_to_save: str, con: Connection
) -> None:
    """
    Gera um gráfico de comparação entre duas ações ao longo do tempo e salva a imagem em uma pasta.

    Args:
    -----
        first_ticker (str): O ticker da primeira ação.
        second_ticker (str): O ticker da segunda ação.
        folder_to_save (str): Caminho da pasta onde o gráfico será salvo.
        con (Connection): Conexão ativa com o banco de dados MySQL.

    Returns:
    --------
        None: A função não retorna nenhum valor. Exibe o gráfico e salva a imagem.

    Raises:
    -------
        Exception: Em caso de falha na extração de dados ou na manipulação do gráfico.

    Notas:
    ------
        - O gráfico é salvo como um arquivo PNG no caminho especificado.
        - A função utiliza uma grade suave para melhor visualização.
    """
    df, t1, t2 = extract_data_from_mysql(first_ticker, second_ticker, con)

    df_t1 = df[df["ticker"] == t1]
    df_t2 = df[df["ticker"] == t2]

    plt.figure(figsize=(10, 6))

    plt.plot(
        df_t1["data"],
        df_t1["close"],
        label=t1,
        linestyle="-",
        linewidth=1,
        color="#fc913a",
    )

    plt.plot(
        df_t2["data"],
        df_t2["close"],
        label=t2,
        linestyle="-",
        linewidth=1,
        color="#8d5524",
    )

    plt.gca().xaxis.set_major_locator(mdates.YearLocator(1))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    plt.title(f"Comparação de {t1} e {t2} ao longo do tempo")
    plt.xlabel("Ano")
    plt.ylabel("Preço de Fechamento (R$)")
    plt.legend()
    plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.4)
    plt.box(False)
    plt.tight_layout()
    plt.tick_params(axis="x", length=0)
    plt.tick_params(axis="y", length=0)

    plt.savefig(
        os.path.join(folder_to_save, f"comparacao_entre_{t1}_{t2}.png"),
        format="png",
        dpi=300,
    )

    plt.show()


if __name__ == "__main__":
    driver = os.getenv("MYSQL_DRIVER")
    server = os.getenv("MYSQL_SERVER")
    database = os.getenv("MYSQL_DATABASE")
    username = os.getenv("MYSQL_USERNAME")
    password = os.getenv("MYSQL_PASSWORD")
    img_folder = os.getenv("IMG_PATH")

    conn = connect_to_mysql(driver, server, database, username, password)

    plot_graph("ITUB4.SA", "SANB11.SA", img_folder, conn)
