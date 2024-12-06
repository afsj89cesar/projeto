from src.models.restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list=None):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        'Correção de bug: Certificar que a lista de sabores é inicializada corretamente'
        self.flavors = flavors_list if flavors_list else []

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e retorne como string."""
        'Refatoração: concatenar os sabores, tornando o código mais limpo e eficiente.'
        if self.flavors:
            result = "No momento temos os seguintes sabores de sorvete disponíveis:\n"
            result += "\n".join([f"\t-{flavor}" for flavor in self.flavors])
            return result
        return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        'Correção de bug: Retornar apenas o sabor requisitado'
        if flavor in self.flavors:
            return f"Temos no momento o sabor {flavor}!"
        return f"Não temos no momento o sabor {flavor}!"

    def add_flavor(self, flavor):
        """Adiciona o sabor informado ao estoque."""
        if flavor in self.flavors:
            return "\nSabor já disponível!"
        self.flavors.append(flavor)
        return f"{flavor} adicionado ao estoque!"