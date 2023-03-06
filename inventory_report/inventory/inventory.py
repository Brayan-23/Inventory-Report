from inventory_report.reports.simple_report import SimpleReport
import xmltodict
import csv
import json
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        leitura = ""
        if ".csv" in path:
            leitura = cls.reader_csv(path)
        elif ".json" in path:
            leitura = cls.reader_json(path)
        else:
            leitura = cls.reader_xml(path)

        return cls.simple_complete(leitura, type)

    @classmethod
    def reader_csv(cls, path):
        with open(path, encoding="utf-8", mode="r") as file:
            read = csv.DictReader(file, delimiter=",")
            lista = []
            for inventory in read:
                lista.append(inventory)
            return lista

    @classmethod
    def reader_json(cls, path):
        with open(path, encoding="utf-8", mode="r") as file:
            read = json.load(file)
            return read

    @classmethod
    def reader_xml(cls, path):
        with open(path, encoding="utf -8", mode="r") as file:
            read = xmltodict.parse(file.read())
            return read["dataset"]["record"]

    @classmethod
    def simple_complete(cls, data, type):
        if type.lower() == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)


print(Inventory.import_data("inventory_report/data/inventory.xml", 'simples'))
