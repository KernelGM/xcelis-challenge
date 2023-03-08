from os import listdir, path
from zipfile import ZipFile

from loguru import logger

from modules.folders import data


class ExtractFiles:
    def __init__(self) -> None:
        self.files_zip = [item for item in listdir(data) if item.endswith(".zip")]
        self.files = [file for file in self.files_zip]

    def extract(self):
        logger.debug(f"Arquivos a serem extraidos: {self.files}")
        for file in self.files:
            with ZipFile(f"{data}/{file}", "r") as zip:
                files = zip.namelist()
                for file in files:
                    filename, extension = path.splitext(file)
                    if extension == ".csv":
                        zip.extract(file, data)
        logger.debug("Extração completa")
