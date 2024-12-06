import pytest
from src.models.restaurant import Restaurant

class TestRestaurant:
    def setup_method(self):
        """Configura um restaurante padrão para uso nos testes."""
        self.restaurant = Restaurant("Teste Restaurante", "Italiana")

    def test_describe_restaurant(self):
        """Testa a descrição do restaurante."""
        assert self.restaurant.describe_restaurant() == (
            "O restaurante Teste Restaurante serve comida do tipo Italiana. Já atendeu 0 clientes."
        ), "Descrição do restaurante está incorreta."

    def test_open_restaurant(self):
        """Testa a abertura do restaurante."""
        assert self.restaurant.open_restaurant() == "Teste Restaurante agora está aberto!", (
            "Abertura do restaurante não está funcionando corretamente."
        )
        assert self.restaurant.is_open, "Atributo `is_open` não foi ajustado corretamente ao abrir."

    def test_close_restaurant(self):
        """Testa o fechamento do restaurante."""
        self.restaurant.open_restaurant()  # Abrir para poder fechar
        assert self.restaurant.close_restaurant() == "Teste Restaurante agora está fechado!", (
            "Fechamento do restaurante não está funcionando corretamente."
        )
        assert not self.restaurant.is_open, "Atributo `is_open` não foi ajustado corretamente ao fechar."

    def test_set_number_served(self):
        """Testa a definição de número de clientes atendidos."""
        self.restaurant.set_number_served(50)
        assert self.restaurant.number_served == 50, "Número de clientes atendidos foi definido incorretamente."

        with pytest.raises(ValueError, match="O número de clientes atendidos deve ser maior ou igual a zero."):
            self.restaurant.set_number_served(-10)

    def test_increment_number_served(self):
        """Testa o incremento do número de clientes atendidos."""
        self.restaurant.increment_number_served(10)
        assert self.restaurant.number_served == 10, "Incremento no número de clientes atendidos foi incorreto."

        with pytest.raises(ValueError, match="O incremento de clientes deve ser maior ou igual a zero."):
            self.restaurant.increment_number_served(-5)
