import faker
from faker import Faker
fake = Faker()




class cards:
   def __init__(self, name, company_name, mail):
       self.name = name
       self.company_name = company_name
       self.mail = mail
   def __str__(self):
       return f'{self.name} {self.company_name} {self.mail}'


bubu = cards(name=fake.name(), company_name=fake.company(), mail=fake.email())
print(bubu)











