from modules.get_distances import Distances
from modules.get_hubs import Hubs
from modules.logs import Logs
from modules.time_meter import time_meter


@time_meter
def run():
    Logs().init_logs()
    # Distances().sheet_distance()
    Hubs().sheet_hubs()
    Logs().finish_logs()


if __name__ == "__main__":
    run()
