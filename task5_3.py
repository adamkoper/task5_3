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

    def __repr__(self):
        return f"Cards(name={self.name} last_name={self.last_name}, company_name={self.company_name}, mail={self.mail})"


card1 = cards(name=fake.unique.first_name(), last_name=fake.unique.last_name(),
              company_name=fake.unique.company(), mail=fake.unique.email())
card2 = cards(name=fake.unique.first_name(), last_name=fake.unique.last_name(),
              company_name=fake.unique.company(), mail=fake.unique.email())
card3 = cards(name=fake.unique.first_name(), last_name=fake.unique.last_name(),
              company_name=fake.unique.company(), mail=fake.unique.email())
card4 = cards(name=fake.unique.first_name(), last_name=fake.unique.last_name(),
              company_name=fake.unique.company(), mail=fake.unique.email())
card5 = cards(name=fake.unique.first_name(), last_name=fake.unique.last_name(),
              company_name=fake.unique.company(), mail=fake.unique.email())

cards_list = [card1, card2, card3, card4, card5]


by_name = sorted(cards_list, key=lambda cards: cards.name)
by_last_name = sorted(cards_list, key=lambda cards: cards.last_name)
by_email = sorted(cards_list, key=lambda cards: cards.mail)

print(card1)
print(by_name)
print(by_last_name)
print(by_email)



