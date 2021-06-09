import faker
from faker import Faker

fake = Faker()


class Cards:
    def __init__(self, name, last_name, company_name, mail):
        self.name = name
        self.last_name = last_name
        self.company_name = company_name
        self.mail = mail

    def __str__(self):
        return f'{self.name} {self.last_name} {self.company_name} {self.mail}'

    def __repr__(self):
        return f"Cards(name={self.name} last_name={self.last_name}, company_name={self.company_name}, mail={self.mail})"



card = Cards(name=fake.unique.first_name(), last_name=fake.unique.last_name(), company_name=fake.unique.company(), mail=fake.unique.email())
cards_list = []
for i in range(10):
    cards_list.append(card)

by_name = sorted(cards_list, key=lambda Cards: Cards.name)
by_last_name = sorted(cards_list, key=lambda Cards: Cards.last_name)
by_email = sorted(cards_list, key=lambda Cards: Cards.mail)

print(by_name)
print(by_last_name)
print(by_email)



