# ========================================
# Szkielet pliku: product.py
# Uzupelnij implementacje!
# ========================================

class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # TODO: Zapisz atrybuty name, price, quantity
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        if quantity < 0:
            raise ValueError("nie  moze byc ujemna ilosc produktu") 

        if price < 0:
            raise ValueError("nie  moze byc cena na -")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        # TODO: Dodaj ilosc do magazynu. Rzuc ValueError jesli amount < 0
        if amount < 0:
            raise ValueError("nie  moze byc ujemna ilosc produktu")
        self.quantity += amount

    def remove_stock(self, amount: int):
        # TODO: Usun ilosc z magazynu.
        # Rzuc ValueError jesli amount < 0 lub amount > quantity
        if amount < 0:
            raise ValueError("nie  moze byc ujemna ilosc produktu")
        if amount > self.quantity:
            raise ValueError("nie ma tylu produktow w magazynie")
        self.quantity -= amount

    def is_available(self) -> bool:
        # TODO: Zwroc True jesli quantity > 0
        if self.quantity > 0:
            return True

    def total_value(self) -> float:
        # TODO: Zwroc price * quantity
        return self.price * self.quantity