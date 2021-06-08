import faker
from faker import Faker
fake = Faker()




class cards:
   def __init__(self, name, last_name, company_name, mail):
       self.name = name
       self.last_name = last_name
       self.company_name = company_name
       self.mail = mail
   def __str__(self):
       return f'{self.name} {self.last_name} {self.company_name} {self.mail}'

random_person = cards(name=fake.first_name(), last_name=fake.last_name(), company_name=fake.company(), mail=fake.email())
print(random_person)
name = [fake.first_name() for i in range(10)]
company_name = [fake.company() for i in range(10)]
mail = [fake.email() for x in range(10)]
last_name = [fake.last_name() for x in range(10)]

cards_list = cards(name=name, last_name=last_name, company_name=company_name, mail=mail)

by_name = sorted(cards_list, key=lambda card: cards.name)
by_last_name = sorted(cards_list, key=lambda card: cards.last_name)
by_email = sorted(cards_list, key=lambda card: cards.mail)


print(cards_list)










