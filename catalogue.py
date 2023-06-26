class Catalogue:
    products = []
    def __init__(self,name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in Catalogue.products if product.startswith(first_letter)]

    def __repr__(self):
        returning_string = f"Items in the {self.name} catalogue:\n"
        returning_string +="\n". join(sorted(Catalogue.products))
        return returning_string
