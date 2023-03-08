import pandas as pd
from loguru import logger

from modules.folders import demands, output_demands


class Demands:
    def __init__(self) -> None:
        self.sheet_demands()

    def sheet_demands(self):
        self.demands = pd.read_csv(
            f"{demands}/pedidos000.csv",
            sep=";",
            skiprows=1,
            header=None,
            on_bad_lines="skip",
            low_memory=False,
            names=[
                "Id Pedido",
                "COD org",
                "COD dest",
            ],
            dtype={
                "Id Pedido": "int64",
                "COD org": "int64",
                "COD dest": "int64",
            },
        )

        self.demands.to_csv(
            f"{output_demands}/pedidos000.csv", index=False, header=False
        )

        logger.debug("DataFrame 'pedidos000.csv' analisado")
