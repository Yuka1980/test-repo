from smartphone import Smartphone 

catalog = []
# создаем пять разных экземпляра класса Smartphone с разными марками, моделями, абонентскими номерами.
phone1 = Smartphone("Samsung", "Galaxy S21", "+79181718000")
phone2 = Smartphone("Xiaomi", "Mi 11", "+79181718111")
phone3 = Smartphone("Google", "Pixel 5", "+79181718222")
phone4 = Smartphone("Motorola", "StarTac", "+79181713330")
phone5 = Smartphone("Apple", "13 Promax", "+79181480008")
# каждый экземпляр добавляется в catalog.
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
