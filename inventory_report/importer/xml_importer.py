from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.xml'):
            with open(path, encoding="utf -8", mode="r") as file:
                read = xmltodict.parse(file.read())
                return read["dataset"]["record"]
        else:
            raise ValueError('Arquivo inválido')
