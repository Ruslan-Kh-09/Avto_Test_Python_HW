from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 25", "+79991112233"),
    Smartphone("Samsung", "Galaxy S20", "+78881112233"),
    Smartphone("Xiaomi", "Redmi Note 13", "+77073002030"),
    Smartphone("Google", "Pixel 8", "+79188782233"),
    Smartphone("Xiaomi", "Redmi Note 15", "+78007007799"),
    Smartphone("Apple", "iPhone 25", "+79981112233"),
    Smartphone("Samsung", "Galaxy S20", "+78781112233"),
    Smartphone("Xiaomi", "Redmi Note 13", "+77573002030"),
    Smartphone("Google", "Pixel 8", "+79198782233"),
    Smartphone("Xiaomi", "Redmi Note 15", "+78107007799")
]

print('Каталог смартфонов:')
for phone in catalog:
    print(f'{phone.brand} - {phone.model}, {phone.phone_number}')
