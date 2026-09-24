from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "IPhone 18 Pro", "+79001234567"),
    Smartphone("Samsung", "Galaxy S26 Ultra", "+79012345678"),
    Smartphone("Xiaomi", "17 Ultra", "+79023456789"),
    Smartphone("Huawei", "Pura 80 Ultra", "+79034567890"),
    Smartphone("One Plus", "One Plus 18", "+79045678901")
]
for Smartphone in catalog:
    print(Smartphone.brand, Smartphone.model, Smartphone.number)
