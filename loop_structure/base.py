from faker import Faker

fake = Faker()

names = [fake.name() for _ in range(5)]

assert len(names) == 5

for name in names:
    print(name)