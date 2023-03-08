import pandas as pd

from modules.folders import output
from modules.get_demands import Demands
from modules.get_hubs import Hubs


class Framework:
    def __init__(self):
        self.hub = Hubs().hubs
        self.demands = Demands().demands
        self.hub_init = [cod_init for cod_init in self.hub["COD inicial"]]
        self.hub_end = [cod_end for cod_end in self.hub["COD final"]]
        self.demands_org = [cod_org for cod_org in self.demands["COD org"]]

    def compare_sheets(self):
        print(1405956 in self.hub["COD inicial"].unique())
        print(1405956 in set(self.hub["COD inicial"]))
        # print(self.demands["COD org"].isin(self.hub["COD inicial"]))
        # cond.to_csv(f"{output}/teste.csv", index=False, header=False)
