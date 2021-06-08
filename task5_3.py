import faker
from faker import Faker
fake = Faker()




class cards:
   def __init__(self, name, company_name):
       self.name = name
       self.company_name = company_name


bubu = cards(name=fake.name(), company_name=fake.company())
for _ in range(10):
    print(bubu.name, bubu.company_name)
    











