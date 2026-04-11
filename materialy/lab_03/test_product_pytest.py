# ========================================
# Szkielet pliku: test_product_pytest.py
# Uzupelnij testy!
# ========================================


import pytest
from product import Product


@pytest.fixture
def product():
    # TODO: Zwroc instancje Product
    return Product("Laptop", 2999.99, 10)


def test_is_available(product):
    # TODO: assert product.is_available() == True
    assert product.is_available() == True


@pytest.mark.parametrize("amount, expected_quantity", [
    # TODO: Dodaj przypadki testowe
    # (5, 15),   # dodanie 5 do poczatkowych 10 = 15
    pytest.param(5, 15, id="add_5"),
    pytest.param(10, 20, id="add_10"),
    pytest.param(0, 10, id="add_0"),
    pytest.param(-5, 10, id="add_negative")
])

def test_add_stock_parametrized(product, amount, expected_quantity):
    # TODO: product.add_stock(amount), sprawdz product.quantity
    product.add_stock(amount)
    assert product.quantity == expected_quantity


def test_remove_stock_too_much_raises(product):
    # TODO: with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        product.remove_stock(15)


print("Uruchom testy komenda: pytest test_product_pytest.py -v")