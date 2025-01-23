import csv
import os
from pathlib import Path


def ler_csv(path_arquivo: Path) -> list[dict]:
    caminho = Path(path_arquivo)
    if os.path.exists(caminho):
        extensao = os.path.splitext(caminho)[1]
        if extensao == ".csv":
            lista_valores: list = []
            with open(caminho, "r", encoding="utf-8") as arquivo:
                linhas = csv.DictReader(arquivo)
                for li in linhas:
                    lista_valores.append(li)
            return lista_valores

    return "Arquivo não encontrado, ou a extensão é diferente de .CSV"


if __name__ == "__main__":
    la = ler_csv(
        r"C:\Users\thiag\Desktop\Jornada_de_dados\bootcamp_python\arquivos.csv"
    )
    print(la)
