from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, lista):
        return f"""{cls.mais_antiga(lista)}
{cls.data_mais_atual(lista)}
{cls.empresa_mais_produtos(lista)}"""

    @classmethod
    def mais_antiga(cls, lista):
        older = datetime.today().date()
        for obj in lista:
            fabrication = obj["data_de_fabricacao"]
            if datetime.strptime(fabrication, "%Y-%m-%d").date() <= older:
                older = datetime.strptime(fabrication, "%Y-%m-%d").date()
        return f"Data de fabricação mais antiga: {older}"

    @classmethod
    def data_mais_atual(cls, lista):
        list_dates = []
        today = datetime.today().date()
        for obj in lista:
            validate = obj["data_de_validade"]
            if datetime.strptime(validate, "%Y-%m-%d").date() > today:
                list_dates.append(validate)
        result = min(list_dates)
        return f"Data de validade mais próxima: {result}"

    @classmethod
    def empresa_mais_produtos(cls, lista):
        emprises = {}
        for obj in lista:
            name = obj["nome_da_empresa"]
            if name not in emprises:
                emprises[name] = 1
            else:
                emprises[name] += 1

        result = sorted(
            emprises.items(), 
            key=lambda item: item[1], reverse=True)[0][0]
        return f'Empresa com mais produtos: {result}'


