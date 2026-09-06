from faker import Faker

generator = Faker()
print("Имя:", generator.name())
print("Адрес:", generator.address())
