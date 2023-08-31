from .models import Product
from faker import Faker
fake = Faker()


def seed_db(n):
    for i in range(0 , n):
        Product.objects.create(
            product=fake.product()
        )
