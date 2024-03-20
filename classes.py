import csv


class Product:

    def __init__(self, name, description, price, available):
        self.name = name
        self.description = description
        self.price = float(price)
        self.available = bool(available)

    def __str__(self):
        return f"{self.name} - R${self.price}"


class ProductList:
    """
    Classe para gerenciar uma lista de produtos.
    """

    def __init__(self):
        """
        Inicializa a lista de produtos.
        """
        self.products = []
        self.boot()

    def boot(self):
        """
        Carrega os produtos do arquivo CSV.
        """
        with open('data.csv', mode='r') as data_csv:
            reader = csv.reader(data_csv)
            for line in reader:
                name, description, price, available = line
                p = Product(name, description, float(price), available)
                self.products.append(p)
        self.sort_by_price_reverse()

        with open('data.csv', mode='w', newline='') as data_csv:
            writer = csv.writer(data_csv)
            for p in self.products:
                writer.writerow([p.name, p.description, p.price, p.available])

    def sort_by_price_reverse(self):
        """
        Ordena a lista de forma decrescente baseado no preço dos produtos.
        """
        self.products.sort(key=lambda x: x.price)

    def print_products(self):
        """
        Imprime os produtos na lista.
        """
        for produto in self.products:
            print(produto)

    def add_product(self, p):
        """
        Adiciona um novo produto à lista.
        Args:
            p: Um objeto da classe Product.
        """
        self.products.append(p)
        with open('data.csv', mode='a', newline='') as data_csv:
            writer = csv.writer(data_csv)
            writer.writerow([p.name, p.description, p.price, p.available])
        self.sort_by_price_reverse()
