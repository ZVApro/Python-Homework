from smartphone import Smartphone

catalog = [
    Smartphone("HUAWEI", "Mate X9", "+7909000000"),
    Smartphone("Apple", "iPhone 17", "+7909000001"),
    Smartphone("Xiaomi", "Redmi Note 12", "+77909000002"),
    Smartphone("HONOR", "X9b", "+7909000003"),
    Smartphone("OPPO", "A6 Pro", "+7909000004")
]
for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')