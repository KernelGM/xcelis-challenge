from modules.framework import Framework
from modules.get_demands import Demands
from modules.get_distances import Distances
from modules.get_hubs import Hubs
from modules.get_provinces import Provinces
from modules.logs import Logs
from modules.organizer import ExtractFiles
from modules.time_meter import time_meter


@time_meter
def run():
    Logs().init_logs()
    ExtractFiles().extract()
    Distances().sheet_distances()
    Hubs().sheet_hubs()
    Provinces().sheet_provinces()
    Demands().sheet_demands()
    Logs().finish_logs()


if __name__ == "__main__":
    run()
