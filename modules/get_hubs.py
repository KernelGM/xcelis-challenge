import pandas as pd
from loguru import logger

from modules.folders import data, output


class Hubs:
    def __init__(self) -> None:
        self.sheet_hubs()

    def sheet_hubs(self):
        self.hubs = pd.read_csv(
            f"{data}/hubs.csv",
            sep=";",
            skiprows=1,
            header=None,
            on_bad_lines="skip",
            low_memory=False,
            names=[
                "Nome HUB",  # nome da unidade de distribuição
                "COD inicial",  # primeiro município atendido pela unidade
                "COD final",  # último município atendido pela unidade
                "Capacidade Entrega",  # qtd de pedidos que podem ser enviados pela unidade em um dia # noqa: E501
            ],
            dtype={
                "Nome HUB": "str",
                "COD inicial": "int64",
                "COD final": "int64",
                "Capacidade Entrega": "int64",
            },
            encoding="cp1252",
        )

        self.hubs["type"] = self.hubs["Nome HUB"].apply(lambda x: x.split(" ", 1)[0])
        self.hubs["order"] = self.hubs["Nome HUB"].apply(lambda x: x.split(" ")[-1])
        self.hubs["province"] = self.hubs["Nome HUB"].apply(
            lambda x: x.split(" ")[1:-1]
        )

        self.hubs.to_csv(f"{output}/hubs.csv", index=False, header=False)

        logger.debug("DataFrame 'hubs.csv' corrigido")
