from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.csv'):
            with open(path, encoding="utf-8", mode="r") as file:
                read = csv.DictReader(file, delimiter=",")
                lista = []
                for inventory in read:
                    lista.append(inventory)
                return lista
        else:
            raise ValueError('Arquivo inválido')
