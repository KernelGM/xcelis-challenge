import numpy as np
import pandas as pd

from modules.folders import output
from modules.get_demands import Demands
from modules.get_hubs import Hubs


class Framework:
    def __init__(self):
        self.hub = Hubs().hubs
        self.demands = Demands().demands

    def compare_sheets(self):
        cond = self.demands["COD org"].isin(self.hub["COD inicial"])
        cond.to_csv(f"{output}/teste.csv", index=False, header=False)
