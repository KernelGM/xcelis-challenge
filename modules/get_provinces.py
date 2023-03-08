import pandas as pd
from loguru import logger

from modules.folders import data, output


class Provinces:
    def __init__(self) -> None:
        self.sheet_provinces()

    def sheet_provinces(self):
        self.prov = pd.read_csv(
            f"{data}/municipios.csv",
            sep=";",
            header=None,
            on_bad_lines="skip",
            low_memory=False,
            names=[
                "Município - UF",  # UF
                "COD mun",  # Cod
            ],
            encoding="cp1252",
        )

        # Remove first line "fake_header"
        self.prov = self.prov.tail(-1)

        self.prov["name"] = self.prov["Município - UF"].apply(
            lambda x: x.split("-", 1)[0].rstrip()
        )

        self.prov["uf"] = self.prov["Município - UF"].apply(
            lambda x: x.split("-")[-1].replace(" ", "")
        )

        self.prov.to_csv(f"{output}/provinces.csv", index=False, header=False)

        logger.debug("DataFrame 'municipios.csv' corrigido")
