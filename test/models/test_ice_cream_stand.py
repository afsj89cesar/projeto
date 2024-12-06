import pytest
from src.models.ice_cream_stand import IceCreamStand

@pytest.fixture
def ice_cream_stand():
    """Criando IceCreamStand."""
    return IceCreamStand("Sorveteria do João", "Sorvetes", ["Chocolate", "Baunilha", "Morango"])

class TestIceCreamStand:
    def test_flavors_available(self, ice_cream_stand):
        result = ice_cream_stand.flavors_available()
        assert "Chocolate" in result, "Erro: Sabor esperado não listado."
        assert "Baunilha" in result, "Erro: Sabor esperado não listado."
        assert "Morango" in result, "Erro: Sabor esperado não listado."

    def test_flavors_available_empty(self):
        stand = IceCreamStand("Sorveteria Vazios", "Sorvetes", [])
        result = stand.flavors_available()
        assert result == "Estamos sem estoque atualmente!", "Erro: Mensagem incorreta para estoque vazio."

    def test_find_flavor_found(self, ice_cream_stand):
        result = ice_cream_stand.find_flavor("Baunilha")
        assert result == "Temos no momento o sabor Baunilha!", "Erro: Sabor existente não encontrado."

    def test_find_flavor_not_found(self, ice_cream_stand):
        result = ice_cream_stand.find_flavor("Limão")
        assert result == "Não temos no momento o sabor Limão!", "Erro: Sabor inexistente reportado como disponível."

    def test_add_flavor_new(self, ice_cream_stand):
        result = ice_cream_stand.add_flavor("Limão")
        assert result == "Limão adicionado ao estoque!", "Erro: Sabor novo não foi adicionado corretamente."
        assert "Limão" in ice_cream_stand.flavors, "Erro: Sabor novo não foi adicionado à lista."

    def test_add_flavor_existing(self, ice_cream_stand):
        result = ice_cream_stand.add_flavor("Chocolate")
        assert result == "\nSabor já disponível!", "Erro: Sabor existente não encontrado."