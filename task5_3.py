from faker import Faker
fake = Faker()


class cards:
    def __init__(self, name, last_name, company_name, mail, job):
        self.name = name
        self.last_name = last_name
        self.company_name = company_name
        self.mail = mail
        self.job = job

    def __str__(self):
        return f'{self.name} {self.last_name} {self.mail}'

    def __repr__(self):
        return f"Cards(name={self.name} last_name={self.last_name}, job={self.job}, company_name={self.company_name}, mail={self.mail})"

    def contact(self):
        return f'Kontaktuję się z {self.name} {self.last_name} {self.job} {self.mail}'

    @property
    def label_lenght(self, name, last_name):
        return len(name)+1+len(last_name)


class BaseContact(cards):
    def __init__(self, phone, name, last_name, mail):
        self.name = name
        self.last_name = last_name
        self.mail = mail
        self.phone = phone

    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonię do {self.name} {self.last_name}'


class BusinessContact(cards):
    def __init__(self, work_phone, work_mail, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_phone = work_phone
        self.work_mail = work_mail

    def contact(self):
        return f'Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.last_name}'



def create_contacts(card_type, qnt = int()):
    base_card = [BaseContact(name = fake.first_name(),
                  last_name = fake.last_name(),
                  phone = fake.phone_number(),
                  mail = fake.ascii_email())
                  for i in range(qnt)]
    biz_card = [BusinessContact(name = fake.first_name(),
                  last_name = fake.last_name(),
                  mail = fake.ascii_email(),
                  company_name = fake.company(),
                  job = fake.job(),
                  work_phone = fake.phone_number(),
                  work_mail = fake.ascii_email())
                  for i in range(qnt)]

    if card_type == 'podstawowe':
        for card in base_card:
            print(card)
    elif card_type == 'biznesowe':
        for card in biz_card:
            print(card)

create_contacts(input('Wpisz "podstawowe" lub "biznesowe"'), int(input('Podaj liczbę osób do wygenerowania:')))














