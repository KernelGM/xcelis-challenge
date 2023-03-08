from datetime import datetime

from loguru import logger

from modules.folders import logs

now_time = datetime.today().strftime("%d-%m-%Y_%H")


class Logs:
    def __init__(self) -> None:
        ...

    def init_logs(self):
        logger.add(
            sink=f"{logs}/{now_time}.log",
            format="{level} - {time:DD/MM/YY - HH:mm:ss} - {message}",
        )

        logger.debug("<!--=====Software iniciado=====-->")

    def finish_logs(self):
        logger.debug("<!--=====Software encerrado=====-->")
