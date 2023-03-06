from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        leitura = ""
        if ".csv" in path:
            leitura = CsvImporter.import_data(path)
        elif ".json" in path:
            leitura = JsonImporter.import_data(path)
        else:
            leitura = XmlImporter.import_data(path)

        return cls.simple_complete(leitura, type)

    @classmethod
    def simple_complete(cls, data, type):
        if type.lower() == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)


print(Inventory.import_data("inventory_report/data/inventory.xml", 'simples'))
