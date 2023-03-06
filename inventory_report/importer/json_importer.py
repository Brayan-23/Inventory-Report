from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.json'):
            with open(path, encoding="utf-8", mode="r") as file:
                read = json.load(file)
                return read
        else:
            raise ValueError('Arquivo inválido')
