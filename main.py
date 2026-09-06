from faker import Faker

fake = Faker()
print("Случайное имя:", fake.name())
print("Случайный адрес:", fake.address())