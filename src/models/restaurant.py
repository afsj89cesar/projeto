class Restaurant:
    """Modelo de restaurante para gerenciamento simples."""

    'Refatoração nas strings e algumas alterações nos métodos e seus atributos'

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0
        self.is_open = False
        ' Refatoração: Simplificação e uso de `.title()` diretamente.'

    def describe_restaurant(self):
        """Retorna uma descrição do restaurante."""
        'Bug corrigijo: Mensagem tinha um erro, repetição de cuisine_type'
        return (
            f"O restaurante {self.restaurant_name} serve comida do tipo {self.cuisine_type}. "
            f"Já atendeu {self.number_served} clientes."
        )

    def open_restaurant(self):
        """Abre o restaurante."""
        'open_restaurant tenta abrir o restaurante, mas define o atributo open como False em vez de True.'
        'number_served era ajustado para -2 quando o restaurante é aberto, acho que não tava certo'
        if not self.is_open:
            self.is_open = True
            return f"{self.restaurant_name} agora está aberto!"
        return f"{self.restaurant_name} já está aberto."

    def close_restaurant(self):
        """Fecha o restaurante."""
        'close_restaurant mudava number_served para 0 ao fechar o restaurante'
        if self.is_open:
            self.is_open = False
            return f"{self.restaurant_name} agora está fechado!"
        return f"{self.restaurant_name} já está fechado."

    def set_number_served(self, total_customers):
        """
        Define o número total de clientes atendidos.
        Aceita apenas valores não negativos.
        """
        'Refatoração: melhoria na mensagem de erro'
        if total_customers < 0:
            raise ValueError("O número de clientes atendidos não pode ser negativo.")
        self.number_served = total_customers

    def increment_number_served(self, more_customers):
        """
        Incrementa o número total de clientes atendidos.
        Aceita apenas valores positivos.
        """
        'Refatoração: validação simplificada'
        if more_customers < 0:
            raise ValueError("O incremento não pode ser negativo.")
        self.number_served += more_customers